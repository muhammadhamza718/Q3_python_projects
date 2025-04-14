import streamlit as st
import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    st.title("🎲 Random Number Generator")
    st.write(f"Generating **{N_NUMBERS}** random numbers between **{MIN_VALUE} and {MAX_VALUE}**.")

    if st.button("Generate Numbers"):
        random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
        st.write("### 🔢 Random Numbers:")
        for num in random_numbers:
            st.write(num)

if __name__ == '__main__':
    main()
