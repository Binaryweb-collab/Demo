import time
from tqdm import tqdm

# Welcome Message Animation
message = "Welcome to the Neonvators Team!"
for char in message:
    print(char, end='', flush=True)
    time.sleep(0.1)  # Typing effect delay

print("\n\n🎉 Meet the Team Members 🎉\n")

# List of team members
team_members = ["Lakshitha", "Angel"]

# Animated Progress Bar
for member in tqdm(team_members, desc="Loading Team Members", ascii=" █"):
    time.sleep(1.5)  # Simulate loading time
    print(f"✨ {member} has joined the team!")

print("\n🚀 Let's innovate with Neonvators! 💡")
