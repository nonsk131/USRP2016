import matplotlib
matplotlib.use('Agg')
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from isochrones.observation import ObservationTree
import pandas as pd
import matplotlib.pyplot as plt
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

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

df = pd.read_csv('/tigress/np5/dataFrame/df_quad_test{}.csv'.format(i))

#-------------------------------------------------------------------------------
#quad0 - all in same system
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar)

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad0'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad0.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad0_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad0_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad1 - M1,M2,M3 bound - M4 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,0,0,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad1'.format(i))

if rank == 0:
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

#quad2 - M1,M2,M4 bound - M3 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,0,1,0])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad2'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad2.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad2_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad2_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad3 - M1,M3,M4 bound - M2 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,0,0])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad3'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad3.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad3_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad3_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad4 - M2,M3,M4 bound - M1 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,1,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad4'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad4.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad4_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad4_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad5 - M1,M2 bound - M3,M4 bound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,0,1,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad5'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad5.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad5_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad5_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad6 - M1,M2 bound - M3 unbound - M4 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,0,1,2])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad6'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad6.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad6_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad6_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad7 - M1,M3 bound - M2,M4 bound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,0,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad7'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad7.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad7_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad7_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad8 - M1,M3 bound - M2 unbound - M4 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,0,2])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad8'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad8.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad8_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad8_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad9 - M1,M4 bound - M2,M3 bound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,1,0])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad9'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad9.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad9_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad9_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad10 - M1,M4 bound - M2 unbound - M3 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,2,0])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad10'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad10.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad10_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad10_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad11 - M2,M3 bound - M1 unbound - M4 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,1,2])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad11'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad11.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad11_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad11_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad12 - M2,M4 bound - M1 unbound - M3 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,2,1])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad12'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad12.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad12_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad12_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad13 - M3,M4 bound - M1 unbound - M2 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,2,2])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad13'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad13.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad13_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad13_corner_observed.png'.format(i))
    plt.close(fig)
#-------------------------------------------------------------------------------

#quad14 - M1 unbound - M2 unbound - M3 unbound - M4 unbound
dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test{}'.format(i))
t.define_models(dar, index=[0,1,2,3])

mod = StarModel(dar, obs=t)
mod.fit_multinest(n_live_points=1000,
                    basename='/tigress/np5/chains/test{}_quad14'.format(i))

if rank == 0:
    f1 = open('/tigress/np5/evidence_quad14.txt','a')
    evi = mod.evidence
    evi = str(evi)
    f1.write('case{}: '.format(i) + evi + '\n')
    f1.close()

    fig = mod.corner_physical(props=['mass', 'distance', 'AV'])
    fig.savefig('/tigress/np5/figures/test{}_quad14_corner_physical.png'.format(i))
    plt.close(fig)
    fig = mod.corner_observed()
    fig.savefig('/tigress/np5/figures/test{}_quad14_corner_observed.png'.format(i))
    plt.close(fig)
