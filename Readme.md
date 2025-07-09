Numerical Linear Algebra and Interpolation Toolkit

This repository contains implementations of classic numerical linear algebra and interpolation algorithms in both Python and MATLAB.

Included files:

Python:
- householder_qr_solver.py         # QR solver using Householder reflections
- cholesky_spd.py                 # Cholesky decomposition for SPD systems
- natural_cubic_spline_demo.py    # Natural cubic spline interpolation (from scratch)
- LU_decomposition.py             # LU decomposition and solver

MATLAB:
- householder_qr_solver.m         % QR solver using Householder (MATLAB built-in)
- cholesky_spd.m                  % Cholesky decomposition for SPD systems
- natural_cubic_spline_demo.m     % Natural cubic spline interpolation (from scratch)
- LU_decomposition.m              % LU decomposition and solver

How to use:

Python: Run the scripts directly, e.g.:
    python householder_qr_solver.py

MATLAB: Call the functions or scripts in the MATLAB console, e.g.:
    householder_qr_solver(A, b)

All files contain example usage.

MIT License.
