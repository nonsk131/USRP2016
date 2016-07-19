import pandas as pd

df1 = pd.read_csv('/tigress/np5/all_df.csv')
df2 = pd.read_csv('/tigress/np5/all_df_params.csv')

df = pd.concat([df1,df2], axis=1)
df.to_csv(path_or_buf='/tigress/np5/all_df_final.csv')
