from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from isochrones.observation import ObservationTree
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

f1 = open('evidence_bound.txt','w')
f2 = open('evidence_unassociated.txt','w')

for n in range(0,2,1):
    if n < 10:
        i = '0' + str(n)
    else:
        i = str(n)

    #same system case
    df = pd.read_csv('df_binary_test{}.csv'.format(i))

    dar = Dartmouth_Isochrone()
    t = ObservationTree.from_df(df, name='test{}'.format(i))
    t.define_models(dar)

    mod = StarModel(dar, obs=t)
    mod.fit_multinest(n_live_points=1000,
                        basename='test{}_bound'.format(i))
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')

    #mod.corner(['mass_0_0','mass_0_1','distance_0','AV_0'])
    mod.corner_physical(props=['mass', 'distance', 'AV'])
    mod.corner_observed()

    #unassociated case
    dar = Dartmouth_Isochrone()
    t = ObservationTree.from_df(df, name='test{}'.format(i))
    t.define_models(dar, index = [0,1])

    mod = StarModel(dar, obs=t)
    mod.fit_multinest(n_live_points=1000,
                        basename='test{}_unassociated'.format(i))
    evi = mod.evidence
    evi = str(evi)
    f2.write('case{}: '.format(i) + evi + '\n')

    #mod.corner(['mass_0_0','mass_0_1','distance_0','distance_1','AV_0','AV_1'])
    mod.corner_physical(props=['mass', 'distance', 'AV'])
    mod.corner_observed()

f1.close()
f2.close()
