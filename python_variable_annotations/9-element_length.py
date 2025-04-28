#!/usr/bin/env python3
"""Module python3"""


from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples
    where each tuple contains an element and its length.

    :param lst: An iterable containing sequences
    (strings, lists, tuples, etc.)
    :return: A list of tuples (element, length of the element)
    """
    return [(i, len(i)) for i in lst]
