import streamlit as st
import random

st.title("Guess the Number Game")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)

guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if guess < st.session_state.number:
        st.write("Try a higher number!")
    elif guess > st.session_state.number:
        st.write("Try a lower number!")
    else:
        st.success("Correct! You guessed the number!")
        st.balloons()
        st.session_state.number = random.randint(1, 100)  # Reset for new game
