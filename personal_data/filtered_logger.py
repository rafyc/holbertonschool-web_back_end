#!/usr/bin/env python3
"""
Main file
"""
import re
from typing import List, Tuple
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        formated = filter_datum(self.fields,
                                RedactingFormatter.REDACTION,
                                super().format(record),
                                      RedactingFormatter.SEPARATOR)
        return formated

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message obfuscated by 'redaction' argument
    """
    for i in fields:
        message = re.sub(i + '=.+?' + separator,
                         i + '=' + redaction + separator,
                         message)
    return message
