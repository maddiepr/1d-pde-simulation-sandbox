import os
import numpy as np

'''
Save an array to a .txt file
    Variables:
        U = size of first dimension of array
        V = size of second dimension of array
    Parameters:
        array: [U, V ]
            Array of any size that will be saved
        name_of_file: str
            Desired name of file
    Returns:
        None (just saves files)
'''

def save_values(array, name_of_file):
    
    # Define a folder to hold data current directory
    output_folder = os.path.join(os.path.dirname(__file__), "Post_simulation_data")
    
    # Save folder to current directory
    os.makedirs(output_folder, exist_ok=True)

    name = name_of_file + '.txt'

    # Save values of positions, t-values, counts, bin edges
    np.savetxt(os.path.join(output_folder, name), array, delimiter=',') 

    return None

