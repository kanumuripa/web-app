import streamlit
import functions
# import PySimpleGUI

# PySimpleGUI.theme("BLACK")

tasks = functions.get_testdata()


def add_task():
    task = streamlit.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.wrt_testdata(tasks)


streamlit.title("TASKS TO DO")
streamlit.subheader("This is developed for Bhavya Sri :)")

for index, task in enumerate(tasks):
    checkbox = streamlit.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.wrt_testdata(tasks)
        del streamlit.session_state[task]
        streamlit.experimental_rerun()


streamlit.text_input(label="", placeholder="Add new task or "
                                           "to delete check the box beside task",
                     on_change=add_task, key="new_task")