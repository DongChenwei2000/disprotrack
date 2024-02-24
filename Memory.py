import numpy as np
import matplotlib.pyplot as plt
style = ["Mysql", "Apache2", "OpenVPN", "Wget" ]
BT2 = [1557.2890625, 725.6953125, 1138.890625, 729.875]
BT3 = [1560.71484375, 724.23828125, 1138.9921875, 758.2265625]
BT4 = [1567.8359375, 727.234375, 1139.25, 767.1484375]
BT5 = [1571.765625,726.703125,1139.04296875,768.82421875]

xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(18, 9))

ax.bar(xticks, BT2, width=0.2, label="BT=2", color="white", edgecolor="k", hatch="X")

ax.bar(xticks + 0.2, BT3, width=0.2, label="BT=3", color="darkblue")

ax.bar(xticks + 0.4, BT4, width=0.2, label="BT=4", color="white", edgecolor="k", hatch='\\')
ax.bar(xticks + 0.6, BT5, width=0.2, label="BT=5", color="green")
ax.set_title("Memory Consumption", fontsize=15)

ax.set_ylabel("Mem(MB)")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5)


ax.set_ylim([0.1, 2000])
ax.set_yscale('log')



ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(style)
plt.xticks(rotation=90)
plt.savefig("memory_chart.png")
plt.show()
