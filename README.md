# U.S. States Game

A simple geography-based game where the user is prompted to guess the names of U.S. states. The game continues until all 50 states have been correctly guessed.

## Requirements

* Python 3.x
* pandas library
* turtle graphics library

## Installation

1. Install the required libraries by running `pip install pandas` in your terminal/command prompt.
2. Clone or download the repository to your local machine.
3. Make sure the `50_states.csv` file is in the same directory as the game script.
4. Replace the file paths in the script with the actual paths to the `50_states.csv` file and the `blank_states_img.gif` image on your machine.

## Usage

1. Run the game script using Python (e.g., `python game.py`).
2. Follow the on-screen prompts to guess the names of U.S. states.
3. The game will display the correct answers on a map of the United States.
4. Once all 50 states have been correctly guessed, the game will end and save the guessed states and missing states to separate CSV files.

## Files

* `game.py`: The main game script.
* `50_states.csv`: A CSV file containing the names and coordinates of the 50 U.S. states.
* `blank_states_img.gif`: A GIF image of a blank U.S. map.
* `missing_states.csv`: A CSV file containing the names of states that were not guessed correctly.
* `guessed_states.csv`: A CSV file containing the names of states that were guessed correctly.

## Notes

* The game uses a simple text-based input system, so be sure to enter your guesses correctly (e.g., "California" instead of "california").
* The game will not end until all 50 states have been correctly guessed, so be prepared to spend some time playing!
