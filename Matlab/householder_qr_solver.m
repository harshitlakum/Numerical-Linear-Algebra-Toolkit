% Set the random seed for reproducibility
rng(0);

% (a) Generate A with known QR factorization
R = triu(randn(50));
[Q, ~] = qr(randn(50));
A = Q * R;

% (b) Compute QR factorization of A
[Q2, R2] = qr(A);

% Compute backward error
backward_error = norm(Q2 * R2 - A, 2) / norm(A, 2);

% Compute orthogonality error
orthogonality_error = norm(Q2' * Q2 - eye(50), 2);

% Display results
fprintf('Relative backward error ||Q2*R2 - A|| / ||A||  = %.2e\n', backward_error);
fprintf('Orthogonality error ||Q2^T*Q2 - I||             = %.2e\n', orthogonality_error);
