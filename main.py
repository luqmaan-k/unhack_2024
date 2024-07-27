import pandas as pd

careareas = pd.read_csv("data/Dataset-0/Dataset-0/1st/CareAreas.csv",header = None)
metadata = pd.read_csv("data/Dataset-0/Dataset-0/1st/metadata.csv",header= None)

def generate_main_fields():
    
    #testing

    minaxes = careareas.min()
    maxaxes = careareas.max()
    mainfields = pd.DataFrame({
        'ID' :[0],
        'X1' :[minaxes.iloc[1]],
        'X2' :[maxaxes.iloc[2]],
        'Y1' :[minaxes.iloc[3]],
        'Y2' :[maxaxes.iloc[4]],
    })
    print(mainfields)

    #code to csv

    mainfields.to_csv("result/mainfield.csv",header=False,index=False)
# careareas.to_csv("result/careareas.csv",index=False)
def generate_sub_fields():

    #testing
    minaxes = careareas.min()
    maxaxes = careareas.max()
    subfields = pd.DataFrame({
        'ID' :[0],
        'X1' :[minaxes.iloc[1]],
        'X2' :[maxaxes.iloc[2]-50],
        'Y1' :[minaxes.iloc[3]],
        'Y2' :[maxaxes.iloc[4]-50],
        'MF ID':[0],
    })
    print(subfields)
    
    #code to write to csv

    subfields.to_csv("result/subfield.csv",header=False,index=False)

generate_main_fields()
generate_sub_fields()