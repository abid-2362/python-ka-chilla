import pandas as pd
import seaborn as sns

kashti = sns.load_dataset('titanic')

kashti.to_csv('../../data/kashti.csv')
