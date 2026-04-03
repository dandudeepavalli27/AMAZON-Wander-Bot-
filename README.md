# AMAZON-Wander-Bot
Aim
To implement a random walk algorithm for robot exploration.
General Objective
To understand stochastic exploration behaviors in mobile robots and how random walk strategies enable exploration in unknown environments.
Specific Objective
To update robot direction using a random angle:
Random Angle = 90°
Robot changes heading → Direction Updated
Dataset
Random Walk Dataset
Source: Navigation2 (Nav2)
Procedure
Generate a random angle
Update robot heading
Change direction
Continue movement
Display result
Algorithm
Start
Generate random angle
Update direction
Move robot
Display result
Stop
Code Logic
direction = direction + random_angle
Python Code
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
Output
Direction Updated to 90 degrees

Program Executed Successfully
Result
The robot successfully updates its direction:
Direction Updated
Industry Application
Random walk strategies are used in:
Robot exploration
Search algorithms
Area coverage
Swarm robotics
Companies like Amazon use such techniques in:
Warehouse robots
Exploration algorithms
Autonomous systems
Conclusion
Random walk enables simple yet effective exploration in unknown environments, forming a baseline for more advanced navigation strategies.
