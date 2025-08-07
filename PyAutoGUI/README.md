# Python Automation Projects

This folder contains several basic automation projects using Python and PyAutoGUI.

## Projects

### 1. Message Automation (`message-automation/`)
- **File**: `auto-message.py`
- **Function**: Automatically types and sends customizable messages
- **Usage**: 
  - Run the script
  - Enter your custom message (or press Enter for default)
  - Set delay between messages in seconds
  - Click in the text field where you want to type
  - Wait 5 seconds for it to start
  - Press 'q' to stop anytime

### 2. Auto Clicker (`auto-clicker/`)
- **File**: `auto-clicker.py`
- **Function**: Automatically clicks at regular intervals
- **Usage**: 
  - Run the script
  - Wait 5 seconds for it to start
  - Press 'q' to stop
  - Clicks every 2 seconds

### 3. Screen Screenshot (`screen-screenshot/`)
- **File**: `screen-screenshot.py`
- **Function**: Takes screenshots at regular intervals
- **Usage**:
  - Run the script
  - Screenshots are saved in a `screenshots/` folder
  - Takes a screenshot every 10 seconds
  - Press Ctrl+C to stop

### 4. Mouse Tracker (`mouse-tracker/`)
- **File**: `mouse-tracker.py`
- **Function**: Tracks and displays mouse position and pixel color
- **Usage**:
  - Run the script
  - Move your mouse to see real-time coordinates
  - Press 'q' to stop

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run any project:
```bash
python project-name/script-name.py
```

## Requirements

- Python 3.6+
- pyautogui
- keyboard
- Pillow (for screenshots)

## Safety Notes

- These scripts control your mouse and keyboard
- Always have a way to stop them (Ctrl+C or 'q' key)
- Be careful when running automation scripts
- Test in a safe environment first

## Tips

- Use these projects to learn about automation
- Modify the timing and actions to suit your needs
- Combine different functions to create more complex automations
