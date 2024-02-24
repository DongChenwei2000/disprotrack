import numpy as np
import matplotlib.pyplot as plt
style = ["s1", "s2", "s3"]

ascl = [0.03602933883666992, 0.26879215240478516, 0.28981852531433105]

parse = [0.07567071914672852, 1.111055612564087,1.061547040939331]
xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(18, 9))

ax.bar(xticks, ascl, width=0.2, label="ASCL GEN", color="darkblue")
ax.bar(xticks, parse, width=0.2, label="Parsing", color="white", edgecolor="k", hatch="X", bottom=ascl)



ax.set_title("Experiment", fontsize=15)

ax.set_ylabel("Time(s)")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5)


ax.set_ylim([0, 1.5])

ax.set_xticks(xticks + 0.01)
ax.set_xticklabels(style)
plt.savefig("execution time.png")
plt.show()