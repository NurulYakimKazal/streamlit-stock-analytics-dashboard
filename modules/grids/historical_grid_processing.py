def prepare_historical_grid(df):
    display_df = df[
        ["date", "open", "high", "low", "close", "volume"]
    ].copy()

    cols = ["open", "high", "low", "close"]
    display_df[cols] = display_df[cols].round(2)

    display_df.rename(
        columns={
            "date": "Date",
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume",
        },
        inplace=True,
    )

    return display_df