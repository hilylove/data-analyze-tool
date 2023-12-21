import pandas as pd

data = pd.read_csv('parts.csv', encoding='latin1')

result = data.groupby(['model_name', 'part_name']).agg({'quantity': 'sum'}).reset_index()

result.to_csv('result.csv', index=False)