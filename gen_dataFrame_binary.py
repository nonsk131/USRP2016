from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.utils import addmags
import numpy as np
import pandas as pd

dar = Dartmouth_Isochrone()

M1 = 1.
M2 = 0.7
age = np.log10(5e9)
feh = 0.0
distance = 200
AV = 0.1
distance2 = 400
feh2 = 0.5
age2 = np.log10(5e8)
AV2 = 0.2

#Simulate true magnitudes
unresolved_bands = ['J','H','K','W1','W2']
resolved_bands = ['i']
args = (age, feh, distance, AV)
args2 = (age2, feh2, distance2, AV2)
unresolved = {b:addmags(dar.mag[b](M1, *args), dar.mag[b](M2, *args2)) for b in unresolved_bands}
resolved_1 = {b:dar.mag['i'](M1, *args) for b in resolved_bands}
resolved_2 = {b:dar.mag['i'](M2, *args2) for b in resolved_bands}

print unresolved, resolved_1, resolved_2

instruments = ['twomass','WISE','RAO']
bands = {'twomass':['J','H','K'],
          'WISE':['W1','W2'],
          'RAO':['i']}
mag_unc = {'twomass': 0.02, 'WISE':0.02, 'RAO':0.1}
resolution = {'twomass':4.0, 'WISE':5.0, 'RAO':0.1}
relative = {'twomass':False, 'WISE':False, 'RAO':True}
separation = 0.5
PA = 100.

columns = ['name', 'band', 'resolution', 'relative', 'separation', 'pa', 'mag', 'e_mag']
df = pd.DataFrame(columns=columns)
i=0
for inst in ['twomass', 'WISE']:  #Unresolved observations
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

print df
df.to_csv(path_or_buf='df_binary.csv')
