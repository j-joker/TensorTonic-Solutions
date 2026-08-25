import numpy as np


def scalar_expression_partials(a, b, c, h):
    # 先定义一个能算 d 的函数
    def d(x, y, z):
        return x * y + z

    # 基准值 d(a, b, c)
    d0 = d(a, b, c)

    # 三个偏导：每次只动一个变量，其余固定，用同一个 d0 做差值
    da = (d(a + h, b, c) - d0) / h
    db = (d(a, b + h, c) - d0) / h
    dc = (d(a, b, c + h) - d0) / h

    return (float(d0), float(da), float(db), float(dc))