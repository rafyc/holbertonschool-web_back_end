#!/usr/bin/env python3
"""
Main file
"""
import re
from typing import List, Tuple


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    replace string
    """
    pattern1 = r"(?<=password=)([^;\s]+)"
    pattern2 = r"(?<=date_of_birth=)([^;\s]+)"

    result1 = re.sub(pattern1, redaction, message)
    result2 = re.sub(pattern2, redaction, result1)
    return result2
