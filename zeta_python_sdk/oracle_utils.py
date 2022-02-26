import math

from .exceptions import OutOfBoundsException


def ERR_BUFFER_OUT_OF_BOUNDS():
    return OutOfBoundsException()


def ERR_INVALID_ARG_TYPE(name: str, expected: str, actual):
    return Exception(f'The "{name}" argument must be of type {expected}. Received {actual}')


def ERR_OUT_OF_RANGE(string: str, range: str, received: int):
    return Exception(
        f'The value of "{string}" is out of range. It must be of {range}. Received {received}'
    )


def validate_number(value, name):
    if type(value) != int:
        raise ERR_INVALID_ARG_TYPE(name, "int", value)


def bounds_error(value: int, length: int):
    if math.floor(value) != value:
        validate_number(value, "offset")
        raise ERR_OUT_OF_RANGE("offset", "an integer", value)

    if length > 0:
        raise ERR_BUFFER_OUT_OF_BOUNDS()

    raise ERR_OUT_OF_RANGE("offset", f">= 0 and <= {length}", value)
