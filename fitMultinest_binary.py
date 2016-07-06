from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from isochrones.observation import ObservationTree
from datetime import datetime
import pandas as pd

df = pd.read_csv('df_binary.csv')

dar = Dartmouth_Isochrone()
t = ObservationTree.from_df(df, name='test-binary')
t.define_models(dar, index=[0,1])
t.add_limit(logg=(3.0,None))

mod = StarModel(dar, obs=t)
startTime = datetime.now()
mod.fit_multinest(n_live_points=1000)
time = datetime.now() - startTime
evi = mod.evidence

print 'evidence = {}'.format(evi)
print 'total time = {}'.format(time)
