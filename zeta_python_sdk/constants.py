from solana.publickey import PublicKey

MINTS = {
    "SOL": PublicKey("So11111111111111111111111111111111111111112"),
}

UNDERLYINGS = [MINTS["SOL"]]

DEX_PID = {
    "localnet": PublicKey("5CmWtUihvSrJpaUrpJ3H1jUa9DRjYz4v2xs6c3EgQWMf"),
    "devnet": PublicKey("5CmWtUihvSrJpaUrpJ3H1jUa9DRjYz4v2xs6c3EgQWMf"),
    "mainnet": PublicKey("zDEXqXEG7gAyxb1Kg9mK5fPnUdENCGKzWrM21RMdWRq"),
}

MAX_CANCELS_PER_TX = 4
MAX_GREEK_UPDATES_PER_TX = 20
MAX_SETTLEMENT_ACCOUNTS = 20
MAX_REBALANCE_ACCOUNTS = 20
MAX_SETTLE_ACCOUNTS = 5
MARKET_INDEX_LIMIT = 40

#  3 accounts per set * 9 = 27 + 2 = 29 accounts.
CLEAN_MARKET_LIMIT = 9
CRANK_ACCOUNT_LIMIT = 12

# This is the most we can load per iteration without
# hitting the rate limit.
MARKET_LOAD_LIMIT = 12

DEFAULT_ORDERBOOK_DEPTH = 5

PYTH_PRICE_FEEDS = {
    "localnet": {
        "SOL/USD": PublicKey("2pRCJksgaoKRMqBfa7NTdd6tLYe9wbDFGCcCCZ6si3F7"),
    },
    "devnet": {
        "SOL/USD": PublicKey("J83w4HKfqxwcq3BEMMkPFSppX3gqekLyLJBexebFVkix"),
    },
    "mainnet": {
        "SOL/USD": PublicKey("H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG"),
    },
}

USDC_MINT_ADDRESS = {
    "localnet": PublicKey("6PEh8n3p7BbCTykufbq1nSJYAZvUp6gSwEANAs1ZhsCX"),
    "devnet": PublicKey("6PEh8n3p7BbCTykufbq1nSJYAZvUp6gSwEANAs1ZhsCX"),
    "mainnet": PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"),
}

CLUSTER_URLS = {
    "localnet": "http://127.0.0.1:8899",
    "devnet": "https://api.devnet.solana.com",
    "mainnet": "https://api.mainnet-beta.solana.com",
}

# These are fixed and shouldn't change in the future.
NUM_STRIKES = 11
PRODUCTS_PER_EXPIRY = NUM_STRIKES * 2 + 1  # +1 for the future.
ACTIVE_EXPIRIES = 2
ACTIVE_MARKETS = ACTIVE_EXPIRIES * PRODUCTS_PER_EXPIRY
TOTAL_EXPIRIES = 6
TOTAL_MARKETS = PRODUCTS_PER_EXPIRY * TOTAL_EXPIRIES

DEFAULT_EXCHANGE_POLL_INTERVAL = 30
DEFAULT_MARKET_POLL_INTERVAL = 5
DEFAULT_CLIENT_POLL_INTERVAL = 20
DEFAULT_CLIENT_TIMER_INTERVAL = 1

VOLATILITY_POINTS = 5

# Numbers represented in BN are generally fixed point integers with precision of 6.
PLATFORM_PRECISION = 6
PRICING_PRECISION = 12
MARGIN_PRECISION = 8
POSITION_PRECISION = 3
