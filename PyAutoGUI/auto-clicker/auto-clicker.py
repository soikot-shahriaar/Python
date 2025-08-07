import pyautogui
import time
import keyboard

print("Auto Clicker - Press 'q' to quit")
print("Clicking will start in 5 seconds...")
time.sleep(5)

# Set a safety delay to prevent rapid clicking
pyautogui.PAUSE = 0.5

try:
    while True:
        # Check if 'q' is pressed to quit
        if keyboard.is_pressed('q'):
            print("Stopping auto clicker...")
            break
        
        # Perform a left click
        pyautogui.click()
        print("Clicked!")
        
        # Wait for 2 seconds before next click
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nAuto clicker stopped by user")
