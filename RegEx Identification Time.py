import numpy as np
import matplotlib.pyplot as plt
style = ["s1", "s2", "s3"]
s1 = [55.85908889770508, 58.049917221069336, 55.10258674621582]


xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(xticks+0.25, s1, width=0.2, label="s1", color="red")



ax.set_title("Experiment", fontsize=15)

ax.set_ylabel("Match(ms)")




ax.set_ylim([55, 59])

ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(style)

plt.savefig("RegEx.png")
plt.show()