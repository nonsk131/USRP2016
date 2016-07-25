import pandas as pd
import os

file = open('/tigress/np5/true_params.txt','r')

index = ''
tracker = 'unbound'
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
for line in file:
    if line == '\n':
        continue
    elif 'test' in line:
        index = line.split(':')[1][1:-1]
        if index > '3999':
            tracker = 'unbound'
        elif index > '1999':
            tracker = 'triplet3'
            #for now we only want the data for binary systems
        elif index > '0999':
            tracker = 'bound'
        index = 'case' + index
    else:
        if tracker == 'unbound':
            line = line.split('=')[1]
            line = line.split(',')
            M1 = float(line[0][2:])
            M2 = float(line[1])
            age1 = float(line[2])
            age2 = float(line[3])
            feh1 = float(line[4])
            feh2 = float(line[5])
            distance1 = float(line[6])
            distance2 = float(line[7])
            AV1 = float(line[8])
            AV2 = float(line[9][:-1])
            df1 = df1.append(pd.DataFrame({'M1':M1,
                                    'M2':M2,
                                    'age1':age1,
                                    'age2':age2,
                                    'feh1':feh1,
                                    'feh2':feh2,
                                    'distance1':distance1,
                                    'distance2':distance2,
                                    'AV1':AV1,
                                    'AV2':AV2},index=[index]))
        elif tracker == 'bound':
            line = line.split('=')[1]
            line = line.split(',')
            M1 = float(line[0][2:])
            M2 = float(line[1])
            age1 = float(line[2])
            feh1 = float(line[3])
            distance1 = float(line[4])
            AV1 = float(line[5][:-1])
            df2 = df2.append(pd.DataFrame({'M1':M1,
                                    'M2':M2,
                                    'age1':age1,
                                    'age2':age1,
                                    'feh1':feh1,
                                    'feh2':feh1,
                                    'distance1':distance1,
                                    'distance2':distance1,
                                    'AV1':AV1,
                                    'AV2':AV1},index=[index]))
        else:
            pass
            # line = line.split('=')[1]
            # line = line.split(',')
            # M1 = float(line[0][2:])
            # M2 = float(line[1])
            # M3 = float(line[2])
            # age1 = float(line[3])
            # age2 = float(line[4])
            # distance1 = float(line[7])
            # distance2 = float(line[8])
            # df3 = df3.append(pd.DataFrame({'M1':M1,
            #                         'M2':M2,
            #                         'M3':M3,
            #                         'age1':age1,
            #                         'age2':age2,
            #                         'age3':age2,
            #                         'feh1':0.0,
            #                         'feh2':0.2,
            #                         'feh3':0.2,
            #                         'distance1':distance1,
            #                         'distance2':distance2,
            #                         'distance3':distance2,
            #                         'AV1':0.0,
            #                         'AV2':0.1,
            #                         'AV3':0.1},index=[index]))
file.close()
all_df = pd.concat([df1,df2,df3])
all_df = all_df.sort_index()
all_df.to_csv(path_or_buf='/tigress/np5/all_df_params.csv')
