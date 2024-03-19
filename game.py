import random
import sys

# ANSI escape code colors
BLUE_TEXT = "\033[94m"
RED_TEXT = "\033[91m"
GREEN_TEXT = "\033[92m"
RESET_TEXT = "\033[0m"

EDUCATIONAL_MESSAGES = {
    'Malware': [
        "Good job! Antivirus software helps identify and eliminate malware threats.",
        "Brilliant! Firewalls prevent unauthorized access and are crucial for stopping malware.",
        "Regularly scanning your computer for malware can help detect and remove hidden threats.",
        "Keeping your operating system and applications up to date is crucial for protecting against malware.",
        "Using strong, unique passwords and changing them regularly can prevent malware from spreading.",
        "Implementing email filters can help block malicious attachments and links, reducing malware risk.",
    ],
    'Phishing': [
        "Recognizing and reporting phishing emails helps protect you and others from identity theft.",
        "Training on how to identify phishing attempts can significantly reduce their success.",
        "Using two-factor authentication adds an extra layer of security against phishing scams.",
        "Avoiding clicking on links from unknown sources is key to preventing phishing.",
        "Using a dedicated email account for financial services can help isolate and identify phishing attempts.",
        "Monitoring financial accounts for unauthorized transactions can detect phishing fallout.",
    ],
    'Ransomware': [
        "Regular backups can help you recover your data without paying a ransom in case of a ransomware attack.",
        "Antivirus software with real-time scanning can prevent ransomware from taking hold.",
        "Avoiding opening emails and attachments from unknown sources can protect against ransomware.",
        "Keeping software and operating systems up to date can prevent ransomware attacks.",
        "Using application whitelisting can prevent unauthorized programs, including ransomware, from running.",
        "Regularly auditing networks for vulnerabilities can help prevent ransomware exploits.",
    ],
    'Spyware': [
        "Antispyware tools can help detect and remove software that may be covertly spying on your activities.",
        "Being mindful of the permissions you grant to apps can reduce the risk of spyware.",
        "Regularly updating your security software can help protect against the latest spyware threats.",
        "Using strong, unique passwords for different accounts can hinder spyware from capturing your data.",
        "Limiting the use of public Wi-Fi can reduce the risk of spyware attacks.",
        "Employing anti-tracking tools can help shield your online activities from spyware.",
    ],
    'DDoS': [
        "A strong network firewall can help mitigate a DDoS attack.",
        "Using a content delivery network (CDN) can help distribute traffic and reduce DDoS impact.",
        "Having a DDoS response plan in place can ensure quick and effective action during an attack.",
        "Monitoring network traffic can help identify and mitigate DDoS attacks early.",
        "Implementing rate limiting can prevent servers from being overwhelmed by DDoS traffic.",
        "Employing IP blacklisting can block traffic from known malicious sources.",
    ]
}


    # ... add other threat types if any ...

# Threat Messages (simplified for demonstration)
THREAT_MESSAGES = {
    
    'Malware': [
        "Unexpected software behavior might indicate a hidden presence.",
        "Your system's slowing down could be a sign of unwanted guests.",
        "An ounce of prevention is worth a pound of cure, especially in digital hygiene.",
        "Silent but deadly, some threats prefer to remain unnoticed.",
        "Routine checks can unveil hidden dangers lurking within.",
        "A vigilant guardian never lets their guard down.",
        "What lies beneath the surface could be harmful to your digital health.",
        "An unwatched system is a paradise for digital pests.",
    ],
    'Phishing': [
        "Beware of messages that request personal information, even if they seem legitimate.",
        "Even the most trustworthy-looking emails could be a trap for the unwary.",
        "A careful inspection of email contents could reveal deceptive intentions.",
        "Phishing attempts often create a sense of urgency; pause and verify before acting.",
        "Unexpected requests for sensitive information should always be treated with suspicion.",
        "Legitimate organizations rarely ask for your personal details via email.",
    ],
    'Ransomware': [
        "The demand for a ransom could be the result of a seemingly innocent click.",
        "Frequent data backups could be your plan B in a ransomware crisis.",
        "Ransomware can disguise itself in the form of attachments or software updates.",
        "Always be wary of software demands that lock access to your own data.",
        "A seemingly benign download can hold your data hostage.",
        "Ransomware is like a digital hijacking of your precious files.",
    ],
    'Spyware': [
        "Your digital footprint might be watched by unseen eyes.",
        "Unexplained activity on your accounts could be a sign of covert surveillance.",
        "The spy within can come in the form of a harmless-looking app.",
        "Being vigilant about app permissions can keep the digital spies away.",
        "What you can't see can hurt you: spyware operates in the shadows.",
        "Keep your confidential information out of reach from digital snoops.",
    ],
    'DDoS': [
        "An overwhelming flood of traffic could be an orchestrated attack.",
        "Your servers might become collateral damage in a DDoS onslaught.",
        "Sometimes, too much attention is a bad thing, especially if it's a DDoS attack.",
        "A tsunami of digital requests could drown your online presence.",
        "When your services are inaccessible, consider the possibility of a DDoS attack.",
        "The digital traffic jam cluttering your network might be malicious.",
    ]
}

        # Add more DDoS hints here...
    


