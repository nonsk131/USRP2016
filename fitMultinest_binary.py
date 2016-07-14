import matplotlib
matplotlib.use('Agg')
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from isochrones.observation import ObservationTree
import pandas as pd
import matplotlib.pyplot as plt
import sys
#from mpi4py import MPI

#comm = MPI.COMM_WORLD
#rank = comm.Get_rank()

def get_index(n):
    if n < 10:
        return '000' + str(n)
    elif n < 100:
        return '00' + str(n)
    elif n < 1000:
        return '0' + str(n)
    else:
        return str(n)

n = sys.argv[1]
i = get_index(n)

#same system case
df = pd.read_csv('/tigress/np5/df_binary_test{}.csv'.format(i))

dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar)

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_bound'.format(i))

#if rank == 0:
f1 = open('/tigress/np5/evidence_bound.txt','a')
evi = mod.evidence
evi = str(evi)
f1.write('case{}: '.format(i) + evi + '\n')
f1.close()

fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
fig.savefig('/tigress/np5/figures/test{}_bound_corner_physical.png'.format(i))
plt.close(fig)
fig = mod.corner_observed()
fig.savefig('/tigress/np5/figures/test{}_bound_corner_observed.png'.format(i))
plt.close(fig)

#unassociated case
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index = [0,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_unassociated'.format(i))

#if rank == 0:
f2 = open('/tigress/np5/evidence_unassociated.txt','a')
evi = mod.evidence
evi = str(evi)
f2.write('case{}: '.format(i) + evi + '\n')
f2.close()

fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
fig.savefig('/tigress/np5/figures/test{}_unasso_corner_physical.png'.format(i))
plt.close(fig)
fig = mod.corner_observed()
fig.savefig('/tigress/np5/figures/test{}_unasso_corner_observed.png'.format(i))
plt.close(fig)
