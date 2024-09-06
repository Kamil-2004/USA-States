import pandas as pd
import turtle

# Load the CSV file
states_df = pd.read_csv("C:/Users/PMYLS/Pictures/50_states.csv")

# Extract the list of states
all_states = states_df['state'].tolist()

# Initialize guessed states list
guessed_states = []

# Setup the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("C:/Users/PMYLS/Downloads/blank_states_img.gif")

# Setup the turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# Main game loop
while len(guessed_states) < 50:
    # Prompt user to guess a state
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess the state's name:")

    if guess:
        guess = guess.title()
    else:
        print("You didn't enter any text, try again!")
        continue

    # Check if the guessed state is correct m,
        guessed_states.append(guess)
        state_data = states_df[states_df.state == guess]
        writer.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        writer.write(guess)

# Identify missing states
missing_states = [state for state in all_states if state not in guessed_states]

# Save missing states to CSV
missing_df = pd.DataFrame(missing_states, columns=["state"])
missing_df.to_csv("C:/Users/PMYLS/Pictures/missing_states.csv", index=False)

# Save guessed states to CSV
guessed_df = pd.DataFrame(guessed_states, columns=["state"])
guessed_df.to_csv("C:/Users/PMYLS/Pictures/guessed_states.csv", index=False)

# End the turtle graphics
screen.bye()
