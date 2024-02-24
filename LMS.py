import numpy as np
import matplotlib.pyplot as plt
style = ["Mysql", "Apache2", "OpenVPN", "Wget" ]
BT2 = [605, 1499, 2281, 651]
BT3 = [676, 1523, 2513, 988]
BT4 = [709, 1530, 2535, 1013]
BT5 = [709,1530,2537,1024]

xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(15, 9))

ax.bar(xticks, BT2, width=0.2, label="BT=2", color="white", edgecolor="k",hatch="X")

ax.bar(xticks + 0.2, BT3, width=0.2, label="BT=3", color="darkblue")

ax.bar(xticks + 0.4, BT4, width=0.2, label="BT=4", color="white", edgecolor="k", hatch='\\')
ax.bar(xticks + 0.6, BT5, width=0.2, label="BT=5", color="green")
ax.set_title("LMS Found", fontsize=15)

ax.set_ylabel("LMS(#)")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5)


ax.set_ylim([0.1, 3000])
ax.set_yscale('log')



ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(style)
plt.xticks(rotation=90)
plt.savefig("LMS_chart.png")
plt.show()
