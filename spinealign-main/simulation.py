import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
d = 1.0  # distance increment (cm)
n_points = 80  # number of measurement points
distance = np.arange(0, n_points * d, d)  # distance along spine (cm)

# Generate realistic sagittal spine reference curve
# Thoracic kyphosis: broad peak around 20-30 cm (outward curve)
# Lumbar lordosis: valley around 55-65 cm (inward curve)
thoracic_peak = 3.0 * np.exp(-((distance - 25) / 12)**2)
lumbar_valley = -2.0 * np.exp(-((distance - 60) / 10)**2)
true_y = thoracic_peak + lumbar_valley  # sagittal displacement (cm), positive = posterior

# Compute slopes and IMU pitch angles
slope = np.gradient(true_y, distance)  # dy/ddistance
angles = np.arctan(slope)  # pitch angles (radians from horizontal)

# Simulate IMU noise and drift
noise_std = 0.005  # rad (~0.3 degrees)
drift_rate = 0.0001  # rad per step
noise = np.random.normal(0, noise_std, len(angles))
drift = np.cumsum(np.random.normal(0, drift_rate, len(angles)))
measured_angles = angles + noise + drift

# Reconstruct spine from simulated IMU data
x_rec = [0.0]  # sagittal position
y_rec = [0.0]  # vertical position

for theta in measured_angles[1:]:
    dx = d * np.sin(theta)  # sagittal displacement
    dy = d * np.cos(theta)  # vertical displacement
    x_rec.append(x_rec[-1] + dx)
    y_rec.append(y_rec[-1] + dy)

x_rec = np.array(x_rec)
y_rec = np.array(y_rec)

# Plot results
plt.figure(figsize=(6, 10))

# Reference spine
plt.plot(true_y, distance, 'b-', linewidth=2, label="Reference Spine")

# Reconstructed spine
plt.plot(x_rec, y_rec, 'r--', linewidth=2, label="Reconstructed Spine")

plt.gca().invert_yaxis()  # spine top at top of plot
plt.xlabel("Sagittal Displacement (cm)")
plt.ylabel("Distance Along Spine (cm)")
plt.title("Sagittal Spine Reconstruction Simulation")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Print reconstruction error
error = np.sqrt((x_rec - true_y)**2 + (y_rec - distance_rec)**2)
print(".2f")
print(".2f")