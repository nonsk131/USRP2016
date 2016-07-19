import pandas as pd

df1 = pd.read_csv('/tigress/np5/all_df.csv')
df2 = pd.read_csv('/tigress/np5/all_df_params.csv')

df = pd.merge(df1, df2, left_index=True, right_index=True, how='inner')
df.to_csv(path_or_buf='/tigress/np5/all_df_final.csv')
