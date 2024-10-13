import numpy as np
import streamlit as st
import pandas as pd
from MatrixGeneration import generateMatrix

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

if not st.session_state.begin_pressed:
    st.session_state.num_rows = st.number_input("How many rows?", step=1, value=st.session_state.num_rows)
    st.session_state.num_columns = st.number_input("How many columns?", step=1, value=st.session_state.num_columns)
    st.session_state.difficulty = st.selectbox("Select a difficulty:", ['Easy', 'Medium', 'Hard'], index=0)

    if st.button("Begin"):
        st.session_state.begin_pressed = True

#Thus begins the main execution of the Hawk Matrix UI
if st.session_state.begin_pressed:
    if st.session_state.no_edit_matrix is None or st.session_state.edit_matrix is None:
        initial_matrix, x_sol = generateMatrix(st.session_state.num_rows, st.session_state.num_columns, st.session_state.difficulty)
        matrix_1 = pd.DataFrame(initial_matrix)
        
        st.session_state.no_edit_matrix = matrix_1.copy()  
        st.session_state.edit_matrix = matrix_1.copy()    
        st.session_state.x_sol = x_sol

    st.markdown(f"Row Operations: {st.session_state.loop_count}")

    st.header("Matrix")
    st.dataframe(st.session_state.no_edit_matrix, hide_index=True) 

    st.header("Row-Operated Matrix")
    
    edited_matrix = st.data_editor(st.session_state.edit_matrix, hide_index=True)

    if not st.session_state.solved:
        
        if st.button("Submit"):
            st.session_state.loop_count += 1
            st.session_state.no_edit_matrix = edited_matrix.copy()  # Save the edited version
            st.session_state.edit_matrix = edited_matrix.copy()     # Sync both versions

            if(np.array_equal(st.session_state.edit_matrix.iloc[:,-1], st.session_state.x_sol)):
                st.session_state.solved = True
                st.success(f"Congratulations, you solved the matrix in {st.session_state.loop_count} operations!")
            
            if not st.session_state.solved:
                st.session_state.submit_pressed = False
                st.rerun()    
        


