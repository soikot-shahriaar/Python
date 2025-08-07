import pyautogui
import time
import keyboard

def auto_message():
    print("=== Auto Message Bot ===")
    print("This bot will automatically type and send messages")
    print("Press 'q' to stop the bot at any time")
    print()
    
    # Get user input for customization
    message = input("Enter your message (or press Enter for default): ").strip()
    if not message:
        message = "Hi! I am a bot"
    
    # Get timing from user
    try:
        delay = float(input("Enter delay between messages in seconds (default 3): ") or "3")
    except ValueError:
        delay = 3
        print("Invalid input, using default delay of 3 seconds")
    
    print(f"\nBot will send: '{message}' every {delay} seconds")
    print("Starting in 5 seconds... Click in the text field where you want to type!")
    print("Press 'q' to stop")
    
    # Safety delay
    time.sleep(5)
    
    # Set pyautogui safety settings
    pyautogui.PAUSE = 0.1  # Small pause between actions
    
    message_count = 0
    
    try:
        while True:
            # Check if 'q' is pressed to quit
            if keyboard.is_pressed('q'):
                print(f"\nBot stopped! Total messages sent: {message_count}")
                break
            
            # Type the message
            pyautogui.typewrite(message)
            time.sleep(0.5)  # Small pause before pressing Enter
            
            # Press Enter to send
            pyautogui.press("Enter")
            
            message_count += 1
            print(f"Message {message_count} sent: '{message}'")
            
            # Wait for next message
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print(f"\nBot stopped by user! Total messages sent: {message_count}")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print(f"Total messages sent: {message_count}")

if __name__ == "__main__":
    auto_message()