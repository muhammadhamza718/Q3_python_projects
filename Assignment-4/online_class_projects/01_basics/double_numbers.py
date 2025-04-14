import streamlit as st

def double_until_threshold(start_value):
    """
    Doubles the given number repeatedly until it reaches or exceeds 100.
    Displays all intermediate values using Streamlit.
    """
    curr_value = start_value * 2  # Start doubling
    results = []  # Store results for display

    while curr_value < 100:
        results.append(curr_value)  # Store current value
        curr_value *= 2  # Double the value

    return results

def main():
    st.title("Double a Number Until It Reaches 100")  # App title
    
    # Get user input
    start_value = st.number_input("Enter a number:", min_value=1, value=2, step=1)

    if st.button("Start Doubling"):
        results = double_until_threshold(start_value)
        st.write("Doubled values:")
        for value in results:
            st.write(value)  # Display each doubled value

if __name__ == '__main__':
    main()
