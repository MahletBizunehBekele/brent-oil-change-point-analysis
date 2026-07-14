import numpy as np


def compute_log_returns(df):
    """
    Calculate daily log returns.
    """

    df = df.copy()

    df["Log_Return"] = np.log(df["Price"]).diff()

    return df