import numpy as np
import matplotlib.pyplot as plt
style = ["Mysql", "Apache2", "OpenVPN", "Wget" ]
BT2 = [642.8485519886017, 141.562481880188, 241.70070028305054, 111.4842700958252]
BT3 = [681.7409737110138, 189.0080623626709, 246.83098769187927, 126.45738387107849]
BT4 = [704.8152554035187, 181.7157905101776, 248.993194806366, 131.8366572856903]
BT5 = [780.5690031051636,185.02718949317932,244.34452986717224,149.51881289482117]

xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(15, 9))

ax.bar(xticks, BT2, width=0.2, label="BT=2", color="white", edgecolor="k",hatch="X")

ax.bar(xticks + 0.2, BT3, width=0.2, label="BT=3", color="darkblue")

ax.bar(xticks + 0.4, BT4, width=0.2, label="BT=4", color="white", edgecolor="k", hatch='\\')
ax.bar(xticks + 0.6, BT5, width=0.2, label="BT=5", color="green")
ax.set_title("Required Time", fontsize=15)

ax.set_ylabel("Time(s)")

ax.legend()


ax.set_ylim([0.1, 1000])
ax.set_yscale('log')



ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(style)
plt.xticks(rotation=90)
plt.savefig("bar_chart.png")
plt.show()
