class InvalidSideException(Exception):
    """Invalid side"""


class NotSupportedException(Exception):
    """Not supported by dummy wallet"""


class InvalidProductException(Exception):
    """Invalid product type"""


class OutOfBoundsException(Exception):
    """Attempt to access memory outside buffer bounds"""
