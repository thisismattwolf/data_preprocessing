# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:51:47 2018

@author: Matthew Wolf

Takes a CSV file with a column of text values on which you want to normalize.
The column in question should contain a string of values delimited by a consistent
    character, such as , or ;. 

LIBRARIES
pandas

KEY INPUTS          -dtype    -description
file_name           -(STRING) -string of the file location of the input csv file
destination_file    -(STRING) -string of the file location of the output csv file
norm_column         -(STRING) -the string name of the column to be normalized
                    -         -   MUST match the column name exactly!
delimit             -(STRING) -the character or string that delimits the different 
                    -         -   values in each cell of norm_column

OUTPUT
norm                -(DATAFRAME) -A dataframe with the original data, database-normalized
                                 -  on the values in norm_column, with all other values
                                 -  the same

"""

def normalizeOnColumn(file_name , destination_file, norm_column, delimit):    
    
    import pandas
    
    # read in data, stored as CSV
    Meltwater_data = pandas.read_csv(file_name)
    
    # We only want the relevant rows
    df = Meltwater_data[Meltwater_data.Classifier == 'Relevant']
    
    # Create new column with a list of strings rather than a string list
    df['temp'] = df[norm_column].str.split(delimit)
    
    # Delete old string column, replace it with the new one
    del df[norm_column]
    df.rename(columns = {'temp': norm_column}, inplace = True)
    
    # Create new DataFrame for the normalized data with the same column headers
    norm = pandas.DataFrame(columns = df.columns)
    
    # Rows with value in norm_column can be added to the norm file directly
    blankRows = df[df[norm_column].isnull()]
    norm = pandas.concat([norm,blankRows])
    
    # Rows with locations need to be normalized - one row per location
    otherRows = df[df[norm_column].notnull()]
    
    # Iterate through these rows
    for index, row in otherRows.iterrows():
        # For each row, check the list of locations
        # for every location in the list of locations...
        for item in row[norm_column]:
                # 1. create a copy of the row
                new_row = row
                # 2. Replace the list of locations with one of the locations
                new_row[norm_column] = item
                # 3. Append this row to the normalized file
                norm = norm.append(new_row)
    
    return norm


