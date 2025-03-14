import random
import streamlit as st

# TODO: Define the possible actions, e.g. words (rock, paper, scissors) or emojis (":rock:", ":newspaper:", ":scissors:")-
possible_actions = []


def evaluate_game(cmp_action, usr_action):
    # TODO: Evaluate what happens for each combination and print out the results. You can celebrate the user's victory
    #  with st.balloons(), for example
    if usr_action == cmp_action:
        pass
    elif usr_action == possible_actions[0] and cmp_action == possible_actions[1]:
        pass
    elif usr_action == possible_actions[1] and cmp_action == possible_actions[2]:
        pass
    elif usr_action == possible_actions[2] and cmp_action == possible_actions[0]:
        pass
    else:
        pass

def play_the_game():
    rps_form = st.form("rps")
    # TODO: Choose an input widget for the User Action, e.g. selectbox, radio, pills.
    user_action = rps_form.pills("Enter your choice!", possible_actions)
    if rps_form.form_submit_button("Play!"):
        computer_action = random.choice(possible_actions)   # Computer chooses action
        # TODO: Print out what the user and computer have selected.
        st.markdown("")
        evaluate_game(computer_action, user_action)


if __name__ == "__main__":
    play_the_game()