VICTORY_MESSAGES = [
    "Congratulations, Cyber Paladin! You've successfully shielded our digital realm from chaos!",
    "Virtuoso of Virtual Defense, your cybersecurity skills have preserved the integrity of our bytes and bits!",
    "Mighty Guardian of the Gateway, you have thwarted the malevolent digital entities!",
    "Supreme Sentinel, the firewall of your wisdom stands unbreached!",
    "Champion of Cyberspace, your defensive prowess is unmatched in the ethernet!",
    "Grandmaster of the Grid, your strategic maneuvers have kept our data domain sovereign!",
    "Digital Overlord, your skillful commands have routed the invaders from our server sanctums!",
    "Sovereign of Security, you’ve encrypted our fears and decrypted peace!",
    "Byte-sized Battles, Mega Victory! You have debugged the future from dystopian threats!",
    "Master of the Mainframe, your vigilance has kept the shadow of uncertainty at bay!",
]


1# Constants for game configuration
GRID_WIDTH = 20
GRID_HEIGHT = 20
THREAT_TYPES = {'Malware': '1', 'Phishing': '2', 'Ransomware': '3', 'Spyware': '4', 'DDoS': '5'}
TOOLS = {'1': 'Firewall', '2': 'Antivirus', '3': 'Encryption', '4': 'Backup', '5': 'Antispyware'}
TOOL_COUNTS = {key: 6 for key in TOOLS.keys()}  # Initialize tool counts to 6
THREATS_NUM = 10

class Player:
    def __init__(self):
        self.x = random.randint(0, GRID_WIDTH - 1)
        self.y = random.randint(0, GRID_HEIGHT - 1)
        self.tools = TOOL_COUNTS.copy()

    def display_tools(self):
        print(f"{RESET_TEXT}Tools Inventory:")
        for tool_key, tool_name in sorted(TOOLS.items()):
            print(f"{tool_key} - {tool_name}: {self.tools[tool_key]}")

    def move(self, direction, grid):
        # Move player in the given direction and update the grid
        if direction == 'w' and self.y > 0:
            self.y -= 1
        elif direction == 's' and self.y < GRID_HEIGHT - 1:
            self.y += 1
        elif direction == 'a' and self.x > 0:
            self.x -= 1
        elif direction == 'd' and self.x < GRID_WIDTH - 1:
            self.x += 1
        else:
            print(f"{RED_TEXT}You can't move in that direction.{RESET_TEXT}")        

class Threat:
    def __init__(self):
        self.x = random.randint(0, GRID_WIDTH - 1)
        self.y = random.randint(0, GRID_HEIGHT - 1)
        self.threat_type = random.choice(list(THREAT_TYPES))  # Choose a type as a string key

class Grid:
    def __init__(self):
        self.threats = [Threat() for _ in range(THREATS_NUM)]


    def display_game_over(self):
        self.display_message("GAME OVER", RED_TEXT)

    def display_final_score(self, score):
        # Clear the console screen
        print("\033[H\033[J", end="")
        message = f"Final Score: {score}"
        self.display_message(message, GREEN_TEXT)
        # No need to check for nearby threats when displaying final score

    def display_message(self, message, text_color):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                start_x = GRID_WIDTH // 2 - len(message) // 2
                if y == GRID_HEIGHT // 2 and start_x <= x < start_x + len(message):
                    print(f"{text_color}{message[x - start_x]}{RESET_TEXT}", end='')
                else:
                    print(" ", end=' ')
            print()
        print("\n" + "=" * 40)

    def check_for_nearby_threats(self, player):
        threat_nearby = False
        for threat in self.threats:
            if abs(threat.x - player.x) <= 1 and abs(threat.y - player.y) <= 1:
                random_message = random.choice(THREAT_MESSAGES[threat.threat_type])
                print(f"{BLUE_TEXT}Caution: {random_message}{RESET_TEXT}")
                threat_nearby = True
                break
        if not threat_nearby:
            print(f"{BLUE_TEXT}No immediate threats detected.{RESET_TEXT}")
    def display(self, player, game_over_reason=""):
        print("\n" + "=" * 40)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                # Center the game over message by calculating the start position
                game_over_start_pos = GRID_WIDTH // 2 - len("GAME OVER") // 2
                # Check if we're in the center of the grid to print "GAME OVER"
                if game_over_reason and GRID_HEIGHT // 2 == y and game_over_start_pos <= x < game_over_start_pos + len("GAME OVER"):
                    print("GAME OVER"[x - game_over_start_pos], end=' ')
                else:
                    char = "P" if player.x == x and player.y == y else \
                           f"{RED_TEXT}T{RESET_TEXT}" if any(threat.x == x and threat.y == y for threat in self.threats) else "."
                    print(char, end=' ')
            print()
        print("=" * 40)
        if not game_over_reason:
            self.check_for_nearby_threats(player)
            player.display_tools()
        else:
            print(f"{RED_TEXT}{game_over_reason}{RESET_TEXT}")

    def display_game_over(self):
        # Clear the console screen
        print("\033[H\033[J", end="")
        
        # Print the game over grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                # Calculate the position for "GAME OVER" horizontally and vertically
                game_over_start_x = GRID_WIDTH // 2 - len("GAME OVER") // 2
                game_over_start_y = GRID_HEIGHT // 2

                if y == game_over_start_y and game_over_start_x <= x < game_over_start_x + len("GAME OVER"):
                    print("GAME OVER"[x - game_over_start_x], end=' ')
                else:
                    print(" ", end=' ')
            print()

