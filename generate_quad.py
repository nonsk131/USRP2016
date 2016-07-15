from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.utils import addmags
import numpy as np
import pandas as pd
from isochrones.observation import ObservationTree

#generate 4 stars all in different systems
#file = open('/tigress/np5/true_params.txt','a')

# def get_index(n):
#     if n < 10:
#         return '000' + str(n)
#     elif n < 100:
#         return '00' + str(n)
#     elif n < 1000:
#         return '0' + str(n)
#     else:
#         return str(n)
#
# def arrange_value(array):
#     if array[0] > array[1]:
#         if array[0] > array[2]:
#             return array[0], array[1], array[2]
#         else:
#             return array[2], array[0], array[1]
#     else:
#         if array[1] > array[2]:
#             return array[1], array[2], array[0]
#         else:
#             return array[2], array[0], array[1]


#for n in range(2000,2250,1):
#index = get_index(n)

#file.write('test: ' + index + '\n')

dar = Dartmouth_Isochrone()
M1, M2, M3, M4 = [1.0, 1.0, 1.0, 1.0]
distance1, distance2, distance3, distance4 = [400, 800, 1200, 1600]
AV = 0.0
feh = 0.0
age = np.log10(1e9)

# array = np.random.rand(3) + 0.5
# M1, M2, M3 = arrange_value(array)
#
# age1 = np.log10(5e8)
# age2 = np.log10(9e8)
# feh1 = 0.0
#
# array = 1400*np.random.rand(2) + 100
# if array[0] > array[1]:
#     distance1 = array[0]
#     distance2 = array[1]
# else:
#     distance1 = array[1]
#     distance2 = array[0]
#
# AV1 = 0.0
# feh2 = 0.2
# AV2 = 0.1
#
# params = (M1,M2,M3,age1,age2,feh1,feh2,distance1,distance2,AV1,AV2)
# params = str(params)
# file.write('(M1,M2,M3,age1,age2,feh1,feh2,distance1,distance2,AV1,AV2) = ' + params + '\n')
# file.write('\n')

#Simulate true magnitudes
unresolved_bands = ['J','H','K']
resolved_bands = ['i','K']
args1 = (age, feh, distance, AV)
unresolved = {b:addmags(dar.mag[b](M1, *args), dar.mag[b](M2, *args), dar.mag[b](M3, *args), dar.mag[b](M4, *args)) for b in unresolved_bands}
resolved_1 = {b:dar.mag[b](M1, *args) for b in resolved_bands}
resolved_2 = {b:dar.mag[b](M2, *args) for b in resolved_bands}
resolved_3 = {b:dar.mag[b](M3, *args) for b in resolved_bands}
resolved_4 = {b:dar.mag[b](M3, *args) for b in resolved_bands}

#print dar.mag['K'](M2, *args2)
#print unresolved, resolved_1, resolved_2

instruments = ['twomass','RAO']
bands = {'twomass':['J','H','K'],
          'RAO':['i','K']}
mag_unc = {'twomass': 0.02, 'RAO':0.1}
resolution = {'twomass':4.0, 'RAO':0.1}
relative = {'twomass':False, 'RAO':True}
separation2 = 0.5
separation3 = 1.1
separation4 = 0.8
PA2 = 100.
PA3 = 45.
PA4 = 235.

columns = ['name', 'band', 'resolution', 'relative', 'separation', 'pa', 'mag', 'e_mag']
df = pd.DataFrame(columns=columns)
i=0
for inst in ['twomass']:  #Unresolved observations
    for b in bands[inst]:
        row = {}
        row['name'] = inst
        row['band'] = b
        row['resolution'] = resolution[inst]
        row['relative'] = relative[inst]
        row['separation'] = 0.
        row['pa'] = 0.
        row['mag'] = unresolved[b]
        row['e_mag'] = mag_unc[inst]
        df = df.append(pd.DataFrame(row, index=[i]))
        i += 1

for inst in ['RAO']:  #Resolved observations
    for b in bands[inst]:
        mags = [resolved_1[b], resolved_2[b], resolved_3[b], resolved_4[b]]
        pas = [0, PA2, PA3, PA4]
        seps = [0., separation2, separation3, separation4]
        for mag,sep,pa in zip(mags,seps,pas):
            row = {}
            row['name'] = inst
            row['band'] = b
            row['resolution'] = resolution[inst]
            row['relative'] = relative[inst]
            row['separation'] = sep
            row['pa'] = pa
            row['mag'] = mag
            row['e_mag'] = mag_unc[inst]
            df = df.append(pd.DataFrame(row, index=[i]))
            i += 1

#print df
df.to_csv(path_or_buf='/tigress/np5/dataFrame/df_quad_test3000.csv')

t = ObservationTree.from_df(df, name='test-quad')
t.define_models(dar)
t.print_ascii()

#file.close()
