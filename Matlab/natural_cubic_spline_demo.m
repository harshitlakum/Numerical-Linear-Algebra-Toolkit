% Given points
x = [0 1 2 3];
y = [5 0 0 0];

% Compute natural cubic spline (returns piecewise polynomial, pp-form)
pp = spline(x, y);

% Display the piecewise cubic polynomials
disp('Piecewise cubic polynomials (for intervals [x_i, x_{i+1}]):');
for i = 1:length(x)-1
    % Coefficients for interval [x_i, x_{i+1}]
    coefs = pp.coefs(i, :); % Format: [a b c d], S(x) = a*(x-xi)^3 + b*(x-xi)^2 + c*(x-xi) + d
    fprintf('Interval [%.1f, %.1f]:\n', x(i), x(i+1));
    fprintf('  S(x) = %.4f*(x-%.1f)^3 + %.4f*(x-%.1f)^2 + %.4f*(x-%.1f) + %.4f\n', ...
        coefs(1), x(i), coefs(2), x(i), coefs(3), x(i), coefs(4));
end

% Plot (optional)
xx = linspace(0, 3, 200);
yy = ppval(pp, xx);

figure;
plot(x, y, 'ro', 'MarkerSize', 8, 'LineWidth', 2); hold on;
plot(xx, yy, 'b-', 'LineWidth', 2);
grid on;
legend('Data points', 'Natural cubic spline');
xlabel('x'); ylabel('y');
title('Natural Cubic Spline Interpolation');
