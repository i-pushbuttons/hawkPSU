import numpy as np
import streamlit as st
import pandas as pd
import time
from MatrixGeneration import generateMatrix
import math

# Placeholder for username and ranking
username = "User1"
ranking = "#1"

# Display username and ranking in a box at the top left
st.markdown(
    f"""
    <style>
    .user-info-box {{
        position: fixed;  /* Use fixed positioning to keep it in place */
        top: 60px;  /* Increase top position to ensure visibility */
        left: 20px;  /* Adjust left position to prevent overlap */
        background-color: #f0f0f0;
        border: 2px solid #C8E6C9;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Georgia', serif;
        z-index: 1000;  /* Ensure it is on top of other elements */
    }}
    .main-content {{
        margin-top: 50;  /* Add top margin to shift content down */
    }}
    </style>
    <div class="user-info-box">
        <strong>Username:</strong> {username}<br>
        <strong>Ranking:</strong> {ranking}
    </div>
    """,
    unsafe_allow_html=True
)

# Wrap the main content in a div with a top margin
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.title("Hawk *Matrix*")

if 'begin_pressed' not in st.session_state:
    st.session_state.begin_pressed = False
    st.session_state.num_rows = 2
    st.session_state.num_columns = 2
    st.session_state.difficulty = 'Easy'
    st.session_state.no_edit_matrix = None
    st.session_state.edit_matrix = None
    st.session_state.solved = False
    st.session_state.loop_count = 0
    st.session_state.start_time = None
    st.session_state.timer_duration = 180  # Default to 3 minutes for 'Easy'
    st.session_state.remaining_time = st.session_state.timer_duration
    st.session_state.score = 0

# Set timer duration based on difficulty
if st.session_state.difficulty == 'Easy':
    st.session_state.timer_duration = 180  # 3 minutes
elif st.session_state.difficulty == 'Medium':
    st.session_state.timer_duration = 240  # 4 minutes
elif st.session_state.difficulty == 'Hard':
    st.session_state.timer_duration = 300  # 5 minutes

if not st.session_state.begin_pressed:
    st.session_state.num_rows = st.number_input("How many rows?", step=1, value=st.session_state.num_rows)
    st.session_state.num_columns = st.number_input("How many columns?", step=1, value=st.session_state.num_columns)
    st.session_state.difficulty = st.selectbox("Select a difficulty:", ['Easy', 'Medium', 'Hard'], index=0)

    if st.button("Begin"):
        st.session_state.begin_pressed = True
        st.session_state.start_time = time.time()  # Record the start time

# Display the timer
timer_placeholder = st.empty()
if st.session_state.begin_pressed:
    elapsed_time = time.time() - st.session_state.start_time
    st.session_state.remaining_time = st.session_state.timer_duration - elapsed_time

    if st.session_state.remaining_time > 0:
        minutes, seconds = divmod(int(st.session_state.remaining_time), 60)
        timer_placeholder.subheader(f"Time Remaining: {minutes:02d}:{seconds:02d}")
    else:
        timer_placeholder.subheader("Time's up!")
        st.session_state.begin_pressed = False  # Stop the game when time is up

# Main execution of the Hawk Matrix UI
if st.session_state.begin_pressed and st.session_state.remaining_time > 0:
    if st.session_state.no_edit_matrix is None or st.session_state.edit_matrix is None:
        initial_matrix, x_sol = generateMatrix(st.session_state.num_rows, st.session_state.num_columns, st.session_state.difficulty)
        matrix_1 = pd.DataFrame(initial_matrix)
        
        st.session_state.no_edit_matrix = matrix_1.copy()  
        st.session_state.edit_matrix = matrix_1.copy()    
        st.session_state.x_sol = x_sol

    st.markdown(f"Row Operations: {st.session_state.loop_count}")

    st.markdown("The last column of the matrix is the y-column vector of the augmented matrix.")
    st.header("Matrix")
    st.dataframe(st.session_state.no_edit_matrix.style.format("{:.2f}"), hide_index=True) 

    st.header("Row-Operated Matrix")
    st.markdown("Edit each cell as you would if you were performing a single row operation to solve the augmented matrix. Hit submit when you are done inputing your operation.")
    # Allow floats in the edit_matrix
    edited_matrix = st.data_editor(st.session_state.edit_matrix.astype(float).style.format("{:.2f}"), hide_index=True)

    if not st.session_state.solved:
        if st.button("Submit"):
            st.session_state.loop_count += 1
            st.session_state.no_edit_matrix = edited_matrix.copy()  # Save the edited version
            st.session_state.edit_matrix = edited_matrix.copy()     # Sync both versions

            # Check if the solution is within a reasonable tolerance
            if np.allclose(st.session_state.edit_matrix.iloc[:, -1], st.session_state.x_sol, atol=0.1):
                st.session_state.solved = True

                # Calculate score
                base_score = 50  # Base score for easy difficulty
                scaling_factor = 60  # Adjust this factor to control the exponential growth
                time_bonus = int(math.exp(st.session_state.remaining_time / scaling_factor))  # Exponential time bonus
                difficulty_bonus = 0
                size_bonus = st.session_state.num_rows * st.session_state.num_columns  # Bonus based on matrix size

                if st.session_state.difficulty == 'Medium':
                    difficulty_bonus = 20
                elif st.session_state.difficulty == 'Hard':
                    difficulty_bonus = 50

                st.session_state.score = base_score + time_bonus + difficulty_bonus + size_bonus

                st.success(f"Congratulations, you solved the matrix in {st.session_state.loop_count} operations!")
                st.info(f"Your score: {st.session_state.score}")
            
            if not st.session_state.solved:
                st.session_state.submit_pressed = False
                st.rerun()    

st.markdown('</div>', unsafe_allow_html=True)
