import streamlit as st  # Streamlit is the library that turns Python into a web app

# ---------- SETTINGS ----------
# Change this one word to change the whole quiz topic!
QUIZ_TOPIC = "Dessert"

# The list of possible results. Keep these names the SAME as in the questions!
DESSERTS = ["Cupcake", "Ice Cream", "Macaron", "Brownie", "Donut"]

# This sets the browser tab title and little tab icon.
# It must be the FIRST Streamlit command in the file.
st.set_page_config(
    page_title=f"Which {QUIZ_TOPIC} Are You?",
    page_icon="🧁",
)

# ---------- TITLE AND WELCOME ----------
st.title(f"✨ Which {QUIZ_TOPIC} Are You? 🧁")
st.write("Hello! Answer a few questions and discover your sweet match. 💖")

# A text box where the user types their name
name = st.text_input("What's your name? 💌")

# A button to begin the quiz
if st.button("Start the quiz 🌈"):
    # .strip() removes spaces, so a name made of only spaces counts as empty
    if name.strip() == "":
        st.warning("Please input your name first! ")
    else:
        st.success(f"Hi {name}! 🎀 Get ready, the questions are coming soon...")
import random  # random lets us shuffle things
import streamlit as st  # Streamlit turns Python into a web app

# ---------- SETTINGS ----------
QUIZ_TOPIC = "Dessert"

st.set_page_config(
    page_title=f"Which {QUIZ_TOPIC} Are You?",
    page_icon="🧁",
)

# ---------- THE QUESTIONS ----------
# A list [] of dictionaries {}. Each dictionary is one question.
# "options" maps each answer text -> the dessert that answer points to.
# The user only sees the answer text. The dessert names stay hidden!
# The 5 desserts: Cupcake, Ice Cream, Macaron, Brownie, Donut.
# Tip: every question should give each dessert exactly one answer.
QUESTIONS = [
    {
        "question": "Pick a random superpower ⚡",
        "options": {
            "Making everyone around you instantly happy 🥰": "Cupcake",
            "Teleporting anywhere you want 🌍": "Ice Cream",
            "Turning anything into beautiful art 🎨": "Macaron",
            "Pausing time so you can nap 😴": "Brownie",
            "Making a party appear out of nowhere 🎉": "Donut",
        },
    },
    {
        "question": "What's hiding at the bottom of your bag? 🎒",
        "options": {
            "A lip balm and a tiny mirror 💄": "Cupcake",
            "A water bottle and sunglasses 😎": "Ice Cream",
            "A sketchbook and fancy pens ✏️": "Macaron",
            "A cosy hoodie and earphones 🎧": "Brownie",
            "Mystery snacks and 7 receipts 🧾": "Donut",
        },
    },
    {
        "question": "Choose a type of weather ☁️",
        "options": {
            "A soft pink-sky evening 🌸": "Cupcake",
            "A hot, sunny day ☀️": "Ice Cream",
            "A light drizzle in a pretty city 🌦️": "Macaron",
            "A big stormy night with thunder ⛈️": "Brownie",
            "Whatever, I'm chaotic in all weather 🌪️": "Donut",
        },
    },
    {
        "question": "Pick an emoji 😍",
        "options": {
            "🥹": "Cupcake",
            "😎": "Ice Cream",
            "✨": "Macaron",
            "😌": "Brownie",
            "🤪": "Donut",
        },
    },
    {
        "question": "What's your sleep schedule like? 🌙",
        "options": {
            "Early bed, cute pyjamas 🎀": "Cupcake",
            "Different every day, I go with the flow 🌊": "Ice Cream",
            "Late nights, because inspiration strikes 💡": "Macaron",
            "I LOVE sleeping, it's my hobby 🛌": "Brownie",
            "Sleep? I'll sleep when I'm older 🦉": "Donut",
        },
    },
    {
        "question": "Choose a music vibe 🎵",
        "options": {
            "Bubblegum pop 🍬": "Cupcake",
            "Summer road trip playlist 🚗": "Ice Cream",
            "Dreamy lo-fi and jazz ☕": "Macaron",
            "Soft acoustic and rainy-day songs 🌧️": "Brownie",
            "Anything I can dance badly to 💃": "Donut",
        },
    },
    {
        "question": "Pick a pair of shoes 👟",
        "options": {
            "Sparkly pink sneakers 💖": "Cupcake",
            "Comfy sandals ☀️": "Ice Cream",
            "Vintage loafers with cute socks 🧦": "Macaron",
            "Fuzzy slippers, always 🥿": "Brownie",
            "One red shoe and one blue shoe 🤷": "Donut",
        },
    },
    {
        "question": "Surprise! You have a free day. You... 🎁",
        "options": {
            "Bake or craft something for a friend 🧁": "Cupcake",
            "Go on a spontaneous adventure 🗺️": "Ice Cream",
            "Visit a café or museum alone 🖼️": "Macaron",
            "Stay home, blanket on, no plans 🧸": "Brownie",
            "Invite everyone over, instant hangout 🥳": "Donut",
        },
    },
    {
        "question": "Choose a flower 🌷",
        "options": {
            "A pink peony 🌸": "Cupcake",
            "A sunflower 🌻": "Ice Cream",
            "A lavender sprig 💜": "Macaron",
            "A deep red rose 🌹": "Brownie",
            "A daisy that grew through the pavement 🌼": "Donut",
        },
    },
    {
        "question": "What's your texting style? 📱",
        "options": {
            "Lots of hearts and kind words 💌": "Cupcake",
            "Quick replies, then I'm outside 🏃": "Ice Cream",
            "Short, thoughtful, and aesthetic 🤍": "Macaron",
            "Slow replies, but deep chats 🫶": "Brownie",
            "Voice notes, memes and 12 messages in a row 😂": "Donut",
        },
    },
    {
        "question": "Pick a way to travel 🚲",
        "options": {
            "A bike with a flower basket 🧺": "Cupcake",
            "A convertible with the top down 🏎️": "Ice Cream",
            "A vintage tram through a pretty town 🚋": "Macaron",
            "A train with a window seat and a book 🚂": "Brownie",
            "A skateboard, no helmet (don't copy me) 🛹": "Donut",
        },
    },
    {
        "question": "Choose a houseplant 🪴",
        "options": {
            "A tiny pink cactus 🌵": "Cupcake",
            "A palm tree 🌴": "Ice Cream",
            "An elegant orchid 🌺": "Macaron",
            "A big, cosy-looking fern 🌿": "Brownie",
            "Whatever survived my last three attempts 🥲": "Donut",
        },
    },
    {
        "question": "Which app is your most-used app? 📲",
        "options": {
            "Camera, for cute photos 📸": "Cupcake",
            "Maps, always exploring 📍": "Ice Cream",
            "Pinterest, for aesthetic ideas 📌": "Macaron",
            "Notes or a reading app 📖": "Brownie",
            "A short-video app, endlessly scrolling 🎬": "Donut",
        },
    },
    {
        "question": "It's a bad day. What helps? 🌧️",
        "options": {
            "A hug and someone sweet to talk to 🤗": "Cupcake",
            "A walk outside to clear my head 🌳": "Ice Cream",
            "Making something pretty to feel better 🎀": "Macaron",
            "A warm drink and some quiet time ☕": "Brownie",
            "Laughing at something silly until I feel better 🤣": "Donut",
        },
    },
    {
        "question": "Last one! Pick a random word ✍️",
        "options": {
            "Sparkle ✨": "Cupcake",
            "Sunshine 🌞": "Ice Cream",
            "Whimsy 🦋": "Macaron",
            "Cosy 🧣": "Brownie",
            "Chaos 🎢": "Donut",
        },
    },
]

