from enum import IntEnum
from typing import Dict, Optional

from anchorpy import Idl, error

DEX_ERRORS = {
    59: "Order does not exist",
    61: "Order would self trade",
}


class NativeErrorCodes(IntEnum):
    ZeroLamportsBalance = 10000
    InsufficientLamports = 10001
    UnconfirmedTransaction = 10002
    FailedToGetRecentBlockhash = 10003


NATIVE_ERRORS = {
    10000: [
        "Attempt to debit an account but found no record of a prior credit.",
        "Zero SOL in wallet.",
    ],
    10001: [
        "Insufficient lamports",
        "Insufficient SOL in wallet.",
    ],
    10002: [
        "Transaction was not confirmed",
        "Transaction was not confirmed. Please check transaction signature.",
    ],
    10003: [
        "Failed to get recent blockhash",
        "Failed to get recent blockhash. Please retry.",
    ],
}


def parse_idl_errors(idl: Idl) -> Dict[int, str]:
    errors = {}
    if idl.errors:
        for _error in idl.errors:
            errors[_error.code] = _error.msg or _error.name

    return errors


def parse_custom_errors(untranslated_error: str) -> Optional[error.ProgramError]:
    """
    Extract error code from custom non-anchor errors.
    """
    components = str(untranslated_error).split("custom program error: ")
    if len(components) != 2:
        return None

    try:
        error_code = int(components[1])
    except ValueError:
        return None

    # Parse user error
    error_msg = DEX_ERRORS.get(error_code)
    if error_msg is not None:
        return error.ProgramError(error_code, error_msg)

    return None
