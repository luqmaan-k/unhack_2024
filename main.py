import pandas as pd

def generate_main_fields(careareas,metadata):

    mainfields_size = metadata.iloc[0,0]
    
    id = []
    x1 = []
    x2 = []
    y1 = []
    y2 = []

    id_index=0
    for index,row in careareas.iterrows():        
        x1.append(row["X1"])
        x2.append(row["X1"] + mainfields_size)
        y1.append(row["Y1"])
        y2.append(row["Y1"] + mainfields_size)
    
        # update id for mainfields
        id.append(id_index)
        id_index += 1

    mainfields = pd.DataFrame({
        'ID' :id,
        'X1' :x1,
        'X2' :x2,
        'Y1' :y1,
        'Y2' :y2,
    })
    
    return mainfields

def generate_sub_fields(careareas,metadata):

    subfields_size = metadata.iloc[0,1]

    id = []
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    mfid = []
    
    id_index=0
    mfid_index=0
    for index,row in careareas.iterrows():        
        x1.append(row["X1"])
        x2.append(row["X1"] + subfields_size)
        y1.append(row["Y1"])
        y2.append(row["Y1"] + subfields_size)
    
        # update id for mainfields
        id.append(id_index)
        mfid.append(mfid_index)
        id_index += 1
        mfid_index += 1



    subfields = pd.DataFrame({
        'ID' :id,
        'X1' :x1,
        'X2' :x2,
        'Y1' :y1,
        'Y2' :y2,
        'MF ID':mfid,
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


# milestone_1()
milestone_2()
# milestone_3()
# milestone_4()
# milestone_5()
# milestone_6()