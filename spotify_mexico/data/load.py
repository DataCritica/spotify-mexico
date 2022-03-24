import pandas as pd
import spotify_mexico.utils.paths as path

""" 
Function to read csv files as dataframes

file: file's name
return: dataframe
"""
def load_file(file=None):
    df = pd.read_csv(file)
    return df

"""
Function to convert columns into a list

df: dataframe
return: list of columns names
"""
def load_columns(df):
    cols = df.columns
    return cols

# Inputs
data_raw = path.data_raw_dir()
data_spotify = path.data_processed_dir('spotify_mexico.csv')

# Outputs
data_processed = path.data_processed_dir()
tables =  path.outputs_tables_dir()
figures = path.outputs_figures_dir()