import streamlit as st

def countdown():
    """
    Displays a countdown from 10 to 1 and then prints "Liftoff!" using Streamlit.
    """
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        st.write(i)
    st.write("🚀 Liftoff!")

def main():
    st.title("🚀 Spaceship Countdown")
    
    if st.button("Start Countdown"):
        countdown()

if __name__ == '__main__':
    main()
