#!python3

import matplotlib.pyplot as plt
import os.path

SYNC_VARIANTS = ("sync_false", "sync_true")
IO_VARIANTS = ("no_io", "cout", "printf")
OPTIMIZATION_VARIANTS = ("O0", "O2", "O3")

columns = SYNC_VARIANTS
rows = tuple('_'.join((io, o_level))
             for io in IO_VARIANTS
             for o_level in OPTIMIZATION_VARIANTS)

cell_text = list()

for io in IO_VARIANTS:
    for o_level in OPTIMIZATION_VARIANTS:
        row = []
        for sync in SYNC_VARIANTS:
            filename = os.path.join(
                "outputs", "_".join((sync, io, o_level)) + ".out")
            with open(filename) as output_file:
                file_content = output_file.read()
                ms = int(file_content.split()[0])
                row.append(f"{ms}")
        cell_text.append(row)

fig, ax = plt.subplots()
plt.title("Average execution time, microseconds")
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

table = ax.table(cellText=cell_text,
                 rowLabels=rows,
                 colLabels=columns,
                 loc='center')
fig.tight_layout()
plt.show()
