import numpy as np

# Define the data type of the structured array
dt = np.dtype([('position', [('x', float), ('y', float)]), ('color', [('r', float), ('g', float), ('b', float)])])

# Create the structured array with values
structured_array = np.array([((1, 2), (0.5, 0.5, 0.5)), ((3, 4), (0.2, 0.3, 0.4)), ((5, 6), (0.1, 0.2, 0.3))], dtype=dt)

print("Position (x, y):", structured_array['position'])
print("Color (r, g, b):", structured_array['color'])
