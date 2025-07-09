import numpy as np
import matplotlib.pyplot as plt

def natural_cubic_spline(x, y):
    n = len(x) - 1
    h = np.diff(x)
    alpha = np.zeros(n)
    for i in range(1, n):
        alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])

    # Build tridiagonal system
    l = np.ones(n+1)
    mu = np.zeros(n)
    z = np.zeros(n+1)
    a = y.copy()
    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)

    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    # Natural spline boundary conditions
    l[n] = 1
    z[n] = 0
    c[n] = 0

    # Back substitution for c, then b and d
    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2*c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3*h[j])

    return a[:-1], b, c[:-1], d, x

def eval_spline(a, b, c, d, x_knots, x_eval):
    # Evaluate the spline at x_eval
    s = np.zeros_like(x_eval)
    for i in range(len(x_knots)-1):
        idx = (x_eval >= x_knots[i]) & (x_eval <= x_knots[i+1])
        dx = x_eval[idx] - x_knots[i]
        s[idx] = a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
    return s

if __name__ == "__main__":
    # Example data
    x = np.array([0, 1, 2, 3])
    y = np.array([5, 0, 0, 0])

    # (b) Compute spline coefficients
    a, b, c, d, x_knots = natural_cubic_spline(x, y)

    # (c) Plot the spline
    xx = np.linspace(np.min(x), np.max(x), 500)
    yy = eval_spline(a, b, c, d, x_knots, xx)

    plt.figure(figsize=(8,5))
    plt.plot(xx, yy, label="Natural Cubic Spline")
    plt.plot(x, y, 'ro', label="Data Points", markersize=8)
    plt.title("Natural Cubic Spline Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()
