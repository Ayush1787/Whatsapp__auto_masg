# Whatsapp__auto_masg
This Python script automates sending repeated messages on WhatsApp Web using PyAutoGUI. After a 5-second setup delay, it types and sends a selected message 100 times by simulating keyboard input. Useful for testing automation, UI interactions, and bot-like message operations.

WhatsApp Auto Message Sender 🚀
Automate sending repeated messages on WhatsApp Web using Python and PyAutoGUI. This script simulates keyboard typing and key presses, allowing you to send a message multiple times automatically.

📌 Features
Sends automated messages on WhatsApp Web
Uses PyAutoGUI for keyboard automation
Customizable delay and number of messages
Simple, lightweight, and beginner-friendly

🛠️ Requirements

Ensure the following libraries are installed:
pip install pyautogui

Python 3.6 or above is recommended.

📁 How It Works
Run the Python script
You get 5 seconds to open WhatsApp Web
Select the chat where messages will be sent
Script begins typing and sending messages automatically

⚡ Customization
You can modify the message count and text:
for i in range(50):       # change message count

    pg.write("Your Message")  # change text

Adjust time delay for slower or faster execution:
time.sleep(1)
⚠️ Important Notes

Use responsibly.
Auto-messaging can be considered spam.
WhatsApp may restrict accounts if misused.
