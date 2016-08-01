import pandas as pd
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from isochrones.observation import ObservationTree
import numpy as np

i = 6000
df = pd.read_csv('/tigress/np5/dataFrame/df_binary_test{}.csv'.format(i))

dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))

t.define_models(dar, index=[0,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_bound'.format(i))

print mod.samples.mass_0_0.median()
