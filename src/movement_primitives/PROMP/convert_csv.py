import pandas as pd
import ast

# Function to parse the tuple string and convert it to a list of floats
def parse_to_floats(tuple_str):
    # Parsing the string as a tuple
    tuple_val = ast.literal_eval(tuple_str)
    # Keeping each element in the tuple as float
    return [float(val) for val in tuple_val]

# Reading the CSV file without assuming a header
file_path = 'lfd_traj.csv'
data = pd.read_csv(file_path, header=None)

# Applying the function to each row in the DataFrame and creating a list of lists
converted_data_list = data.iloc[:, 0].apply(parse_to_floats).tolist()

# Creating a new DataFrame from the list of lists
converted_df = pd.DataFrame(converted_data_list)

# Saving the new DataFrame as a CSV file
output_file_path = 'converted_lfd_traj.csv'
converted_df.to_csv(output_file_path, index=False)

print(f"Converted data saved to {output_file_path}")
