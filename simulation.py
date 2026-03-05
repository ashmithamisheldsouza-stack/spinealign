import numpy as np
import matplotlib.pyplot as plt

d = 1
n_points = 40
distance = np.arange(0, n_points*d, d)

true_y = 5 * np.sin(distance / 8)
true_x = distance

angles = np.arctan(np.gradient(true_y, true_x))

x_rec = [0]
y_rec = [0]

for theta in angles:
    x_new = x_rec[-1] + d * np.cos(theta)
    y_new = y_rec[-1] + d * np.sin(theta)
    x_rec.append(x_new)
    y_rec.append(y_new)

x_rec = np.array(x_rec[1:])
y_rec = np.array(y_rec[1:])

plt.plot(true_x, true_y, label="Reference Spine Curve")
plt.plot(x_rec, y_rec, label="Reconstructed Spine Curve")
plt.legend()
plt.xlabel("Distance Along Spine")
plt.ylabel("Sagittal Displacement")
plt.title("Spinal Curve Reconstruction Simulation")

plt.show()