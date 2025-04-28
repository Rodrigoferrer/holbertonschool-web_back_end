#!/usr/bin/env python3
"""Module python3"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
     Typed fn that returns a tuple of str and float
    """
    return (k, float(v ** 2))
