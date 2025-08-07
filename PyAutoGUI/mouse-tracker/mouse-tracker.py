import pyautogui
import time
import keyboard

print("Mouse Position Tracker")
print("Press 'q' to quit")
print("Moving mouse will show coordinates...")

# Get screen size
screen_width, screen_height = pyautogui.size()
print(f"Screen size: {screen_width}x{screen_height}")

try:
    while True:
        # Check if 'q' is pressed to quit
        if keyboard.is_pressed('q'):
            print("Stopping mouse tracker...")
            break
        
        # Get current mouse position
        x, y = pyautogui.position()
        
        # Get pixel color at mouse position
        pixel_color = pyautogui.pixel(x, y)
        
        # Clear the line and print current position
        print(f"\rMouse position: X={x}, Y={y} | Color: RGB{pixel_color}", end="", flush=True)
        
        # Small delay to prevent excessive CPU usage
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\nMouse tracker stopped by user")
