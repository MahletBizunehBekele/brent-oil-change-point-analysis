import pandas as pd


def load_data(filepath):
    """
    Load Brent oil price dataset.
    """

    try:
        df = pd.read_csv(filepath)

        df["Date"] = pd.to_datetime(
            df["Date"],
            format="mixed"
        )

        df = df.sort_values("Date")

        return df

    except Exception as e:
        raise Exception(f"Error loading dataset: {e}")