import streamlit as st
import random

def main():
    st.title("🔢 Guess My Number Game!")
    st.write("I am thinking of a number between **1 and 99**. Can you guess it?")

    # Initialize session state for secret number and game status
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 99)
        st.session_state.game_over = False

    # User input for guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=99, step=1)

    if st.button("Submit Guess"):
        if not st.session_state.game_over:
            if guess < st.session_state.secret_number:
                st.warning("Your guess is **too low**! Try again.")
            elif guess > st.session_state.secret_number:
                st.warning("Your guess is **too high**! Try again.")
            else:
                st.write(f"🎉 Congrats! The number was **{st.session_state.secret_number}**.")
                st.session_state.game_over = True  # Mark game as finished

    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 99)
            st.session_state.game_over = False
            st.rerun()

if __name__ == '__main__':
    main()
