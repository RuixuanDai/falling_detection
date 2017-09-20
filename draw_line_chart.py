import numpy as np
import matplotlib.pyplot as plt


filename = "a.csv"
data = np.genfromtxt(
    filename, delimiter=",", skip_header=1,
    dtype=[('time', 'f'), ('x', 'f'), ('y', 'f'), ('z', 'f')]
)
time = data["time"]
acc_x = data["x"]
acc_y = data["y"]
acc_z = data["z"]

fig, ax = plt.subplots()
ax.plot(time, acc_x, 'r', label='x', linewidth=2)
ax.plot(time, acc_y, 'b', label='y', linewidth=2)
ax.plot(time, acc_z, 'y', label='z', linewidth=2)
legend = ax.legend(loc="best", shadow=True, title="axis")
plt.xlabel("Time/s")
plt.ylabel("Accelerations/g")
plt.show()
