import pyautogui
import time
from datetime import datetime
import os

# Create screenshots directory if it doesn't exist
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

print("Screen Screenshot Taker")
print("Taking screenshots every 10 seconds...")
print("Press Ctrl+C to stop")

try:
    screenshot_count = 1
    
    while True:
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Take screenshot
        screenshot = pyautogui.screenshot()
        
        # Save screenshot with timestamp
        filename = f"screenshots/screenshot_{timestamp}.png"
        screenshot.save(filename)
        
        print(f"Screenshot {screenshot_count} saved: {filename}")
        screenshot_count += 1
        
        # Wait for 10 seconds
        time.sleep(10)
        
except KeyboardInterrupt:
    print(f"\nStopped! Total screenshots taken: {screenshot_count - 1}")
