import numpy as np


def gradient_check_product_chain(a, b, c, f, h):
    a, b, c, f, h = map(np.float64, (a, b, c, f, h))

    e = a * b + c
    loss = e * f

    analytic = [
        b * f,
        a * f,
        f,
        e,
    ]

    numerical = [
        (((a + h) * b + c) * f - loss) / h,
        ((a * (b + h) + c) * f - loss) / h,
        ((a * b + c + h) * f - loss) / h,
        (e * (f + h) - loss) / h,
    ]

    max_disagreement = max(
        abs(x - y) for x, y in zip(analytic, numerical)
    )

    return loss, analytic, numerical, max_disagreement