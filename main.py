import pandas as pd

def generate_main_fields(careareas,metadata):
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
    
    return mainfields
# careareas.to_csv("result/careareas.csv",index=False)
def generate_sub_fields(careareas,metadata):
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
    
    return subfields

def milestone_1():
    careareas = pd.read_csv("data/Dataset-0/Dataset-0/1st/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Dataset-0/Dataset-0/1st/metadata.csv")

    mainfields = generate_main_fields(careareas,metadata)
    subfields = generate_sub_fields(careareas,metadata)

    careareas.to_csv("result/milestone_1/careareas.csv",header=False,index=False)
    mainfields.to_csv("result/milestone_1/mainfields.csv",header=False,index=False)
    subfields.to_csv("result/milestone_1/subfields.csv",header=False,index=False)

def milestone_2():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/2nd/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/2nd/metadata.csv")

    mainfields = generate_main_fields(careareas,metadata)
    subfields = generate_sub_fields(careareas,metadata)

    careareas.to_csv("result/milestone_2/careareas.csv",header=False,index=False)
    mainfields.to_csv("result/milestone_2/mainfields.csv",header=False,index=False)
    subfields.to_csv("result/milestone_2/subfields.csv",header=False,index=False)

def milestone_3():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/3rd/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/3rd/metadata.csv")

    mainfields = generate_main_fields(careareas,metadata)
    subfields = generate_sub_fields(careareas,metadata)

    careareas.to_csv("result/milestone_3/careareas.csv",header=False,index=False)
    mainfields.to_csv("result/milestone_3/mainfields.csv",header=False,index=False)
    subfields.to_csv("result/milestone_3/subfields.csv",header=False,index=False)

def milestone_4():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/4th/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/4th/metadata.csv")

    mainfields = generate_main_fields(careareas,metadata)
    subfields = generate_sub_fields(careareas,metadata)

    careareas.to_csv("result/milestone_4/careareas.csv",header=False,index=False)
    mainfields.to_csv("result/milestone_4/mainfields.csv",header=False,index=False)
    subfields.to_csv("result/milestone_4/subfields.csv",header=False,index=False)

def milestone_5():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/5th/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/5th/metadata.csv")

    mainfields = generate_main_fields(careareas,metadata)
    subfields = generate_sub_fields(careareas,metadata)

    careareas.to_csv("result/milestone_5/careareas.csv",header=False,index=False)
    mainfields.to_csv("result/milestone_5/mainfields.csv",header=False,index=False)
    subfields.to_csv("result/milestone_5/subfields.csv",header=False,index=False)

def milestone_6():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/6th/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/6th/metadata.csv")

    mainfields = generate_main_fields(careareas,metadata)
    subfields = generate_sub_fields(careareas,metadata)

    careareas.to_csv("result/milestone_6/careareas.csv",header=False,index=False)
    mainfields.to_csv("result/milestone_6/mainfields.csv",header=False,index=False)
    subfields.to_csv("result/milestone_6/subfields.csv",header=False,index=False)


milestone_1()
milestone_2()
milestone_3()
milestone_4()
milestone_5()
milestone_6()