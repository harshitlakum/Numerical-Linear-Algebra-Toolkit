import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Given points
x = np.array([0, 1, 2, 3])
y = np.array([5, 0, 0, 0])

# Compute the natural cubic spline
spline = CubicSpline(x, y, bc_type='natural')

# Show the piecewise cubic coefficients
print("Piecewise cubic coefficients (intervals are [x[i], x[i+1]]):")
for i in range(len(x)-1):
    coefs = spline.c[:, i]  # coefs: [a, b, c, d], S(x) = a*(x-xi)^3 + b*(x-xi)^2 + c*(x-xi) + d
    print(f"Interval [{x[i]}, {x[i+1]}]:")
    print(f"  S(x) = {coefs[0]:.4f}*(x-{x[i]})^3 + {coefs[1]:.4f}*(x-{x[i]})^2 + {coefs[2]:.4f}*(x-{x[i]}) + {coefs[3]:.4f}")

# Plot (optional)
xx = np.linspace(0, 3, 200)
yy = spline(xx)

plt.plot(x, y, 'o', label='Data points')
plt.plot(xx, yy, label='Natural cubic spline')
plt.legend()
plt.grid(True)
plt.show()
