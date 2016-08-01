import pandas as pd
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from isochrones.observation import ObservationTree
import numpy as np

df = pd.DataFrame()

i = 6000
df = pd.read_csv('/tigress/np5/dataFrame/df_binary_test{}.csv'.format(i))

dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))

t.define_models(dar, index=[0,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_unassociated'.format(i))

M1 = mod.samples.mass_0_0.median()
M2 = mod.samples.mass_1_0.median()
distance1 = mod.samples.distance_0.median()
distance2 = mod.samples.distance_1.median()

index = 'case'+str(i)
df = df.append({'M1':M1,
                'M2':M2,
                'distance1':distance1,
                'distance2':distance2},index=[index])

print df
