import streamlit as st
import pandas as pd
from services.students import list_students, add_student


def render():
    st.title("LTL Pathfinder (Basic)")

    st.subheader("Add Student")

    col1, col2 = st.columns(2)
    first = col1.text_input("First name")
    last = col2.text_input("Last name")

    col3, col4 = st.columns(2)
    school = col3.text_input("School")
    grade = col4.text_input("Grade")

    if st.button("Save Student"):
        if not first.strip() or not last.strip():
            st.error("First and last name required")
        else:
            add_student(first, last, school, grade)
            st.success("Student saved")
            st.rerun()

    st.divider()
    st.subheader("Students")

    students = list_students()

    if not students:
        st.info("No students yet")
        return

    df = pd.DataFrame(students)
    st.dataframe(df, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    render()
