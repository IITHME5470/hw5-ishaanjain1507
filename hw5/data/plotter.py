import numpy as np
import matplotlib.pyplot as plt
import glob

# Get all .dat files in order
data_files = sorted(glob.glob("T_x_y_000000_*.dat"))

# Plot each file
for i, file in enumerate(data_files):
    data = np.loadtxt(file)  # Load x, y, T

    x = data[:, 0]
    y = data[:, 1]
    T = data[:, 2]

    # Get unique x and y counts to reshape
    nx = len(np.unique(x))
    ny = len(np.unique(y))

    # Reshape for 2D plotting
    T_grid = T.reshape((ny, nx))
    x_grid = x.reshape((ny, nx))
    y_grid = y.reshape((ny, nx))

    plt.figure(figsize=(6, 5))
    plt.contourf(x_grid, y_grid, T_grid, cmap='hot')
    plt.colorbar(label='Temperature')
    plt.title(f'Time Step {i}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.tight_layout()
    plt.show()
    plt.savefig(f'contour_{i}.png')
    plt.close()