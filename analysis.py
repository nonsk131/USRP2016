import pandas as pd
import os

filePath = '/tigress/np5/'

binary = ['evidence_bound.txt','evidence_unassociated.txt']
triplet = ['evidence_triplet0.txt','evidence_triplet1.txt',
            'evidence_triplet2.txt','evidence_triplet3.txt',
            'evidence_triplet4.txt']
quad = ['evidence_quad0.txt','evidence_quad1.txt','evidence_quad2.txt',
        'evidence_quad3.txt','evidence_quad4.txt','evidence_quad5.txt',
        'evidence_quad6.txt','evidence_quad7.txt','evidence_quad8.txt',
        'evidence_quad9.txt','evidence_quad10.txt','evidence_quad11.txt',
        'evidence_quad12.txt','evidence_quad13.txt','evidence_quad14.txt']

data = [binary, triplet, quad]

def get_columnName(name):
    if 'triple' in name:
        return name[:17]
    elif 'quad' in name:
        return name[:-4]
    else:
        name = name.split('.')
        return name[0]

df_final = pd.DataFrame()
for element in data:
    df = pd.DataFrame()
    for name in element:
        indexList = []
        valueList = []
        c = get_columnName(name)
        fileName = os.path.join(filePath, name)
        file = open(fileName, 'r')
        for line in file:
            line = line.split(':')
            indexList.append(line[0])
            line = line[1].split(',')
            valueList.append(float(line[0][2:]))
        file.close()
        series = pd.Series(valueList, index=indexList, name=c)
        df = pd.concat([df,series], axis=1)
    df_final = df_final.append(df)

df_final = df_final.sort_index()
df_final.to_csv(path_or_buf='/tigress/np5/all_df.csv')
