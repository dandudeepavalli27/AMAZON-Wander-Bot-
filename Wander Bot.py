# SESSION 33 – Wander Bot (Random Walk)

import random

# Step 1: Current direction
direction = 0  # initial heading in degrees

# Step 2: Generate random angle
random_angle = 90  # example value (can use random.randint(0, 360))

# Step 3: Update direction
direction = direction + random_angle

# Step 4: Display result
print("Direction Updated to", direction, "degrees")

print("\nProgram Executed Successfully")
