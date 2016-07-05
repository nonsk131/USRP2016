import pandas as pd
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.observation import ObservationTree
from isochrones.starmodel import StarModel
from datetime import datetime


df = pd.read_cvs('df.csv')

dar = Dartmouth_Isochrone()

t = ObservationTree.from_df(df, name='test-triplet')
t.define_models(dar)
t.add_limit(logg=(3.0,None))
t.print_ascii()

mod = StarModel(dar, obs=t)
startTime = datetime.now()
mod.fit_multinest(n_live_points=1000, refit=True)
time = datetime.now() - startTime
evi = mod.evidence

print 'evidence = {}'.format(evi)
print 'total time = {}'.format(time)
