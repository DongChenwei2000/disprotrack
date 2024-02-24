import numpy as np
import matplotlib.pyplot as plt
style = ["s1", "s2", "s3"]

s= [2.7924323081970215, 3.3726608753204346, 5.269985914230347]

xticks = np.arange(len(style))

fig, ax = plt.subplots(figsize=(9,5))

ax.bar(xticks+0.25, s, width=0.2, label="s1", color="red")



ax.set_title("Experiment", fontsize=15)

ax.set_ylabel("Total(s)")




ax.set_ylim([2, 6])

ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(style)

plt.savefig("UPG COnstruction.png")
plt.show()