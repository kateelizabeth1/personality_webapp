import streamlit as st  # Streamlit is the library that turns Python into a web app

# ---------- SETTINGS ----------
# Change this one word to change the whole quiz topic!
QUIZ_TOPIC = "Dessert"

# This sets the browser tab title and little tab icon.
# It must be the FIRST Streamlit command in the file.
st.set_page_config(
    page_title=f"Which {QUIZ_TOPIC} Are You?",
    page_icon="🧁",
)

# ---------- TITLE AND WELCOME ----------
st.title(f"✨ Which {QUIZ_TOPIC} Are You? 🧁")
st.write("Welcome, sweet soul! 🌸 Answer a few dreamy questions and discover your true match. 💖")

# A text box where the user types their name
name = st.text_input("What's your name? 💌")

# A button to begin the quiz
if st.button("Start the quiz 🌈"):
    # .strip() removes spaces, so a name made of only spaces counts as empty
    if name.strip() == "":
        st.warning("Please tell me your name first! 🥺")
    else:
        st.success(f"Hi {name}! 🎀 Get ready, the questions are coming soon...")
