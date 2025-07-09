import numpy as np


def householder_qr(A):
    """
    Compute the QR factorization of A using Householder reflections.
    A: (m x n) full rank matrix, m >= n
    Returns Q (m x m) unitary, R (m x n) upper-triangular (below diagonal zeros)
    """
    A = A.copy().astype(np.complex128)
    m, n = A.shape
    Q = np.eye(m, dtype=np.complex128)
    R = A.copy()

    for k in range(n):
        # Extract the vector to reflect
        x = R[k:, k]
        # Compute Householder vector
        alpha = -np.sign(x[0]) * np.linalg.norm(x)
        v = x.copy()
        v[0] -= alpha
        v /= np.linalg.norm(v)
        # Apply reflector to R
        R[k:, k:] -= 2.0 * np.outer(v, np.dot(v.conj().T, R[k:, k:]))
        # Apply reflector to Q
        Q[:, k:] -= 2.0 * np.outer(np.dot(Q[:, k:], v), v.conj().T)

    return Q, R


def solve_qr(A, b):
    """
    Solve A x = b when m = n, or the least-squares solution when m > n,
    using QR from Householder method.
    A: (m x n) full rank matrix, m >= n
    b: (m,) or (m x 1) vector
    Returns x of length n
    """
    A = A.copy().astype(np.complex128)
    b = b.copy().astype(np.complex128).reshape(-1)
    m, n = A.shape

    # Compute QR
    Q, R = householder_qr(A)
    # Compute Q^H b
    c = np.dot(Q.conj().T, b)
    # Extract top n components
    c1 = c[:n]
    # Extract R1 = top n rows of R, shape (n x n)
    R1 = R[:n, :]
    # Solve R1 x = c1
    x = np.linalg.solve(R1, c1)
    return x


if __name__ == "__main__":
    # Example usage
    np.random.seed(0)
    m, n = 60, 50
    # Random full rank complex matrix
    A = np.random.randn(m, n) + 1j * np.random.randn(m, n)
    b = np.random.randn(m) + 1j * np.random.randn(m)

    x = solve_qr(A, b)
    print("Solution x (first 5 entries):", x[:5])
    # Verify residual
    residual = np.linalg.norm(A @ x - b)
    print(f"Residual norm ||Ax - b|| = {residual:.2e}")
