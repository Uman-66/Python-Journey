# Flashcard Language Learning App

## Overview

A professional language learning application built with Python and Tkinter that uses a spaced repetition system to help users memorize vocabulary. The app displays French words and phrases, then reveals their English translations after a brief interval, allowing users to actively recall meanings before seeing the answers.

## Features

### Core Functionality
- **Dual-language Flashcards**: Displays French vocabulary with English translations
- **Automatic Card Flipping**: Cards automatically flip after 3 seconds to reveal translations
- **Progress Tracking**: Removes known words from the learning deck and saves progress
- **Persistent Learning**: Progress is saved to CSV files for continued learning across sessions
- **Randomized Learning**: Presents cards in random order for effective memorization

### User Interface
- **Clean, Modern Design**: Uses a color-coded system (purple for questions, green for answers)
- **Intuitive Controls**: Simple two-button interface for known/unknown responses
- **Visual Feedback**: Color changes and text formatting enhance learning experience
- **Responsive Design**: Properly sized elements with comfortable padding and spacing

### Data Management
- **CSV Integration**: Uses pandas for efficient data handling
- **Fallback System**: Automatically uses the original dataset if progress file doesn't exist
- **Efficient Storage**: Only saves words that still need to be learned

## System Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- pandas library
- 10MB free disk space

## Installation

1. Ensure Python is installed on your system
2. Install required dependencies:
   ```
   pip install pandas
   ```
3. Prepare the following files in your project directory:
   - `purple.png` - Front card background image
   - `green.png` - Back card background image (note: code expects "greem.png" - consider renaming)
   - `cross.png` - Unknown button icon
   - `tick.png` - Known button icon
   - `Untitled spreadsheet - Sheet1.csv` - Initial vocabulary data with "French" and "English" columns

## Usage

### Starting the Application
Run the Python script to launch the flashcard application:
```
python flashcard_app.py
```

### Learning Process
1. The app displays a French word or phrase on a purple card
2. After 3 seconds, the card automatically flips to reveal the English translation on a green background
3. Users can:
   - Click the green checkmark (✓) if they knew the translation (card is removed from deck)
   - Click the red cross (✗) if they didn't know the translation (card remains in deck)
4. The app automatically progresses to the next card after each response

### Data Files
- **Initial Data**: `Untitled spreadsheet - Sheet1.csv` contains the complete vocabulary set
- **Progress Data**: `to_learn.csv` is automatically created and updated with remaining words to learn

## Customization

### Modifying Vocabulary
Edit the CSV file to add or change vocabulary:
- Ensure the file has "French" and "English" columns
- Maintain proper CSV formatting

### Adjusting Timing
Change the flip delay by modifying the timer value in the code:
```python
timer = window.after(3000, func = flip_card)  # Change 3000 to desired milliseconds
```

### Custom Styling
Modify these constants in the code:
- `BACKGROUND_COLOR`: Change the app background color
- Font styles and sizes in the `canvas.create_text()` calls
- Image files for different visual themes

## Technical Architecture

### Components
1. **Main Window**: Tkinter root window with configured styling
2. **Canvas**: Displays card images and text elements
3. **Image Assets**: Front/back card backgrounds and button icons
4. **Data Handler**: pandas CSV reader/writer for vocabulary management
5. **Timer System**: Controls automatic card flipping

### Key Functions
- `next_card()`: Selects and displays a new random card
- `flip_card()`: Reveals the translation side of the card
- `is_known()`: Handles known words and updates progress

## Troubleshooting

### Common Issues
1. **Missing Image Files**: Ensure all PNG files are in the project directory
2. **CSV Format Problems**: Verify CSV has correct "French" and "English" column headers
3. **Module Import Errors**: Install missing packages using pip

### Debug Mode
Add print statements to track application flow:
```python
print(f"Current card: {current_card}")
print(f"Remaining cards: {len(learn)}")
```

## Extension Possibilities

### Potential Enhancements
1. **Audio Support**: Add pronunciation guides for words
2. **Categories**: Implement vocabulary categories or difficulty levels
3. **Progress Statistics**: Add tracking of learning metrics and performance history
4. **Multiple Language Support**: Expand beyond French-English pairs
5. **Cloud Sync**: Save progress across multiple devices
6. **Custom Study Sessions**: Allow users to select specific word sets

## Contributing

To extend this application:
1. Fork the repository
2. Create a feature branch
3. Implement changes with appropriate comments
4. Test thoroughly with different datasets
5. Submit a pull request with description of enhancements

## License

This project is open source and available under the MIT License.

## Support

For technical support or questions:
1. Check file paths and names match expected values
2. Verify CSV formatting meets requirements
3. Ensure all dependencies are properly installed

---

This application effectively combines principles of spaced repetition and active recall to optimize language vocabulary acquisition. The simple interface focuses attention on learning while the systematic progress tracking ensures efficient study sessions.