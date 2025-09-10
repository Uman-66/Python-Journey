# Kanye Quote App - Professional README

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![API](https://img.shields.io/badge/API-Kanye.rest-orange)

A sleek desktop application that displays random quotes from Kanye West, built with Python and Tkinter.

## Features

- **Real-time Quotes**: Fetches authentic Kanye West quotes from the official Kanye REST API
- **Responsive Design**: Automatically wraps text to ensure quotes stay within the application boundaries
- **Visually Appealing**: Clean UI with Kanye's image and a themed background
- **One-Click Operation**: Get a new quote with a single click on Kanye's image
- **Cross-Platform**: Works on Windows, macOS, and Linux systems

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Steps
1. Clone or download the project files
2. Navigate to the project directory
3. Install required dependencies:
   ```bash
   pip install requests
   ```
4. Ensure you have the following files in your project directory:
   - `main.py` (the Python script)
   - `background.png` (UI background image)
   - `kanye.png` (button image)

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. The application window will open with an initial Kanye quote
3. Click on Kanye's image to fetch a new random quote
4. The text will automatically adjust to fit within the UI boundaries

## Technical Details

### Code Structure
- **get_quote()**: Fetches data from the Kanye REST API
- **wrap_text()**: Handles text wrapping to prevent overflow
- **button_click()**: Event handler for the button click
- **Tkinter GUI**: Creates and manages the application window

### API Integration
The application uses the [Kanye.rest API](https://kanye.rest/) to fetch quotes:
- Endpoint: `https://api.kanye.rest/`
- Method: GET
- Response: JSON with a "quote" field

### UI Components
- Main Window: 300x414 pixels with padding
- Canvas: Displays background image and quote text
- Button: Kanye's image that triggers new quote generation
- Text: Automatically wrapped with white color for contrast

## Customization

You can customize the application by:
- Modifying the font size and style in the `canvas.create_text()` call
- Adjusting the text width parameter to change wrapping behavior
- Replacing the image files with your own (maintain same dimensions for best results)
- Changing the color scheme by modifying the `fill` parameter

## Troubleshooting

### Common Issues
1. **Missing module error**: Run `pip install requests` to install the required package
2. **Image not found**: Ensure `background.png` and `kanye.png` are in the same directory as the script
3. **Text still overflowing**: Adjust the `width` parameter in the `canvas.create_text()` call

### API Limitations
- The application requires an internet connection to fetch new quotes
- If the API is unavailable, the application will display an error

## Future Enhancements

Potential improvements for the application:
- Add quote sharing functionality
- Implement a history of previous quotes
- Add animation when displaying new quotes
- Include error handling for API connectivity issues
- Add a loading indicator while fetching quotes


## Contributing

This project is for educational purposes. The Kanye REST API is provided for free by [kanye.rest](https://kanye.rest/
Contributions to improve the application are welcome. Please ensure:
- Code follows PEP 8 guidelines
- New features don't break existing functionality
- Appropriate error handling is included

## Support

For questions or issues with this application, please check:
1. The troubleshooting section above
2. Python and Tkinter documentation
3. The Kanye.rest API status

---

*This application is not officially affiliated with Kanye West. It uses a public API to display quotes attributed to him.*