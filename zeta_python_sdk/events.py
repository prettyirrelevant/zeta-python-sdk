import dataclasses
from enum import Enum


class EventType(Enum):
    # Refers to events that reflect a change in the exchange state.
    EXCHANGE = "EXCHANGE"

    # Expiration event for a zeta group.
    EXPIRY = "EXPIRY"

    # Events that reflect a change in user state
    # i.e. Margin account or orders
    USER = "USER"

    # A change in the clock account.
    CLOCK = "CLOCK"

    # A change in the greeks account.
    GREEKS = "GREEKS"

    # A trade event for the user margin account.
    TRADE = "TRADE"

    # An update in the orderbook
    ORDERBOOK = "ORDERBOOK"

    # On oracle account change.
    ORACLE = "ORACLE"


class OrderBookEvent:
    marketIndex: int
