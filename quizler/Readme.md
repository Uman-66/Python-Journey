# 🎮 Quizler – A True/False Trivia Game

Quizler is a Python-based trivia quiz application that delivers an engaging True/False question experience using a graphical user interface (GUI) powered by Tkinter. It fetches random questions from the Open Trivia Database API and challenges players to test their knowledge while tracking their score in real time.

## 🌟 Features

- **Dynamic Question Fetching**: Retrieves 10 random True/False questions from the Open Trivia DB API
- **Intuitive GUI**: Built with Tkinter, featuring a clean and responsive interface
- **Real-Time Score Tracking**: Displays the player's score in the top-right corner, updated after each answer
- **Visual Feedback**: The question canvas changes color to green for correct answers and red for incorrect ones
- **Game Completion**: Ends with a summary message when all questions are answered, disabling further input
- **Customizable Design**: Uses a consistent theme color (#375362) and custom button images for True (✅) and False (❌)

## 🛠️ Tech Stack

- **Python 3.8+**: Core programming language
- **Tkinter**: Python's standard library for creating the GUI
- **Requests**: Handles HTTP requests to fetch questions from the Open Trivia DB API
- **HTML**: Used for decoding HTML-encoded question text from the API
- **Open Trivia Database API**: Provides a free source of trivia questions

## 📂 Project Structure

```
quizler/
├── main.py               # Entry point: Initializes quiz logic and UI
├── question_model.py     # Defines the Question class for storing question text and answers
├── quiz_brain.py         # Manages quiz logic: question progression, scoring, and answer validation
├── ui.py                 # Implements the Tkinter-based GUI
├── data.py               # Fetches and processes question data from the API
├── tick.png              # Image for the "True" button
├── cross.png             # Image for the "False" button
├── README.md             # Project documentation (this file)
```

## 📋 Prerequisites

To run Quizler, ensure you have the following installed:

- Python 3.8+: [Download from python.org](https://python.org)
- Requests Library: For API calls
- Tkinter: Included with standard Python installations
- Image Files: Ensure `tick.png` and `cross.png` are in the project directory for the True/False buttons

## ▶️ Installation and Setup

Follow these steps to set up and run Quizler locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/quizler.git
   cd quizler
   ```

2. **Install Dependencies**:
   Install the requests library using pip:
   ```bash
   pip install requests
   ```

3. **Verify Image Files**:
   Ensure `tick.png` and `cross.png` are present in the project root directory. These images are used for the True and False buttons in the GUI.

4. **Run the Application**:
   Start the quiz by running the main script:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. Launch the application using `python main.py`
2. The GUI displays a trivia question in the center of a canvas
3. Click the ✅ **True** or ❌ **False** button to submit your answer
4. The canvas background turns green for correct answers or red for incorrect ones, with a 1-second delay before the next question
5. Your score is updated in real time in the top-right corner
6. After answering all 10 questions, the game ends with a message: "Sorry, you have reached the limit of the game"
7. The final score is displayed in the console as: "Your final score was: X/10"

## 🖼️ Screenshots

**Main Interface**
- Question Canvas: Displays the current question, centered with word-wrapping for long text
- Score Label: Shows the current score (e.g., "Score: 3") at the top-right
- True/False Buttons: Custom images (`tick.png` and `cross.png`) for intuitive interaction

**Feedback Mechanism**
- Correct Answer: Canvas turns green
- Incorrect Answer: Canvas turns red

## 🌐 API Details

Quizler uses the Open Trivia Database API to fetch questions. The API request is configured as follows:

- **Endpoint**: `https://opentdb.com/api.php`
- **Parameters**:
  - `amount=10`: Fetches 10 questions
  - `type=boolean`: Restricts questions to True/False format

**Example Request**:
```
https://opentdb.com/api.php?amount=10&type=boolean
```

**Response Handling**:
- Questions are decoded using the `html.unescape()` function to handle HTML-encoded characters (e.g., `&quot;` → `"`)
- The `results` field from the API response is used to populate the question bank

## 🧠 Code Breakdown

### 1. main.py
**Purpose**: Entry point of the application  
**Functionality**:
- Imports question data from `data.py`
- Creates a Question object for each API result and stores them in a `question_bank`
- Initializes the QuizBrain and QuizInterface classes
- Prints the final score to the console when the quiz ends

### 2. question_model.py
**Purpose**: Defines the Question class  
**Attributes**:
- `text`: The question text (string)
- `answer`: The correct answer ("True" or "False")

**Code**:
```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

### 3. quiz_brain.py
**Purpose**: Manages the quiz logic  
**Key Methods**:
- `__init__(q_list)`: Initializes the quiz with a list of questions, tracking `question_number` and `score`
- `still_has_question()`: Checks if more questions remain
- `next_question()`: Returns the next question text, decoded with `html.unescape()`
- `check_answer(user_answer)`: Compares the user's answer to the correct answer, increments the score if correct, and returns a boolean indicating correctness

### 4. ui.py
**Purpose**: Implements the Tkinter GUI  
**Key Components**:
- Window: Configured with a dark teal theme (#375362), padding, and title "Quizller"
- Canvas: Displays the question text, with a white background that changes to green/red for feedback
- Score Label: Updates dynamically with the current score
- Buttons: True (`tick.png`) and False (`cross.png`) buttons trigger `press_true` and `press_false` methods
- Feedback: Changes canvas color and delays 1 second before loading the next question

**Key Methods**:
- `get_next_question()`: Updates the canvas with the next question or displays the end message
- `press_true()` / `press_false()`: Submits the user's answer and triggers feedback
- `feedback(is_ok)`: Changes the canvas color based on answer correctness

### 5. data.py
**Purpose**: Fetches question data from the Open Trivia DB API  
**Functionality**:
- Sends a GET request with parameters `amount=10` and `type=boolean`
- Raises an exception for HTTP errors using `response.raise_for_status()`
- Extracts the `results` field from the JSON response

## 📌 Future Improvements

- **Difficulty Levels**: Add options for Easy, Medium, or Hard questions using the API's `difficulty` parameter
- **Multiple-Choice Support**: Extend the quiz to handle multiple-choice questions (`type=multiple`)
- **Category Selection**: Allow users to choose specific categories (e.g., Science, History) via the API's `category` parameter
- **High Score System**: Store high scores in a JSON file or SQLite database for persistence
- **Timer Feature**: Add a countdown timer for each question to increase challenge
- **Custom Styling**: Allow users to customize the theme color or button images
- **Sound Effects**: Add audio feedback for correct/incorrect answers

## 🐛 Known Issues

- **Image Dependency**: The app will raise an error if `tick.png` or `cross.png` is missing from the project directory
- **API Errors**: If the Open Trivia DB API is down or returns malformed data, the app may crash. Consider adding fallback questions
- **Long Questions**: Very long question text may not wrap perfectly in the canvas. Adjust the `width` parameter in `create_text` if needed

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the license terms.

## 🙌 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes and commit (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure your code follows PEP 8 style guidelines and includes appropriate comments.

## 📧 Contact

For questions or suggestions, reach out via GitHub Issues or open a discussion in the repository.

Happy quizzing! 🎉