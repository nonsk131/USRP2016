import matplotlib
matplotlib.use('Agg')
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from isochrones.observation import ObservationTree
import pandas as pd
import matplotlib.pyplot as plt
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

for n in range(100,200,1):
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

    if rank == 0:
        f1 = open('evidence_bound.txt','w')
        evi = mod.evidence
        evi = str(evi)
        f1.write('case{}: '.format(i) + evi + '\n')

        #mod.corner(['mass_0_0','mass_0_1','distance_0','AV_0'])
        fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
        fig.savefig('test{}_bound_corner_physical.png'.format(i))
        plt.close(fig)
        fig = mod.corner_observed()
        fig.savefig('test{}_bound_corner_observed.png'.format(i))
        plt.close(fig)

    #unassociated case
    dar = Dartmouth_Isochrone()
    t = ObservationTree.from_df(df, name='test{}'.format(i))
    t.define_models(dar, index = [0,1])

    mod = StarModel(dar, obs=t)
    mod.fit_multinest(n_live_points=1000,
                        basename='test{}_unassociated'.format(i))

    if rank == 0:
        f2 = open('evidence_unassociated.txt','w')
        evi = mod.evidence
        evi = str(evi)
        f2.write('case{}: '.format(i) + evi + '\n')
        f2.close()

        #mod.corner(['mass_0_0','mass_0_1','distance_0','distance_1','AV_0','AV_1'])
        fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
        fig.savefig('test{}_unasso_corner_physical.png'.format(i))
        plt.close(fig)
        fig = mod.corner_observed()
        fig.savefig('test{}_unasso_corner_observed.png'.format(i))
        plt.close(fig)
