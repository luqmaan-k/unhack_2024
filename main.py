import pandas as pd

def is_in(id,x1,x2,y1,y2,carefield):
    for i in range(0,len(x1)):
        if (carefield["X2"] <= x2[i] ) and (carefield["Y2"] <= y2[i]):
            return True,id[i]
    return False,None

def generate_sub_fields(sf_id,sf_x1,sf_x2,sf_y1,sf_y2,mfid,subfields_size,sf_id_index,mainfield_id,carefield):
    tempx1 = carefield["X1"]
    tempy1 = carefield["Y1"]
    while(True):
        if tempx1 > carefield["X2"]:
            tempx1 = carefield["X1"]
            tempy1 += subfields_size
        if tempy1 > carefield["Y2"]:
            break
        sf_x1.append(tempx1)
        sf_x2.append(tempx1 + subfields_size)
        sf_y1.append(tempy1)
        sf_y2.append(tempy1+subfields_size)
        tempx1 += subfields_size
        # update id for subfields
        sf_id.append(sf_id_index)
        mfid.append(mainfield_id)
        sf_id_index += 1

def generate_main_fields(careareas,metadata):

    mainfields_size = metadata.iloc[0,0]
    subfields_size = metadata.iloc[0,1]
    id = []
    x1 = []
    x2 = []
    y1 = []
    y2 = []

    sf_id = []
    sf_x1 = []
    sf_x2 = []
    sf_y1 = []
    sf_y2 = []
    mfid = []

    id_index = 0
    sf_id_index = 0
    for index,row in careareas.iterrows():        
        isin , mainfield_id= is_in(id,x1,x2,y1,y2,row)
        #if row not in mainfield area generate a mainfield
        if not isin:
            x1.append(row["X1"])
            x2.append(row["X1"] + mainfields_size)
            y1.append(row["Y1"])
            y2.append(row["Y1"] + mainfields_size)
            # update id for mainfields
            id.append(id_index)
            mainfield_id = id_index
            id_index += 1
        # generate subfields for it
        generate_sub_fields(sf_id,sf_x1,sf_x2,sf_y1,sf_y2,mfid,subfields_size,sf_id_index,mainfield_id,row)    

    mainfields = pd.DataFrame({
        'ID' :id,
        'X1' :x1,
        'X2' :x2,
        'Y1' :y1,
        'Y2' :y2,
    })
    
    subfields = pd.DataFrame({
            # 'ID' :sf_id,
            'X1' :sf_x1,
            'X2' :sf_x2,
            'Y1' :sf_y1,
            'Y2' :sf_y2,
            'MF ID':mfid,
    })

    subfields.sort_values("MF ID")
    return mainfields,subfields

# def generate_sub_fields(careareas,metadata,mainfields):

#     subfields_size = metadata.iloc[0,1]

#     id = []
#     x1 = []
#     x2 = []
#     y1 = []
#     y2 = []
#     mfid = []
    
#     id_index=0
#     mfid_index=0
#     for index,row in careareas.iterrows():        
#         x1.append(row["X1"])
#         x2.append(row["X1"] + subfields_size)
#         y1.append(row["Y1"])
#         y2.append(row["Y1"] + subfields_size)
    
#         # update id for mainfields
#         id.append(id_index)
#         mfid.append(mfid_index)
#         id_index += 1
#         mfid_index += 1

#     subfields = pd.DataFrame({
#         'ID' :id,
#         'X1' :x1,
#         'X2' :x2,
#         'Y1' :y1,
#         'Y2' :y2,
#         'MF ID':mfid,
#     })
    
#     return subfields

def milestone_1():
    careareas = pd.read_csv("data/Dataset-0/Dataset-0/1st/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Dataset-0/Dataset-0/1st/metadata.csv")

    mainfields , subfields= generate_main_fields(careareas,metadata)
    # subfields = generate_sub_fields(careareas,metadata,mainfields)

    careareas.to_csv("result/Milestone1/CareAreas.csv",header=False,index=False)
    mainfields.to_csv("result/Milestone1/mainfields.csv",header=False,index=False)
    metadata.to_csv("result/Milestone1/metadata.csv",index= False)
    subfields.to_csv("result/Milestone1/subfields.csv",header=False,index=True)

def milestone_2():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/2nd/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/2nd/metadata.csv")

    mainfields , subfields= generate_main_fields(careareas,metadata)
    # subfields = generate_sub_fields(careareas,metadata,mainfields)

    careareas.to_csv("result/Milestone2/CareAreas.csv",header=False,index=False)
    mainfields.to_csv("result/Milestone2/mainfields.csv",header=False,index=False)
    metadata.to_csv("result/Milestone2/metadata.csv",index= False)
    subfields.to_csv("result/Milestone2/subfields.csv",header=False,index=True)

def milestone_3():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/3rd/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/3rd/metadata.csv")

    mainfields , subfields= generate_main_fields(careareas,metadata)
    # subfields = generate_sub_fields(careareas,metadata,mainfields)

    careareas.to_csv("result/Milestone3/CareAreas.csv",header=False,index=False)
    mainfields.to_csv("result/Milestone3/mainfields.csv",header=False,index=False)
    metadata.to_csv("result/Milestone3/metadata.csv",index= False)
    subfields.to_csv("result/Milestone3/subfields.csv",header=False,index=True)

def milestone_4():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/4th/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/4th/metadata.csv")

    mainfields , subfields= generate_main_fields(careareas,metadata)
    # subfields = generate_sub_fields(careareas,metadata,mainfields)

    careareas.to_csv("result/Milestone4/CareAreas.csv",header=False,index=False)
    mainfields.to_csv("result/Milestone4/mainfields.csv",header=False,index=False)
    metadata.to_csv("result/Milestone4/metadata.csv",index= False)
    subfields.to_csv("result/Milestone4/subfields.csv",header=False,index=True)

def milestone_5():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/5th/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/5th/metadata.csv")

    mainfields , subfields= generate_main_fields(careareas,metadata)
    # subfields = generate_sub_fields(careareas,metadata,mainfields)

    careareas.to_csv("result/Milestone5/CareAreas.csv",header=False,index=False)
    mainfields.to_csv("result/Milestone5/mainfields.csv",header=False,index=False)
    metadata.to_csv("result/Milestone5/metadata.csv",index= False)
    subfields.to_csv("result/Milestone5/subfields.csv",header=False,index=True)

def milestone_6():
    careareas = pd.read_csv("data/Student-Dataset-1/Dataset-1/6th/CareAreas.csv",names=["ID","X1","X2","Y1","Y2"])
    metadata = pd.read_csv("data/Student-Dataset-1/Dataset-1/6th/metadata.csv")

    mainfields , subfields= generate_main_fields(careareas,metadata)
    # subfields = generate_sub_fields(careareas,metadata,mainfields)

    careareas.to_csv("result/Milestone6/CareAreas.csv",header=False,index=False)
    mainfields.to_csv("result/Milestone6/mainfields.csv",header=False,index=False)
    metadata.to_csv("result/Milestone6/metadata.csv",index= False)
    subfields.to_csv("result/Milestone6/subfields.csv",header=False,index=True)


milestone_1()
milestone_2()
milestone_3()
milestone_4()
milestone_5()
milestone_6()