import time
import os
import random
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.05, color=None):
    """Display text with a typing effect and optional color."""
    for char in text:
        if color:
            print(f"{color}{char}{Style.RESET_ALL}", end='', flush=True)
        else:
            print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_neon_banner():
    """Display a neon-style banner."""
    banner = """
    ╔═══════════════════════════════════════════╗
    ║  _   _                                    ║
    ║ | \ | | ___  ___  _ ____   ____ _| |_ ___ ║
    ║ |  \| |/ _ \/ _ \| '_ \ \ / / _` | __/ _ \\║
    ║ | |\  |  __/ (_) | | | \ V / (_| | || (_) ║
    ║ |_| \_|\___|\___/|_| |_|\_/ \__,_|\__\___/║
    ║                                           ║
    ╚═══════════════════════════════════════════╝
    """
    colors = [Fore.CYAN, Fore.MAGENTA, Fore.BLUE, Fore.GREEN]
    for line in banner.split('\n'):
        color = random.choice(colors)
        print(f"{color}{line}{Style.RESET_ALL}")

def animate_team_member(name, role="Team Member", emoji="✨"):
    """Animate the introduction of a team member with role and emoji."""
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    for _ in range(10):
        for frame in frames:
            print(f"\r{Fore.CYAN}{frame} Loading profile for {name}...", end="")
            time.sleep(0.1)
    print(f"\r{emoji} {Fore.YELLOW}{name}{Style.RESET_ALL} has joined as {Fore.GREEN}{role}{Style.RESET_ALL}!{' ' * 20}")
    time.sleep(0.5)

def main():
    # Team member data with roles
    team_members = [
        {"name": "Lakshitha", "role": "Tech Lead", "emoji": "🚀"},
        {"name": "Angel", "role": "Creative Director", "emoji": "🎨"}
    ]
    
    # Optional: Add more team members
    # team_members.append({"name": "Alex", "role": "Developer", "emoji": "💻"})
    # team_members.append({"name": "Jordan", "role": "Designer", "emoji": "🎭"})

    # Clear screen and display banner
    clear_screen()
    display_neon_banner()
    time.sleep(1)
    
    # Welcome message with colorful typing effect
    typing_effect("\nWelcome to the Neonvators Team!", delay=0.08, color=Fore.MAGENTA)
    print("\n" + "=" * 40 + "\n")
    
    # Team members introduction
    typing_effect("🎉 Meet the Innovative Minds Behind Neonvators 🎉", color=Fore.YELLOW)
    print()
    
    # Progress bar for team loading
    for _ in tqdm(range(100), 
                 desc=f"{Fore.CYAN}Initializing Team Portal{Style.RESET_ALL}", 
                 bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
                 colour="GREEN"):
        time.sleep(0.03)
    
    print()
    
    # Introduce each team member with animation
    for member in team_members:
        animate_team_member(member["name"], member["role"], member["emoji"])
    
    # Final message
    print("\n" + "=" * 40)
    typing_effect("\n🚀 Let's innovate with Neonvators! The future is neon bright! 💡", 
                  delay=0.06, 
                  color=Fore.CYAN)
    
    # Display a motivational quote
    quotes = [
        "Innovation distinguishes between a leader and a follower.",
        "The best way to predict the future is to create it.",
        "Creativity is intelligence having fun.",
        "Where there is innovation, there is energy."
    ]
    
    time.sleep(1)
    print(f"\n{Fore.MAGENTA}💭 {random.choice(quotes)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
