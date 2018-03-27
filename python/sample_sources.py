import pandas as pd

df = pd.read_csv('./updated_sources.csv')

left = df.loc[df['side'] == 'left']
right = df.loc[df['side'] == 'right']

left_srs = left.sample(30)
right_srs = right.sample(30)

left_srs.to_csv('sampled_sources_left.csv')
right_srs.to_csv('sampled_sources_right.csv')
