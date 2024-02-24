import numpy as np
import matplotlib.pyplot as plt
style = ["s1", "s2", "s3"]
ascl = [12.734375, 13.5234375, 13.14453125]
upg = [64.12109375, 72.078125, 72.4140625]


xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(18, 9))

ax.bar(xticks, ascl, width=0.2, label="ASCL GEN", color="darkblue")

ax.bar(xticks + 0.2, upg, width=0.2, label="UPG GEN", color="white", edgecolor="k", hatch='\\')


ax.set_title("Experiment", fontsize=15)

ax.set_ylabel("Mem(BYtes)")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5)


ax.set_ylim([10, 80])

ax.set_xticks(xticks + 0.1)
ax.set_xticklabels(style)
plt.savefig("memory utilizition.png")
plt.show()