'''
Removes duplicate keywords from the csv file 'keyword clustered.csv' and saves it to 'keywords_clustered_clean.csv'
'''

import pandas as pd

inupt_csv = "keywords_clustered.csv"
output_csv = "keywords_clustered_clean.csv"
df = pd.read_csv(inupt_csv)


# Notes:
# - the `subset=Keword` means that keyword column is used 
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  
df.drop_duplicates(subset='Keyword', inplace=True)

df.to_csv(output_csv)