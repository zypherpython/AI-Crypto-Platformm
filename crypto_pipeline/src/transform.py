import pandas as pd
import numpy as np
from datetime import datetime

def clean_data(raw_data):

    df = pd.DataFrame(raw_data).T

    print("RAW SHAPE:", df.shape)
    print("COLUMNS:", df.columns.tolist())
    print(df.head())

    df = df.dropna(subset=["usd", "usd_market_cap", "usd_24h_vol"])

    df.index = df.index.str.lower()

    df = df.reset_index().rename(columns={"index": "symbol"})

    df["volume_ratio"] = (df["usd_24h_vol"] / df["usd_market_cap"]).round(6)

    df["price_category"] = np.select(
        [
            df["usd"] > 50000,
            df["usd"] > 5000,
            df["usd"] > 1000,
            df["usd"] > 100
        ],
        ["very high", "high", "medium", "low"],
        default="very low"
    )

    df["time"] = datetime.now()

    df = df.rename(columns={
        "usd": "price_usd",
        "usd_market_cap": "market_cap",
        "usd_24h_vol": "hr_24_vol"
    })

    return df
