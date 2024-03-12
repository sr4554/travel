import streamlit as st
import Projects, Contact  # Import your pages

# Page configuration
st.set_page_config(
    page_title="Multipage App",
    page_icon=""
)

# Sidebar navigation
selected_page = st.sidebar.selectbox("Select a page", ["Homepage", "Projects", "Contact"])

# Conditional rendering
if selected_page == "Homepage":
    st.title("Main Page")
    st.sidebar.success("Select a page above.")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Input a text here", st.session_state["my_input"])
    submit = st.button("Submit")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered: ", my_input)

elif selected_page == "Projects":
    projects.run()  # Call the function from projects.py

elif selected_page == "Contact":
    contact.run()  # Call the function from contact.py

