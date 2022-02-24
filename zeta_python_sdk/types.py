from enum import Enum, IntEnum
from typing import List

from construct import Optional
from solana.publickey import PublicKey

from .exceptions import InvalidProductException, InvalidSideException, NotSupportedException


class Wallet:
    """
    Base class for objects that can be used to sign provider transactions.
    """

    public_key: PublicKey

    def sign_transaction(self, txn):
        pass

    def sign_all_transactions(self, txns):
        pass


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


class Order:
    marketIndex: int
    market: PublicKey
    price: int
    size: int
    side: Side

    # Just an identifier, shouldn't be shown to users.
    orderId: int

    # Open orders account that owns the order.
    owner: PublicKey

    # Client order id.
    clientOrderId: int


def order_equals(a: Order, b: Order, cmpOrderId: bool = False) -> bool:
    order_id_match = True
    if order_id_match:
        order_id_match = a.orderId == b.orderId

    return (
        a.marketIndex == b.marketIndex
        and a.market == b.market
        and a.price == b.price
        and a.size == b.size
        and a.side == b.side
        and order_id_match
    )


class Position:
    marketIndex: int
    market: PublicKey
    position: int
    costOfTrades: int


def position_equals(a: Position, b: Position) -> bool:
    return (
        a.marketIndex == b.marketIndex
        and a.market == b.market
        and a.position == b.position
        and a.costOfTrades == b.costOfTrades
    )


class Level:
    price: int
    size: int


class DepthOrderBook:
    bids: List[Level]
    asks: List[Level]


class TopLevel:
    bid: Optional[Level]
    ask: Optional[Level]


class MarginType(Enum):
    # Margin for orders.
    INITIAL = "initial"

    # Margin for positions.
    MAINTENANCE = "maintenance"


class MarginRequirement:
    initialLong: int
    initialShort: int
    maintenanceLong: int
    maintenanceShort: int


class MarginAccountState:
    balance: int
    initialMargin: int
    maintenanceMargin: int
    unrealizedPnl: int
    availableBalanceInitial: int
    availableBalanceMaintenance: int


class CancelArgs:
    market: PublicKey
    orderId: int
    cancelSide: Side


class MarginParams:
    futureMarginInitial: int
    futureMarginMaintenance: int
    optionMarkPercentageLongInitial: int
    optionSpotPercentageLongInitial: int
    optionSpotPercentageShortInitial: int
    optionDynamicPercentageShortInitial: int
    optionMarkPercentageLongMaintenance: int
    optionSpotPercentageLongMaintenance: int
    optionSpotPercentageShortMaintenance: int
    optionDynamicPercentageShortMaintenance: int
    optionShortPutCapPercentage: int


class ProgramAccountType(Enum):
    MarginAccount = "MarginAccount"


class ClockData:
    timestamp: int
    slot: int
