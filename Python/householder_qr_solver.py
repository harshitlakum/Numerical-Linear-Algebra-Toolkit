import numpy as np

# Set seed for reproducibility
np.random.seed(0)

# (a) Generate A with known QR factorization
R = np.triu(np.random.randn(50, 50))
Q, _ = np.linalg.qr(np.random.randn(50, 50))
A = Q @ R

# (b) Compute QR factorization of A using Householder (numpy.linalg.qr)
Q2, R2 = np.linalg.qr(A)

# Compute backward error and orthogonality error
backward_error = np.linalg.norm(Q2 @ R2 - A, 2) / np.linalg.norm(A, 2)
orthogonality_error = np.linalg.norm(Q2.T @ Q2 - np.eye(50), 2)

print("Relative backward error ||Q2*R2 - A|| / ||A||  =", backward_error)
print("Orthogonality error ||Q2^T*Q2 - I||             =", orthogonality_error)
