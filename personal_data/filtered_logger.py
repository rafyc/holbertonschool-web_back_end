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
    i = 0
    while (i < len(fields)):
        pattern = r"(?<={}=)([^;\s]+)".format(fields[i])
        message = re.sub(pattern, redaction, message)
        i += 1
    return message
