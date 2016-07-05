from isochrones.utils import addmags
from isochrones.dartmouth import Dartmouth_Isochrone
import pandas as pd
import numpy as np
import os

dar = Dartmouth_Isochrone()
M1 = 1.5
M2 = 0.5
M3 = 1.0
age = np.log10(5e8)
age3 = np.log10(5e9)
feh = 0.0
distance = 300
distance3 = 500
AV = 0.1

unresolved_bands = ['i','J','H','K','W1','W2']
resolved_bands = ['i','J','K']
args = (age, feh, distance, AV)
args3 = (age3, feh, distance3, AV)
unresolved = {b:addmags(dar.mag[b](M1, *args), dar.mag[b](M2, *args), dar.mag[b](M3, *args3)) for b in unresolved_bands}
resolved_1 = {b:dar.mag[b](M1, *args) for b in resolved_bands}
resolved_2 = {b:dar.mag[b](M2, *args) for b in resolved_bands}
resolved_3 = {b:dar.mag[b](M3, *args3) for b in resolved_bands}

print unresolved, resolved_1, resolved_2, resolved_3

instruments = ['twomass','WISE','SDSS','RAO']
bands = {'twomass':['J','H','K'],
          'WISE':['W1','W2'],
          'SDSS':['i'],
          'RAO':['i','J','K']}
mag_unc = {'twomass': 0.02, 'WISE':0.02, 'SDSS':0.02, 'RAO':0.1}
resolution = {'twomass':4.0, 'WISE':5.0, 'SDSS':4.5, 'RAO':0.1}
relative = {'twomass':False, 'WISE':False, 'SDSS':False, 'RAO':True}
separation2 = 0.5
separation3 = 1.2
PA2, PA3 = 100.,45.

columns = ['name', 'band', 'resolution', 'relative', 'separation', 'pa', 'mag', 'e_mag']
df = pd.DataFrame(columns=columns)
i=0
for inst in ['twomass', 'WISE','SDSS']:  #Unresolved observations
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
        mags = [resolved_1[b], resolved_2[b], resolved_3[b]]
        pas = [0, PA2, PA3]
        seps = [0., separation2, separation3]
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
df.to_cvs(path_or_buf='df.cvs')
