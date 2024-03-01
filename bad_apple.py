import time
import os

# Define text frames for the animation
frames = [
    "Frame 1",
    "Frame 2",
    "Frame 3",
    # Add more frames here...
]

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the frames as an animation
for frame in frames:
    clear_screen()
    print(frame)
    time.sleep(0.1)  # Adjust the delay between frames as needed

