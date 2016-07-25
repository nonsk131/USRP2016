from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.utils import addmags
import numpy as np
import pandas as pd

file = open('/tigress/np5/true_params.txt','a')


for n in range(6000,7000,1):
    index = str(n)

    file.write('test: ' + index + '\n')

    dar = Dartmouth_Isochrone()

    array = np.random.rand(2) + 0.5
    if array[0] > array[1]:
        M1 = array[1]
        M2 = array[0]
    else:
        M1 = array[0]
        M2 = array[1]

    feh1,feh2 = 0.7*np.random.rand(2) - 0.5

    random1, random2 = np.random.rand(2)
    age_low, age_high = dar.agerange(M1,feh1)
    age_low = max(age_low, dar.minage)
    age_high = min(age_high, dar.maxage)
    age_low = 10**age_low
    age_high = 10**age_high
    age1 = random1*(age_high - age_low) + age_low
    age1 = np.log10(age1)

    age_low, age_high = dar.agerange(M2,feh2)
    age_low = max(age_low, dar.minage)
    age_high = min(age_high, dar.maxage)
    age_low = 10**age_low
    age_high = 10**age_high
    age2 = random2*(age_high - age_low) + age_low
    age2 = np.log10(age2)

    array = 1400*np.random.rand(2) + 100
    if array[0] > array[1]:
        distance1 = array[1]
        distance2 = array[0]
    else:
        distance1 = array[0]
        distance2 = array[1]

    AV1, AV2 = 0.5*np.random.rand(2)+0.5
    AV1 = AV1 * distance1/1000.0
    AV2 = AV2 * distance2/1000.0

    params = (M1,M2,age1,age2,feh1,feh2,distance1,distance2,AV1,AV2)

    #Simulate true magnitudes
    unresolved_bands = ['J','H','K']
    resolved_bands = ['i','K']
    args1 = (age1, feh1, distance1, AV1)
    args2 = (age2, feh2, distance2, AV2)
    unresolved = {b:addmags(dar.mag[b](M1, *args1), dar.mag[b](M2, *args2)) for b in unresolved_bands}
    resolved_1 = {b:dar.mag[b](M1, *args1) for b in resolved_bands}
    resolved_2 = {b:dar.mag[b](M2, *args2) for b in resolved_bands}

    params = str(params)
    file.write('(M1,M2,age1,age2,feh1,feh2,distance1,distance2,AV1,AV2) = ' + params + '\n')
    file.write('\n')

    #print dar.mag['K'](M2, *args2)
    #print unresolved, resolved_1, resolved_2

    instruments = ['twomass','RAO']
    bands = {'twomass':['J','H','K'],
              'RAO':['i','K']}
    mag_unc = {'twomass': 0.02, 'RAO':0.04}
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
