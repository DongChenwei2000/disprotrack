import numpy as np
import matplotlib.pyplot as plt
style = ["Nodes", "Edges", "CC"]
s1 = [5, 3, 2]
s2 = [89, 69, 20]
s3= [219, 189, 32]

xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(18, 9))

ax.bar(xticks, s1, width=0.2, label="s1", color="white", edgecolor="k", hatch="X")

ax.bar(xticks + 0.2, s2, width=0.2, label="s2", color="darkblue")

ax.bar(xticks + 0.4, s3, width=0.2, label="s3", color="white", edgecolor="k", hatch='\\')

ax.set_title("UPG properties", fontsize=15)

ax.set_ylabel("Cardinality(#)")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5)


ax.set_ylim([0.1, 300])
ax.set_yscale('log')
ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(style)
plt.savefig("upgparameter.png")
plt.show()