import streamlit as st
import todo_functions

st.title("Todo App")
todos = todo_functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'].strip()
    if len(todo) > 0:
        todos.append(todo + "\n")
        todo_functions.write_todos(todos)

    st.session_state['new_todo'] = ''

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=idx)
    if checkbox:
        todos.pop(idx)
        todo_functions.write_todos(todos)
        del st.session_state[idx]
        st.rerun()

st.text_input(label=" ", placeholder="Add a new to do...",
              on_change=add_todo, key='new_todo')

# st.session_state