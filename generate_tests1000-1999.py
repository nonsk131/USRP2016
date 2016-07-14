from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.utils import addmags
import numpy as np
import pandas as pd

#generate synthetic binaries that are in the same system
file = open('/tigress/np5/true_params.txt','a')

def get_index(n):
    if n < 10:
        return '000' + str(n)
    elif n < 100:
        return '00' + str(n)
    elif n < 1000:
        return '0' + str(n)
    else:
        return str(n)

for n in range(1000,2000,1):
    index = get_index(n)

    file.write('test: ' + index + '\n')

    dar = Dartmouth_Isochrone()

    array = np.random.rand(2) + 0.5
    if array[0] > array[1]:
        M1 = array[0]
        M2 = array[1]
    else:
        M1 = array[1]
        M2 = array[0]

    age = np.log10(7e8)
    feh = 0.0
    distance = 1400*np.random.rand() + 100
    AV = 0.0

    params = (M1,M2,age,feh,distance,AV)
    params = str(params)
    file.write('(M1,M2,age,feh,distance,AV) = ' + params + '\n')
    file.write('\n')

    #Simulate true magnitudes
    unresolved_bands = ['J','H','K']
    resolved_bands = ['i','K']
    args = (age, feh, distance, AV)
    unresolved = {b:addmags(dar.mag[b](M1, *args), dar.mag[b](M2, *args)) for b in unresolved_bands}
    resolved_1 = {b:dar.mag[b](M1, *args) for b in resolved_bands}
    resolved_2 = {b:dar.mag[b](M2, *args) for b in resolved_bands}

    #print dar.mag['K'](M2, *args2)
    #print unresolved, resolved_1, resolved_2

    instruments = ['twomass','RAO']
    bands = {'twomass':['J','H','K'],
              'RAO':['i','K']}
    mag_unc = {'twomass': 0.02, 'RAO':0.1}
    resolution = {'twomass':4.0, 'RAO':0.1}
    relative = {'twomass':False, 'RAO':True}
    separation = 0.5
    PA = 100.

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
            mags = [resolved_1[b], resolved_2[b]]
            pas = [0, PA]
            seps = [0., separation]
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
    df.to_csv(path_or_buf='/tigress/np5/dataFrame/df_binary_test{}.csv'.format(index))

file.close()
