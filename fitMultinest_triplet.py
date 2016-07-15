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

df = pd.read_csv('/tigress/np5/dataFrame/df_triplet_test{}.csv'.format(i))

#-------------------------------------------------------------------------------
#triplet0 - all in same system
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar)

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_triplet0'.format(i))

#if rank == 0:
f1 = open('/tigress/np5/evidence_triplet0.txt','a')
evi = mod.evidence
evi = str(evi)
f1.write('case{}: '.format(i) + evi + '\n')
f1.close()

fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
fig.savefig('/tigress/np5/figures/test{}_triplet0_corner_physical.png'.format(i))
plt.close(fig)
fig = mod.corner_observed()
fig.savefig('/tigress/np5/figures/test{}_triplet0_corner_observed.png'.format(i))
plt.close(fig)
#-------------------------------------------------------------------------------

#triplet1 - M1,M2 bound - M3 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,0,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_triplet1'.format(i))

#if rank == 0:
f1 = open('/tigress/np5/evidence_triplet1.txt','a')
evi = mod.evidence
evi = str(evi)
f1.write('case{}: '.format(i) + evi + '\n')
f1.close()

fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
fig.savefig('/tigress/np5/figures/test{}_triplet1_corner_physical.png'.format(i))
plt.close(fig)
fig = mod.corner_observed()
fig.savefig('/tigress/np5/figures/test{}_triplet1_corner_observed.png'.format(i))
plt.close(fig)
#-------------------------------------------------------------------------------

#triplet2 - M1,M3 bound - M2 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,0])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_triplet2'.format(i))

#if rank == 0:
f1 = open('/tigress/np5/evidence_triplet2.txt','a')
evi = mod.evidence
evi = str(evi)
f1.write('case{}: '.format(i) + evi + '\n')
f1.close()

fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
fig.savefig('/tigress/np5/figures/test{}_triplet2_corner_physical.png'.format(i))
plt.close(fig)
fig = mod.corner_observed()
fig.savefig('/tigress/np5/figures/test{}_triplet2_corner_observed.png'.format(i))
plt.close(fig)
#-------------------------------------------------------------------------------

#triplet3 - M2,M3 bound - M1 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_triplet3'.format(i))

#if rank == 0:
f1 = open('/tigress/np5/evidence_triplet3.txt','a')
evi = mod.evidence
evi = str(evi)
f1.write('case{}: '.format(i) + evi + '\n')
f1.close()

fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
fig.savefig('/tigress/np5/figures/test{}_triplet3_corner_physical.png'.format(i))
plt.close(fig)
fig = mod.corner_observed()
fig.savefig('/tigress/np5/figures/test{}_triplet3_corner_observed.png'.format(i))
plt.close(fig)
#-------------------------------------------------------------------------------

#triplet4 - M1,M2,M3 all unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,2])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_triplet4'.format(i))

#if rank == 0:
f1 = open('/tigress/np5/evidence_triplet4.txt','a')
evi = mod.evidence
evi = str(evi)
f1.write('case{}: '.format(i) + evi + '\n')
f1.close()

fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
fig.savefig('/tigress/np5/figures/test{}_triplet4_corner_physical.png'.format(i))
plt.close(fig)
fig = mod.corner_observed()
fig.savefig('/tigress/np5/figures/test{}_triplet4_corner_observed.png'.format(i))
plt.close(fig)
