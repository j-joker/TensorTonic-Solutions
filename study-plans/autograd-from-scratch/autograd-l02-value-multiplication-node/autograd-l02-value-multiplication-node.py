import numpy as np

def value_multiplication_node(left, right, output_id):
    """
    Returns: a multiplication node that retains the two supplied leaf records as ordered parents
    """
    return {
        "id": output_id,
        "data": left["data"] * right["data"],
        "op": "*",
        "grad": 0.0,
        "parents": [left, right],
    }
