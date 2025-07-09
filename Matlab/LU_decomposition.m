function natural_cubic_spline_demo()
    % Example data points
    x = [0 1 2 3];
    y = [5 0 0 0];
    n = length(x) - 1;
    h = diff(x);

    % Step 1: Set up the system for c (second derivatives at knots)
    A = zeros(n+1, n+1);
    rhs = zeros(n+1, 1);

    % Natural spline boundary conditions
    A(1,1) = 1;
    A(end,end) = 1;
    rhs(1) = 0;
    rhs(end) = 0;

    % Fill the tridiagonal system
    for i = 2:n
        A(i,i-1) = h(i-1);
        A(i,i) = 2*(h(i-1)+h(i));
        A(i,i+1) = h(i);
        rhs(i) = 3*((y(i+1)-y(i))/h(i) - (y(i)-y(i-1))/h(i-1));
    end

    % Solve for moments c
    c = A \ rhs;

    % Compute coefficients b and d
    b = zeros(n,1);
    d = zeros(n,1);
    for i = 1:n
        b(i) = (y(i+1) - y(i))/h(i) - h(i)*(2*c(i)+c(i+1))/3;
        d(i) = (c(i+1) - c(i)) / (3*h(i));
    end
    a = y(1:n)';

    % Plot the spline and data points
    xx = linspace(x(1), x(end), 500);
    yy = zeros(size(xx));
    for j = 1:n
        idx = xx >= x(j) & xx <= x(j+1);
        dx = xx(idx) - x(j);
        yy(idx) = a(j) + b(j)*dx + c(j)*dx.^2 + d(j)*dx.^3;
    end

    figure;
    plot(xx, yy, 'b-', 'LineWidth', 2); hold on;
    plot(x, y, 'ro', 'MarkerSize', 8, 'LineWidth', 2);
    xlabel('x'); ylabel('y');
    title('Natural Cubic Spline Interpolation');
    legend('Spline','Data points');
    grid on;
end
