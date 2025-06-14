# Building a Rule-Based AI System in Python project.

---

## Part 1: Initial Project Ideas

### 1. Project Idea 1: Symptom Checker Chatbot
- **Description:** A chatbot that asks users about their symptoms and suggests possible health conditions based on what they describe. It acts like a basic virtual health assistant to help users understand what they might be feeling.
- **Rule-Based Approach:**  
  - The system uses keywords like "fever," "cough," or "sore throat" to determine possible illnesses.
  - For example, if the user mentions “fever” and “cough,” the system responds with “You may have the flu.”

### 2. Project Idea 2: Tech Support Expert System
- **Description:** A digital assistant that helps users fix common computer issues by asking for a brief description of the problem and then offering tailored troubleshooting advice. It works like a basic IT help tool that follows a rule-based process to match issues to possible solutions.
- **Rule-Based Approach:**  
  - The system looks for keywords and phrases in the user's input and compares them against a list of predefined patterns.
  - For example, if the user says the computer doesn’t turn on, the system suggests checking the power cable and trying a hard reset.

### 3. Project Idea 3: Academic Advisor Bot
- **Description:** A virtual advisor that helps students decide which courses to take next based on their major, completed classes, and preferences. It provides suggestions like a real academic counselor using basic logic. 
- **Rule-Based Approach:**  
  - The system checks the student’s major and what classes they’ve already taken.
  - For example, if a student is majoring in Computer Science and has taken “Intro to Programming,” it recommends “Data Structures” or “Web Development.”

### **Chosen Idea:** Tech Support Expert System
**Justification:** I chose this project because it relates to the simple troubleshooting I used to do for employees at my previous job. It lets me create a basic support system using rule-based keyword matching, while storing the rules in a structure similar to JSON.

---

## Part 2: Rules/Logic for the Chosen System

The **Tech Support Expert System** will follow these rules:

1. **Power Issue Rule**  
   - **IF** the user’s message contains keywords or phrases such as **“won’t turn on,” “no power,” “won’t start,”** or **“dead computer”**  
   - **THEN** → Guide the user to:
     - Verify the power cable is firmly connected to both the computer and a working outlet.  
     - Test a different outlet or power strip.  
     - Hold the power button for 5 seconds to force a hard reset.  
     - Check for signs of battery charge (on laptops).

2. **Display Issue Rule**  
   - **IF** the user says the **PC is on** but mentions keywords or phrases like **“black screen,” “blank monitor,” “no display,”** or **“screen stays off”**  
   - **THEN** → Suggest:
     - Ensuring the monitor is turned on (power LED lit).  
     - Reseating or replacing the HDMI/DisplayPort/VGA cable.  
     - Raising screen brightness or trying an external monitor.  
     - Restarting the computer after disconnecting all peripherals.

3. **Internet Connectivity Rule**  
   - **IF** the message contains keywords or phrase combination of **“no internet,” “can’t connect,” “Wi-Fi not working,” “network down,”** or **“router”**  
   - **THEN** → Walk the user through:
     - Power-cycling (unplug → wait → plug in) the modem/router.  
     - Toggling the device’s Wi-Fi switch or airplane mode setting.  
     - Forgetting and re-joining the Wi-Fi network.  
     - Testing a wired Ethernet connection to isolate Wi-Fi issues.

4. **Peripheral Device Rule**  
   - **IF** the user mentions a **“keyboard,” “mouse,” “USB device,” “printer,”** etc. with keywords or phrases like **“not working,” “unresponsive,”** or **“not recognized”**  
   - **THEN** → Recommend:
     - Unplugging and reconnecting the device to a different USB port.  
     - Checking batteries or turning the peripheral off/on (for wireless devices).  
     - Updating or reinstalling the relevant driver.  
     - Testing the device on another computer to confirm hardware status.

5. **Performance Issue Rule**  
   - **IF** the user complains of **“slow,” “laggy,” “freezing,” “takes forever,”** or **“running hot”** behavior  
   - **THEN** → Advise:
     - Closing unnecessary programs via Task Manager / Activity Monitor.  
     - Checking disk space and deleting temporary files.  
     - Running a malware/antivirus scan.  
     - Installing pending OS and driver updates.

6. **No Match Rule**  
   - **IF** none of the above rules trigger (i.e., no recognizable keywords or conditions are present)  
   - **THEN** →  
     - Ask clarifying questions (e.g., “Can you describe what you see on-screen?”).  
     - (Simulate) Gather system details (OS version, recent changes, error codes).  
     - (Simulate) Escalate to a human technician if the issue remains unclear after two clarification attempts.


---

## Part 3: Test Cases / Sample Runs

Sample input and output: Power Issue

**User Input:**  
My computer won’t turn on.

**System Output:**
System (Power Issue Rule):  
It sounds like a power issue. Try these steps:  
  1. Make sure the power-cable is firmly connected to the computer AND a working outlet.  
  2. Test a different outlet or power strip.  
  3. Hold the power button for ~5 seconds to force a hard reset.  
  4. (Laptop) Check that the battery is charged or the AC adapter LED is on.


---


Sample input and output: Internet Connectivity Issue

**User Input:**  
The Wi-Fi isn’t working.

**System Output:**
System (Internet Connectivity Rule):  
Network issues detected. Try:  
  1. Power-cycle the modem/router (unplug → 30 s → plug back).  
  2. Toggle your device’s Wi-Fi or airplane-mode switch.  
  3. Forget and re-join your Wi-Fi network.  
  4. Try plugging in a wired Ethernet cable to test connection.


---


Sample input and output: Peripheral Device Issue

**User Input:**  
My mouse stopped working and it’s not being recognized.

**System Output:**
System (Peripheral Device Rule):  
Peripheral issue detected. Here are a few things to try:  
  1. Unplug and reconnect the device to a different USB port.  
  2. (Wireless) Replace batteries or switch the device off/on.  
  3. Update or reinstall the driver.  
  4. Test the device on another computer if possible.


---


Sample input and output: No Match

**User Input:**  
It just makes a buzzing noise.

**System Output (1st & 2nd attempt):**
System: I'm not sure I understand yet. Could you describe the issue in a bit more detail?

**System Output (3rd attempt):**
System: I’m still having trouble figuring it out. Let me connect you with a technician.


---

## Part 4: Reflection

### Project Overview:
The project involves asking the user to enter their computer issues using short prompts. The rule-based system filters their input for keywords, partial or exact matches, that it can recognize and then offers troubleshooting steps to help the user. Unlike modern machine learning, which finds patterns by learning from data, this system follows a set of clear IF/THEN rules. It doesn’t learn or change over time, it just responds based on the rules I gave it.

### Challenges:
- **Not User Friendly**  
  - I did experience the start of the code not being user friendly. It would simply start with the assumption that the user knew what to ask for, versus offering a help prompt to let the user know what to ask.
- **Lack of Comments**  
  - I understood majority of the code due to past experience with Python, but there were some portions that were new to me.
  - Asking to include additional comments for clarity helped.
- **Apostrophes Not Being Read**  
  - If a prompt included an ```'```, (e.g. The Wi-Fi isn’t working), it would originally not recognize the prompt for keywords.