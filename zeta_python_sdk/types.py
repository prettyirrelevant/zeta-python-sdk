from enum import Enum, IntEnum

from construct import Optional
from solana.publickey import PublicKey

from .exceptions import InvalidProductException, InvalidSideException, NotSupportedException


class Wallet:
    """
    Base class for objects that can be used to sign provider transactions.
    """

    public_key: PublicKey

    def sign_transaction(self, txn):
        raise NotImplementedError

    def sign_all_transactions(self, txns):
        raise NotImplementedError


class DummyWallet(Wallet):
    def __init__(self) -> None:
        super().__init__()

    def sign_transaction(txn):
        raise NotSupportedException

    def sign_all_transactions(txns):
        raise NotSupportedException

    @property
    def public_key(self):
        raise NotSupportedException


class Side(IntEnum):
    BID = 0
    ASK = 1


def to_program_side(side: Side):
    if side == side.BID.value:
        return {"bid": {}}
    if side == side.ASK.value:
        return {"ask": {}}

    raise InvalidSideException


class Kind(Enum):
    UNINITIALIZED = "uninitialized"
    CALL = "call"
    PUT = "put"
    FUTURE = "future"


def to_product_kind(kind: dict) -> Optional[Kind]:
    if Kind.CALL.value in kind:
        return Kind.CALL

    if Kind.PUT.value in kind:
        return Kind.PUT

    if Kind.FUTURE.value in kind:
        return Kind.FUTURE

    #  We don't expect uninitialized.
    raise InvalidProductException
