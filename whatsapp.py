#Importing the required libraries
import pyautogui as pg 
import time

#Giving delay to run program
print("You have 5 seconds to open WhatsApp Web and select the chat.")
time.sleep(5)

## Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages

for i in range(100):
    #writing the message
    pg.write("Hello, Butkiiii")
    time.sleep(0.5)
    #seding the message by pressing enter
    pg.press("enter")
    time.sleep(0.5)
