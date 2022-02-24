from typing import List, Tuple

from solana.publickey import PublicKey


class State:
    admin: PublicKey
    stateNonce: int
    vaultNonce: int
    serumNonce: int
    mintAuthNonce: int
    numUnderlyings: int
    expiryIntervalSeconds: int
    newExpiryThresholdSeconds: int
    strikeInitializationThresholdSeconds: int
    pricingFrequencySeconds: int
    liquidatorLiquidationPercentage: int
    insuranceVaultLiquidationPercentage: int
    nativeTradeFeePercentage: int
    nativeUnderlyingFeePercentage: int
    nativeWhitelistUnderlyingFeePercentage: int
    nativeDepositLimit: int
    expirationThresholdSeconds: int
    padding: List[int]


class MarketIndexes:
    nonce: int
    initialized: bool
    indexes: List[int]


class Underlying:
    mint: PublicKey


class SettlementAccount:
    settlementPrice: int
    strikes: List[int]


class AnchorDecimal:
    flags: int
    hi: int
    lo: int
    mid: int


class PricingParameters:
    optionTradeNormalizer: AnchorDecimal
    futureTradeNormalizer: AnchorDecimal
    maxVolatilityRetreat: AnchorDecimal
    maxInterestRetreat: AnchorDecimal
    minDelta: int
    maxDelta: int
    minInterestRate: int
    maxInterestRate: int
    minVolatility: int
    maxVolatility: int


class MarginParameters:
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
    padding: List[int]


class HaltState:
    halted: bool
    spotPrice: int
    timestamp: int
    markPricesSet: List[bool]
    _markPricesSetPadding: List[bool]
    marketNodesCleaned: List[bool]
    _marketNodesCleanedPadding: List[bool]
    marketCleaned: List[bool]
    _marketCleanedPadding: List[bool]


class Strike:
    isSet: bool
    value: int


class Product:
    market: PublicKey
    strike: Strike
    dirty: bool
    kind: object


class ExpirySeries:
    activeTs: int
    expiryTs: int
    dirty: bool


class ZetaGroup:
    nonce: int
    vaultNonce: int
    insuranceVaultNonce: int
    frontExpiryIndex: int
    haltState: HaltState
    underlyingMint: PublicKey
    oracle: PublicKey
    greeks: PublicKey
    pricingParameters: PricingParameters
    marginParameters: MarginParameters
    products: List[Product]
    _productsPadding: List[Product]
    expirySeries: List[ExpirySeries]
    _expirySeriesPadding: List[ExpirySeries]
    totalInsuranceVaultDeposits: int
    padding: List[int]


class OpenOrdersMap:
    userKey: PublicKey


class Position:
    position: int
    costOfTrades: int
    closingOrders: int
    openingOrders: Tuple[int, int]


class MarginAccount:
    authority: PublicKey
    nonce: int
    balance: int
    forceCancelFlag: bool

    openOrdersNonce: List[int]
    seriesExpiry: List[int]
    positions: List[Position]
    _positionsPadding: List[Position]

    rebalanceAmount: int
    padding: List[int]


class ProductGreeks:
    delta: int
    vega: AnchorDecimal
    volatility: AnchorDecimal


class Greeks:
    nonce: int
    markPrices: List[int]
    _markPricesPadding: List[int]
    productGreeks: List[ProductGreeks]
    _productGreeksPadding: List[ProductGreeks]
    updateTimestamp: List[int]
    _updateTimestampPadding: List[int]
    retreatExpirationTimestamp: List[int]
    _retreatExpirationTimestampPadding: List[int]
    interestRate: List[int]
    _interestRatePadding: List[int]
    nodes: List[int]
    volatility: List[int]
    _volatilityPadding: List[int]
    nodeKeys: List[PublicKey]
    haltForcePricing: List[bool]
    padding: List[int]


class MarketNode:
    index: int
    nonce: int
    nodeUpdates: List[int]
    interestUpdate: int


class TradeEvent:
    marginAccount: PublicKey
    index: int
    costOfTrades: int
    size: int
    isBid: bool
    clientOrderId: int
    orderId: int


class InsuranceDepositAccount:
    nonce: int
    amount: int


class WhitelistInsuranceAccount:
    nonce: int
    userKey: PublicKey


class WhitelistDepositAccount:
    nonce: int
    userKey: PublicKey


class SocializedLossAccount:
    nonce: int
    overbankruptAmount: int


class WhitelistTradingFeesAccount:
    nonce: int
    userKey: PublicKey
