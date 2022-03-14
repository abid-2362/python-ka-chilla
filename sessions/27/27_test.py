# Learning Pandas With Dr. Ammar Tufail
# import libraries
import numpy as np
import pandas as pd

# Object Creation
sample_series = pd.Series([1, 3, np.nan, 5, 7, 8, 9])
# sample_series
# Creating date range by pandas
dates = pd.date_range("20220101", periods=20)
# dates
# Create a 2 dimensional array by using numpy random.randn function
random_array = np.random.randn(20, 4)
# random_array
# Creating DataFrame
# sample_data_frame = pd.DataFrame(random_array, index=dates, columns="abcd")
# TypeError: Index(...) must be called with a collection of some kind, 'abcd' was passed

sample_data_frame = pd.DataFrame(random_array, index=dates, columns=list("ABCD"))
# sample_data_frame
# Creating Data Frame using pandas
data_frame2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(3, index=list(range(5)), dtype=np.float32),
        "D": np.array([3] * 5, dtype="int32"),
        "E": pd.Categorical(["girl", "woman", "girl", "woman", "girl"]),
        "F": "females"
    }
)

# data_frame2
# data_frame2.dtypes
data_frame2.head()
data_frame2.tail(2)
# Creating Data Frame using pandas
data_frame3 = pd.DataFrame(
    {
        "A": 1.0,
        "B": dates[:5],
        "C": pd.Series(3, index=list(range(5)), dtype=np.float32),
        "D": np.array([3] * 5, dtype="int32"),
        "E": pd.Categorical(["girl", "woman", "girl", "woman", "girl"]),
        "F": "females"
    }
)

# data_frame3
data_frame3.head(2)
data_frame3.tail(2)
# sample_data_frame.index
# data_frame3.index
sample_data_frame.to_numpy()
# sample_data_frame
data_frame3.to_numpy()
sample_data_frame.describe()
# Pandas DataFrame: transpose(); T is not callable
t = sample_data_frame.T
# t
# sample_data_frame.sort_index(axis=0, ascending=False)
# sample_data_frame.sort_values(by="D", ascending=True)

sample_data_frame[0:4].sort_index(axis=1, ascending=True)

# data selection by row
# sample_data_frame[0:2]
# dates
# sample_data_frame.loc[dates[0]]
