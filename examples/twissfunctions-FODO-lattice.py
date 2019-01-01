import plotly
plotly.io.orca.config.executable = '/home/felix/anaconda3/bin/orca'
plotly.io.orca.config.save()



import elements as el
from elements.linbeamdyn import LinBeamDyn

D1 = el.Drift('D1', length=0.55)
Q1 = el.Quad('Q1', length=0.2, k1=1.2)
B1 = el.Bend('B1', length=1.5, angle=0.392701, e1=0.1963505, e2=0.1963505)
Q2 = el.Quad('Q2', length=0.4, k1=-1.2)
fodo = el.Line('fodo-cell', [Q1, D1, B1, D1, Q2, D1, B1, D1, Q1])
ring = el.Mainline('fodo-ring', [fodo] * 8)

lin = LinBeamDyn(ring)
import matplotlib.pyplot as plt

plt.plot(ring.s, lin.twiss.betax)
plt.show()