from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones.starmodel import StarModel
from datetime import datetime

dar = Dartmouth_Isochrone()
mod = StarModel(dar)
mod.load_hdf('mod.h5')
startTime = datetime.now()
mod.fit_multinest(n_live_points=1000, refit=True)
time = datetime.now() - startTime
evi = mod.evidence

print 'evidence = {}'.format(evi)
print 'total time = {}'.format(time)
