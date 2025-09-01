# Pomodoro Timer Application

![Pomodoro Timer](https://img.shields.io/badge/Python-3.x-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

A comprehensive Python-based Pomodoro timer application built with Tkinter that implements the famous Pomodoro Technique for enhanced productivity. This application helps you manage your work sessions and breaks effectively using a scientifically-proven time management method.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Customization](#customization)
7. [Technical Details](#technical-details)
8. [File Structure](#file-structure)
9. [Troubleshooting](#troubleshooting)
10. [The Pomodoro Technique](#the-pomodoro-technique)
11. [License](#license)

## Overview

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This application implements this technique with a beautiful graphical interface, visual progress tracking, and customizable timing options.

## Features

- **Automated Session Cycling**: Automatically transitions between work sessions and breaks
- **Visual Session Indicators**:
  - Green indicator for work sessions
  - Pink indicator for short breaks
  - Red indicator for long breaks
- **Progress Tracking**: Checkmark system to visualize completed work sessions
- **Responsive Design**: Clean, visually appealing interface with a tomato-themed design
- **Session Management**:
  - Start button to begin the timer
  - Reset button to stop and clear the current session
- **Audible Alerts**: (Potential enhancement) Can be extended with sound notifications

## Requirements

- **Python 3.6 or higher**: The application is built using Python 3
- **Tkinter**: Usually included with standard Python installations
- **PIL/Pillow** (optional): For enhanced image support if modifying the code

### Verification

To check if you have Python installed:
```bash
python --version
```

To verify Tkinter is available:
```bash
python -m tkinter
```

## Installation

### Step-by-Step Guide

1. **Download the Application**
   ```bash
   # Clone or download the source files
   git clone <repository-url>
   ```
   Or download the ZIP file and extract it to your preferred directory.

2. **Obtain the Tomato Image**
   - The application requires a tomato image named `pngwing.com.png`
   - Place this image in the same directory as the Python script
   - Alternatively, you can use any PNG image and update the filename in the code

3. **Verify Dependencies**
   - Ensure Python is properly installed
   - No additional packages are required beyond standard Python libraries

## Usage

### Starting the Application

1. Navigate to the application directory:
   ```bash
   cd pomodoro-timer
   ```

2. Run the application:
   ```bash
   python pomodoro_timer.py
   ```

### Interface Overview

- **Top Section**: Displays the current session type (Work/Break)
- **Center**: Tomato image with the countdown timer
- **Bottom Left**: Start button to begin the timer
- **Bottom Right**: Exit button to reset the timer
- **Bottom Center**: Progress checkmarks indicating completed work sessions

### Workflow

1. Click the "Start" button to begin your first work session
2. The timer will count down from 25 minutes (default)
3. When the work session ends, the application will:
   - Play a sound notification (if implemented)
   - Switch to a break session
   - Display a pink break indicator

4. After four completed work sessions, you'll get a longer break:
   - The break indicator will turn red
   - The timer will count down from 20 minutes (default)

5. The progress checkmarks below the timer show completed work sessions

6. At any time, you can click "Exit" to reset the timer to its initial state

## Customization

### Modifying Time Intervals

You can easily customize the timing intervals by modifying these constants at the top of the script:

```python
WORK_MIN = 25        # Duration of work sessions in minutes
SHORT_BREAK_MIN = 5  # Duration of short breaks in minutes
LONG_BREAK_MIN = 20  # Duration of long breaks in minutes
```

### Changing Colors and Styling

The application uses a predefined color scheme that can be modified:

```python
PINK = "#e2979c"     # Color for short breaks
RED = "#e7385b"      # Color for long breaks
GREEN = "#9bdeac"    # Color for work sessions
YELLOW = "#f7f5dd"   # Background color
FONT_NAME = "Courier"# Font family for text
```

### Adding Sound Notifications

To add sound notifications, you could extend the code with:

```python
# Add to the start of the file
import winsound  # Windows only
# Or use a cross-platform solution like pygame.mixer

# Add to the countdown function where sessions change
def play_sound():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000   # Set duration to 1000 ms = 1 second
    winsound.Beep(frequency, duration)
```

## Technical Details

### Application Structure

The application follows a procedural programming paradigm with global variables to maintain state. Key components include:

1. **Main Window**: Tkinter root window with configured styling
2. **Labels**: For displaying session information and progress
3. **Canvas**: For displaying the tomato image and timer text
4. **Buttons**: For user interaction (start and reset)
5. **Timer Mechanism**: Uses Tkinter's `after()` method for the countdown functionality

### Key Functions

- `reset_timer()`: Stops the timer and resets all values to initial state
- `start_timer()`: Initiates the timer based on the current session type
- `countdown(count)`: Handles the countdown logic and session transitions

### Session Management

The application uses a repetition counter (`reps`) to track the current session:
- Odd repetitions: Work sessions
- Even repetitions: Break sessions
- Every 8th repetition: Long break session

## File Structure

```
pomodoro-timer/
│
├── pomodoro_timer.py    # Main application script
├── pngwing.com.png      # Tomato image (must be provided by user)
├── README.md            # This documentation file
└── (optional sound files for enhancements)
```

## Troubleshooting

### Common Issues

1. **Image not found error**
   - Solution: Ensure `pngwing.com.png` is in the same directory as the script
   - Alternative: Modify the filename in the code to match your image file

2. **Tkinter not available**
   - On Linux: Install with `sudo apt-get install python3-tk`
   - On Mac: Usually included with Python installations
   - On Windows: Usually included with Python installations

3. **Window appears too large or small**
   - Solution: Adjust the `width` and `height` parameters in the Canvas initialization

4. **Timer doesn't start**
   - Solution: Check if another instance of the timer is running in the background

### Performance Considerations

- The application uses minimal system resources
- The timer mechanism is efficient, using Tkinter's event system
- For extended use, the application remains stable

## The Pomodoro Technique

### Background

The Pomodoro Technique was developed by Francesco Cirillo in the late 1980s. The method involves using a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a "pomodoro", from the Italian word for 'tomato', after the tomato-shaped kitchen timer Cirillo used as a university student.

### Benefits

1. **Reduces Mental Fatigue**: Regular breaks prevent burnout
2. **Maintains Focus**: Time-boxed work sessions encourage concentration
3. **Increases Awareness**: Helps track time spent on tasks
4. **Improves Planning**: Encourages estimation of effort required for tasks
5. **Enhances Motivation**: Small victories from completing pomodoros

### Standard Workflow

1. Choose a task to be accomplished
2. Set the Pomodoro timer to 25 minutes
3. Work on the task until the timer rings
4. Take a short break (5 minutes)
5. After four pomodoros, take a longer break (15-20 minutes)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Francesco Cirillo for developing the Pomodoro Technique
- The Python community for excellent documentation and resources
- Tkinter developers for maintaining a robust GUI library

## Support

For questions, issues, or contributions:
1. Check the troubleshooting section above
2. Search for similar issues in the GitHub repository
3. Create a new issue with details about your problem

---

**Happy Productive Time!** 🍅