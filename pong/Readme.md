# Pong Game

A classic Pong game implemented in Python using the Turtle graphics library. This game features two paddles, a bouncing ball, and a scoring system.

## Features

- **Two-player gameplay**: One player controls the left paddle (W/S keys), the other controls the right paddle (Up/Down arrow keys)
- **Realistic ball physics**: The ball bounces off walls and paddles with appropriate angles
- **Score tracking**: Keeps track of each player's score
- **Adjustable game speed**: The ball's speed increases as the game progresses

## Requirements

- Python 3.x
- Turtle module (comes standard with Python)

## How to Play

1. Run the `main.py` file to start the game
2. Player 1 (left side) uses:
   - W key to move paddle up
   - S key to move paddle down
3. Player 2 (right side) uses:
   - Up arrow key to move paddle up
   - Down arrow key to move paddle down
4. Score points by getting the ball past your opponent's paddle
5. The first player to reach the winning score wins the game

## Project Structure

The game consists of several modules:

- `main.py`: Main game loop and logic
- `pad.py`: Paddle class implementation
- `ball.py`: Ball class with movement and collision detection
- `score.py`: Score tracking and display

## Game Mechanics

- The ball speeds up slightly after each paddle hit
- The ball resets to the center after each point scored
- The ball bounces at different angles depending on where it hits the paddle

Enjoy this classic arcade game challenge!