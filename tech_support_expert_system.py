"""
tech_support_expert_system.py
A user-friendly, rule-based expert system for basic computer troubleshooting.
"""

import re  # Regular expressions module used to match keyword patterns

# ---------- RULE DEFINITIONS ----------
# Each rule contains:
# - a name (for clarity in responses)
# - a list of keyword patterns to match against user input
# - a corresponding response (what the system should say if matched)

RULES = [
    {
        "name": "Power Issue Rule",
        "keywords": [
            r"\bwon'?t\s+turn\s+on\b",
            r"\bno\s+power\b",
            r"\bwon'?t\s+start\b",
            r"\bdead\s+computer\b",
        ],
        "response": """\
It sounds like a power issue. Try these steps:
  1. Make sure the power-cable is firmly connected to the computer AND a working outlet.
  2. Test a different outlet or power strip.
  3. Hold the power button for ~5 seconds to force a hard reset.
  4. (Laptop) Check that the battery is charged or the AC adapter LED is on."""
    },
    {
        "name": "Display Issue Rule",
        "keywords": [
            r"\bblack\s+screen\b",
            r"\bblank\s+monitor\b",
            r"\bno\s+display\b",
            r"\bscreen\s+stays?\s+off\b",
        ],
        "response": """\
Looks like a display problem. Please try:
  1. Confirm the monitor is powered on (LED lit).
  2. Reseat or replace the HDMI/DisplayPort/VGA cable.
  3. Increase screen brightness or test with an external monitor.
  4. Restart the computer after disconnecting all peripherals."""
    },
    {
    "name": "Internet Connectivity Rule",
    "keywords": [
        r"\bno\s+internet\b",
        r"\b(can'?t|cannot)\s+connect\b",
        r"\bwi[\- ]?fi\s+(not|isn'?t)\s+working\b",
        r"\bnetwork\s+down\b",
        r"\brouter\b",
    ],
    "response": """\
Network issues detected. Try:
  1. Power-cycle the modem/router (unplug → 30 s → plug back).
  2. Toggle your device’s Wi-Fi or airplane-mode switch.
  3. Forget and re-join your Wi-Fi network.
  4. Try plugging in a wired Ethernet cable to test connection."""
    },
    {
        "name": "Peripheral Device Rule",
        "keywords": [
            r"\bkeyboard\b",
            r"\bmouse\b",
            r"\busb\s+device\b",
            r"\bprinter\b",
            r"\bunresponsive\b",
            r"\bnot\s+recognized\b",
        ],
        "response": """\
Peripheral issue detected. Here are a few things to try:
  1. Unplug and reconnect the device to a different USB port.
  2. (Wireless) Replace batteries or switch the device off/on.
  3. Update or reinstall the driver.
  4. Test the device on another computer if possible."""
    },
    {
        "name": "Performance Issue Rule",
        "keywords": [
            r"\bslow\b",
            r"\blag(gy)?\b",
            r"\bfreez(e|ing)\b",
            r"\btakes?\s+forever\b",
            r"\brunning\s+hot\b",
        ],
        "response": """\
Performance problems can usually be fixed by:
  1. Closing unnecessary programs in Task Manager.
  2. Freeing up disk space and clearing temporary files.
  3. Running a malware scan.
  4. Installing all available OS and driver updates."""
    },
]

# ---------- FALLBACK MESSAGES ----------
CLARIFY_MSG = (
    "I'm not sure I understand yet. Could you describe the issue in a bit more detail?"
)

ESCALATE_MSG = (
    "I’m still having trouble figuring it out. Let me connect you with a technician."
)

HELP_TEXT = """
You can type things like:
- "My computer won’t turn on"
- "I only see a black screen"
- "The Wi-Fi isn’t working"
- "My mouse stopped responding"
- "My computer is very slow"
Type 'quit' to exit the system anytime.
"""

# ---------- MATCHING FUNCTION ----------
def match_rule(user_input):
    """
    Checks user input against each rule's keywords.
    Returns the first matching rule or None if no match is found.
    """
    # Normalize curly quotes and apostrophes to regular ones
    text = user_input.lower()
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')

    for rule in RULES:
        if any(re.search(pattern, text) for pattern in rule["keywords"]):
            return rule
    return None


# ---------- MAIN PROGRAM LOOP ----------
def main():
    # Friendly welcome message
    print("=" * 50)
    print("💻 Welcome to the Tech Support Expert System")
    print("I'm here to help you troubleshoot basic computer issues.")
    print("Type your problem below, or type 'help' for examples.")
    print("Type 'quit' anytime to exit.")
    print("=" * 50)

    unclear_count = 0  # Used to keep track of how many times input was unclear

    # Main input/output loop
    while True:
        user_input = input("\nYou: ").strip()
        
        # Exit option
        if user_input.lower() in {"quit", "q", "e", "exit"}:
            print("System: Goodbye! Hope this helped. 🛠️")
            break

        # Help command shows example phrases
        if user_input.lower() == "help":
            print(f"\nSystem Help:\n{HELP_TEXT}")
            continue

        # Try to match the input to one of the rule sets
        rule = match_rule(user_input)

        if rule:
            print(f"\nSystem ({rule['name']}):\n{rule['response']}")
            unclear_count = 0  # Reset counter if matched
        else:
            unclear_count += 1
            if unclear_count < 3:
                print(f"\nSystem: {CLARIFY_MSG}")
            else:
                print(f"\nSystem: {ESCALATE_MSG}")
                unclear_count = 0  # Reset counter after escalation

# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    main()
