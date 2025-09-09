# U.S. States Geography Game

An interactive educational application that helps users learn and memorize all 50 U.S. states through an engaging visual quiz game.

## Overview

This Python-based game challenges players to identify all 50 U.S. states on a blank map. The program uses Turtle graphics for visualization and pandas for data management, creating an effective learning tool for geography students, teachers, or anyone interested in improving their knowledge of U.S. states.

## Features

### Core Gameplay
- **Interactive Map Interface**: Visual display of the United States with state boundaries
- **Progressive Scoring System**: Real-time tracking of correctly identified states (X/50)
- **Case-Insensitive Input**: Automatically formats user input to proper case for matching
- **Visual Feedback**: Correctly identified states are labeled directly on the map

### Educational Components
- **State Coordinate Accuracy**: Precisely places state names at their geographic centers using coordinate data
- **Learning Reinforcement**: Immediate visual confirmation when a state is correctly identified
- **Customizable Exit**: Players can end the game at any time by typing "Exit"

### Data Management
- **Automated Progress Tracking**: The game monitors which states have been successfully identified
- **Personalized Learning Report**: Generates a customized CSV file listing states the player needs to study
- **Data Persistence**: Learning progress is saved between sessions via the generated CSV file

## Technical Requirements

### Software Dependencies
- Python 3.x (compatible with most recent versions)
- pandas library (`pip install pandas`)
- Standard Python modules: turtle, pandas

### Data Files
- `blank_states_img.gif`: Blank map of the United States with state boundaries
- `50_states.csv`: Database containing state names and their precise map coordinates
- `need_to_learn.csv`: Generated file containing states the player hasn't mastered (created upon exit)

## Installation & Setup

1. **Install Python**: Download and install Python 3.x from [python.org](https://python.org)
2. **Install pandas**: Open a terminal/command prompt and run:
   ```
   pip install pandas
   ```
3. **Download Game Files**: Ensure all game files are in the same directory:
   - Main Python script
   - `blank_states_img.gif`
   - `50_states.csv`

## How to Play

1. **Launch the Game**: Run the Python script in your preferred environment
2. **Game Interface**: A blank U.S. map will appear with a prompt dialog
3. **Enter State Names**: Type the name of any U.S. state when prompted
4. **Progress Tracking**: The title bar shows your current score (e.g., "15/50 States guessed correct")
5. **Completion**: Continue until you've identified all 50 states or type "Exit" to end early

## Educational Value

### For Students
- Reinforces geographic knowledge through active recall
- Provides visual-spatial learning of state locations
- Creates personalized study materials based on individual learning needs

### For Teachers
- Can be used as a classroom activity or assessment tool
- Generates customized review materials for each student
- Encourages self-paced learning and improvement

### Learning Methodology
The game employs effective learning techniques including:
- Active recall (retrieving information from memory)
- Spaced repetition (through multiple gameplay sessions)
- Visual mapping (associating names with spatial locations)
- Immediate feedback (correct answers are confirmed visually)

## The "Need to Learn" Feature

### Purpose
The game automatically generates a `need_to_learn.csv` file when you exit, containing only the states you haven't successfully identified during your session.

### Implementation
- The program compares your guessed states against the complete list of 50 states
- Any states not correctly identified are compiled into a customized list
- This list is exported to a CSV file for future reference and focused study

### How to Use for Effective Studying
1. After playing, open the `need_to_learn.csv` file
2. Use this list as a targeted study guide for your next session
3. Focus your preparation on these specific states
4. Repeat the game until no states remain in your "need to learn" list

### File Format
The CSV file contains a single column with the header "0" and each row containing the name of a state that needs further study.

## Customization Options

### Difficulty Adjustment
- Modify the font size in the `marker.write()` function for easier/harder visibility
- Adjust coordinate values in `50_states.csv` for precise label placement

### Extended Features
Advanced users can extend the game by:
- Adding capital cities to the learning objectives
- Implementing a timer for speed challenges
- Creating different game modes (region-specific quizzes)
- Adding sound effects for correct/incorrect answers
