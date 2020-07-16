import pandas as pd
hsValues = pd.read_csv(r"C:\Users\John.Moore\Downloads\7_16issuance.csv.csv")
hsValues.rename(columns ={'Company Name':'Company_Name','Initial Payment Setup':'Initial_Payment_Setup'}, inplace = True)
yesList = hsValues[hsValues.Initial_Payment_Setup == 'Yes']
yesList.shape
print(yesList)
yesList.to_csv(r"C:\Users\John.Moore\Documents\pythonScripts\7_16practice.csv", index = False)
