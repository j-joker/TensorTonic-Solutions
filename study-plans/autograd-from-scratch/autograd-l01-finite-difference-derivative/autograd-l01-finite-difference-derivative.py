import numpy as np


def finite_difference_derivative(coefficients, x, h):
    coeffs = np.asarray(coefficients, dtype=np.float64)

    # f(x) 和 f(x+h)，用 NumPy 的 polyval，它也是升幂顺序，正好对上
    fx   = np.polynomial.polynomial.polyval(x, coeffs)
    fxph = np.polynomial.polynomial.polyval(x + h, coeffs)

    slope = (fxph - fx) / h

    return (float(fx), float(fxph), float(slope))