def deploy_tool(player, grid, tool_key):
    tool_name = TOOLS[tool_key]
    threat = next((t for t in grid.threats if t.x == player.x and t.y == player.y), None)

    if threat is None:
        print(f"{BLUE_TEXT}No threat at this location.{RESET_TEXT}")
        return

    if player.tools[tool_key] <= 0:
        print(f"{RED_TEXT}No {tool_name} tools left.{RESET_TEXT}")
        return

    if THREAT_TYPES[threat.threat_type] == tool_key:
        message = random.choice(EDUCATIONAL_MESSAGES[threat.threat_type])
        print(f"{GREEN_TEXT}Correct tool! {message}{RESET_TEXT}")
        grid.threats.remove(threat)
    else:
        # Selects one random hint message associated with the threat type
        hint_message = random.choice(THREAT_MESSAGES[threat.threat_type])
        print(f"{RED_TEXT}Wrong tool! The {threat.threat_type} threat is still active. Hint: {hint_message}{RESET_TEXT}")

    player.tools[tool_key] -= 1



# ... (Assuming all necessary classes, global variables, and constants are defined above this point) ...

def game_over(player, grid):
    # First, check if there are no threats left on the grid
    if not grid.threats:
        return False, "All threats have been neutralized!"

    # Now check if there's at least one tool to counter each type of threat on the grid
    for threat in grid.threats:
        tool_key = THREAT_TYPES[threat.threat_type]
        if player.tools[tool_key] == 0:
            # If a specific tool has run out, and there is a threat of that type, it's game over
            return True, f"No {TOOLS[tool_key]} tools left to counter remaining {threat.threat_type} threats!"

    # If we have at least one of each tool required for the remaining threats, the game is not over
    return False, "You can still fight the threats!"


def main():
    while True:  # Start an infinite loop for the game
        print("Welcome to the Cyber Defender Game!")
        print("How to play:")
        print("- Move your player using 'w', 'a', 's', 'd' for up, left, down, right.")
        print("- Deploy tools to counter threats by entering the number associated with the tool.")
        print("- Manage your tool inventory wisely and eliminate all threats to win the game.")
        print("- Each remaining tool in your inventory counts as 1 point in your score.")
        print("- If you run out of tools and threats remain, it's game over!")
        print("- Eliminate all threats to achieve victory and calculate your score based on remaining tools.")
        print("- Enter 'exit' at any time to quit the game.\n")

        player = Player()
        grid = Grid()
        grid.display(player)

        while True:  # This is the main game loop
            action = input("Choose action - Move (w/a/s/d), Deploy Tool (number), or Exit (exit): ").lower()

            if action in ['w', 'a', 's', 'd']:
                player.move(action, grid)
            elif action in TOOL_COUNTS.keys():
                deploy_tool(player, grid, action)
            elif action == 'exit':
                print("Exiting game. Goodbye!")
                return  # Use 'return' to exit the function and thus the game
            else:
                print(f"{RED_TEXT}Invalid action. Please try again.{RESET_TEXT}")

            grid.display(player)

            is_game_over, game_over_reason = game_over(player, grid)
            if is_game_over:
                grid.display_game_over()
                print(f"{RED_TEXT}{game_over_reason}{RESET_TEXT}")
                break  # Break out of the main game loop to the play again or quit prompt

            if not grid.threats:
                score = sum(player.tools.values())
                grid.display_final_score(score)
                break  # Break out of the main game loop to the play again or quit prompt

        # Play again or quit prompt
        print("Would you like to play again? (yes/no): ", end='')
        action = input().lower()
        if action != "yes":
            print("Thank you for playing. Goodbye!")
            break  # Break out of the infinite game loop and end the game

if __name__ == "__main__":
    main()

