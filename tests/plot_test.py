import elements as el
import os

filepath = os.path.expanduser(f'{el.ROOT_DIR}/../examples/lattices/FODO-lattice.json')
line = el.read_lattice_file_json(filepath)
# el.save_lattice_file_json(line, "wosolldassein.json")
fodo = line.cells["fodo"]
print(fodo.length)
Q1 = line.elements["Q1"]
B1 = line.elements["B1"]
lin = el.LinBeamDyn(line)


import matplotlib.pyplot as plt
from elements.plotting import plot_full, plot_twiss

ax = plt.axes()
plot_twiss(ax, lin.twiss, linestyle="dashed")
line.elements["Q2"].k1 = -1.4
plot_full(ax, lin, path="test.pdf", overwrite=True)

