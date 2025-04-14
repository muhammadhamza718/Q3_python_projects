import streamlit as st
import random

# Constants
N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

# Streamlit UI
st.title("Random Number Generator")
st.write(f"Generating {N_NUMBERS} random numbers between {MIN_VALUE} and {MAX_VALUE}:")

# Generate and display numbers
random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
st.write(random_numbers)

# Button to generate new numbers
if st.button("Generate Again"):
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    st.write(random_numbers)

# For Terminal based output

# import random

# N_NUMBERS = 10
# MIN_VALUE = 1
# MAX_VALUE = 100

# def main():
#     """Generates and prints 10 random numbers between 1 and 100."""
#     for _ in range(N_NUMBERS):
#         print(random.randint(MIN_VALUE, MAX_VALUE))

# if __name__ == '__main__':
#     main()
