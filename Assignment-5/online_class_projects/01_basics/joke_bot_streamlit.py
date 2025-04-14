import streamlit as st

# Constants
PROMPT = "What do you want?"
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

# Set up the Streamlit app
st.title("Joke Bot")
st.write(PROMPT)

# Create an input field for the user
user_input = st.text_input("", key="user_input")

# Create a button to submit the input
if st.button("Submit"):
    if user_input == "Joke":
        st.success(JOKE)
    else:
        st.error(SORRY)

# Add instructions
st.markdown("---")
st.markdown("**Instructions:** Type 'Joke' and click Submit to hear a joke!")