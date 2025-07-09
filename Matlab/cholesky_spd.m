function x = householder_qr_solver(A, b)
% Solves Ax = b (if m=n) or least-squares (if m>n) using QR (Householder)
% Inputs:  A (m x n), b (m x 1), both complex allowed, m >= n
% Output:  x (n x 1) solution

    [m, n] = size(A);

    % QR factorization (MATLAB uses Householder by default)
    [Q, R] = qr(A, 0);  % Economy QR: Q is m x n, R is n x n upper-triangular

    % Apply Q' to b
    c = Q' * b;

    % Solve R x = c (always n x n system)
    x = R \ c;

end
