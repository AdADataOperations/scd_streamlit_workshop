import random
import streamlit as st

possible_actions = [":rock:", ":newspaper:", ":scissors:"]


def evaluate_game(cmp_action, usr_action):
    if usr_action == cmp_action:
        st.markdown("tied")
    elif usr_action == possible_actions[0] and cmp_action == possible_actions[1]:
        st.markdown("computer wins!")
        return "cmp"
    elif usr_action == possible_actions[1] and cmp_action == possible_actions[2]:
        st.markdown("computer wins!")
        return "cmp"
    elif usr_action == possible_actions[2] and cmp_action == possible_actions[1]:
        st.markdown("computer wins!")
        return "cmp"
    else:
        st.markdown("You win!")
        st.balloons()
        return "usr"


def play_the_game():
    rps_form = st.form("rps")
    user_action = rps_form.pills("Enter your choice!", [":rock:", ":newspaper:", ":scissors:"])
    if rps_form.form_submit_button("Play!"):
        computer_action = random.choice(possible_actions)   # Der Computer wählt ein Element.
        st.markdown(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        evaluate_game(computer_action, user_action)


if __name__ == "__main__":
    play_the_game()
