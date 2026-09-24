import pandas as pd
input_data = pd.read_csv('/workspaces/DataEngineer/healthcare_dataset.csv')
print(input_data[1:10])
print(input_data.columns)
