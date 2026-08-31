import numpy as np

def gradient_descent_step(values, gradients, learning_rate):
    """
    Returns: updated values and the predicted first-order objective change
    """
    updated = [v - learning_rate * g for v, g in zip(values, gradients)]
    delta_l_pred = sum(g * (u - v) for g, u, v in zip(gradients, updated, values))
    return updated, delta_l_pred