# ---------- APP MEMORY ----------
# session_state remembers things between clicks.
if "started" not in st.session_state:
    st.session_state.started = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Shuffle the answer order ONCE per visitor, then remember it.
# (If we shuffled on every rerun, the answers would jump around!)
if "shuffled_options" not in st.session_state:
    st.session_state.shuffled_options = []   # one shuffled list per question
    for q in QUESTIONS:
        answer_texts = list(q["options"].keys())  # just the answer texts
        random.shuffle(answer_texts)              # mix them up
        st.session_state.shuffled_options.append(answer_texts)

# ---------- TITLE (shown on every page) ----------
st.title(f"✨ Which {QUIZ_TOPIC} Are You? 🧁")

# ---------- WELCOME PAGE ----------
if not st.session_state.started:
    st.write("Welcome, sweet soul! 🌸 Answer a few random questions and discover your true match. 💖")

    name = st.text_input("What's your name? 💌")

    if st.button("Start the quiz 🌈"):
        if name.strip() == "":
            st.warning("Please tell me your name first! 🥺")
        else:
            st.session_state.user_name = name.strip()
            st.session_state.started = True
            st.rerun()

# ---------- QUESTIONS PAGE ----------
else:
    st.write(f"Okay {st.session_state.user_name}, let's begin! 🎀")
    st.caption(f"{len(QUESTIONS)} questions, no wrong answers 💕")

    with st.form("quiz_form"):
        answers = []

        for i, q in enumerate(QUESTIONS):
            st.subheader(f"{i + 1}/{len(QUESTIONS)}  {q['question']}")

            choice = st.radio(
                q["question"],
                st.session_state.shuffled_options[i],  # the shuffled answers for question i
                index=None,
                key=f"question_{i}",
                label_visibility="collapsed",
            )
            answers.append(choice)

        submitted = st.form_submit_button("Reveal my dessert 🍧")

    if submitted:
        if None in answers:
            st.warning("Please answer every question! 🥺")
        else:
            st.session_state.answers = answers
            st.success("Answers saved! 🎉 Your result is coming in the next section...")
