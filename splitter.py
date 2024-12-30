import pandas as pd 

file_path = 'US_Accidents.csv'

data = pd.read_csv(file_path)
data.head() 



num_parts = 9

part_size = len(data) // num_parts



for part in range(num_parts):
    start_index = part * part_size
    end_index = (part + 1) * part_size if (part + 1) != num_parts else len(data)
    
    data_subset = data.iloc[start_index:end_index]
    
    data_subset.to_csv(f'US_Accidents_Part{part+1}.csv', index=False)