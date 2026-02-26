import pandas as pd
import os


# create a sample dataframe with column names
data = {'Name': ['vishank' , 'rahul' , 'banti'] ,
        'Age' : [20,21,18],
        'city': ['jamshedpur' , 'bokaro','ranchi'] 
        }

df = pd.DataFrame(data)

# Ensure the "data" directory exists at root level
data_dir = 'data'
os.makedirs(data_dir , exist_ok= True) # True means if their is already a data that is with the same name then use that only , do not overwrite or replace it 

# define the file path 
file_path = os.path.join(data_dir , 'sample_data.csv')

# save the dataframe to a csv file including teh columns names
df.to_csv(file_path , index= False)

print(f'csv file saved to {file_path}')