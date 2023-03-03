from django.test import TestCase

# Create your tests here.
import pandas as pd

# Load Excel file into a pandas dataframe
df = pd.read_excel("/content/Demo.xlsx")

# Define the column to search in and the string to search for
search_column = "Utterance"
search_string = ["outlook" ,"okta" , "zoom"]


# df = df.applymap(lambda s: s.lower() if type(s) == str else s)

for ss in search_string :
      print(ss)
# Search for the string in the specified column and create a boolean mask
      mask = df[search_column].str.contains(ss)

# Add a response to a specific column based on the boolean mask
      df.loc[mask, "Related to"] = "Found"
      # df.loc[~mask, "Related to"] = "Not Found"

# Save the updated dataframe back to the Excel file
df.to_excel("/content/Demo.xlsx", index=False)
