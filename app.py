import random  # random lets us shuffle things and pick random winners
import streamlit as st  # Streamlit turns Python into a web app

# ---------- SETTINGS ----------
QUIZ_TOPIC = "Dessert"

# The list of possible results. Keep these names the SAME as in the questions!
DESSERTS = ["Cupcake", "Ice Cream", "Macaron", "Brownie", "Donut"]

st.set_page_config(
    page_title=f"Which {QUIZ_TOPIC} Are You?",
    page_icon="🧁",
)

# ---------- COLOURS AND STYLING ----------
# CSS is the language that controls how web pages look.
# Streamlit lets us add our own CSS using st.markdown with unsafe_allow_html=True.
# Colours are "hex codes" like #ffd6e8. Change them to make your own palette!
CUSTOM_CSS = """
<style>
/* A cute rounded font from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&display=swap');

html, body, .stApp, button, input, label, p, li {
    font-family: 'Quicksand', sans-serif;
}

/* Dreamy pastel gradient background: pink -> lavender -> baby blue */
.stApp {
    background: linear-gradient(160deg, #fff0f6 0%, #f0e9ff 50%, #e6f7ff 100%);
}

/* Main text colour: a soft plum, easy to read on pastel */
.stApp, .stApp p, .stApp label, .stApp li {
    color: #5b3a5e;
}

/* Headings: a deeper pink so they stand out */
h1, h2, h3 {
    color: #c2418a !important;
    font-weight: 700 !important;
}

/* Buttons: soft pink, rounded, and they get darker when you hover */
.stButton > button, .stFormSubmitButton > button {
    background-color: #ffd6e8;
    color: #7a2e5c;
    border: 2px solid #ff9fc9;
    border-radius: 20px;
    padding: 0.5rem 1.5rem;
    font-weight: 700;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background-color: #ffc2de;
    border-color: #ff7ab5;
    color: #7a2e5c;
}

/* The quiz form becomes a see-through white "card" */
[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.6);
    border: 2px solid #ffd1e6;
    border-radius: 24px;
    padding: 1.5rem;
}

/* The name box: rounded with a pink border */
.stTextInput input {
    border-radius: 14px;
    border: 2px solid #ffd1e6;
}

/* Progress bars on the result page: pink */
.stProgress > div > div > div > div {
    background-color: #ff8fc0;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------- THE RESULTS ----------
# A dictionary of dictionaries. Each dessert has its own little info card.
RESULTS = {
    "Cupcake": {
        "emoji": "🧁",
        "tagline": "Sweet, caring, and always adding a little sparkle ✨",
        "description": (
            "You're the friend everyone feels safe around. You remember birthdays, "
            "send the nicest messages, and make even boring days feel special. "
            "You love pretty things and you put love into everything you do."
        ),
        "traits": ["Kind-hearted 🥰", "Loves cute details 🎀", "A natural caregiver 💌"],
    },
    "Ice Cream": {
        "emoji": "🍦",
        "tagline": "Fun, bright, and always up for an adventure ☀️",
        "description": (
            "You bring the sunshine wherever you go. You're spontaneous, friendly, "
            "and the first to say 'let's do it!' People love your energy, "
            "and you make every day feel like summer."
        ),
        "traits": ["Adventurous 🗺️", "Easygoing 🌊", "Super friendly 😎"],
    },
    "Macaron": {
        "emoji": "🍬",
        "tagline": "Elegant, creative, and a little dreamy 💜",
        "description": (
            "You have taste and you know it. You notice beautiful little details "
            "that others miss, and your mind is full of ideas. You might be quiet, "
            "but your style and creativity speak loudly."
        ),
        "traits": ["Creative 🎨", "Great taste ✨", "Thoughtful 🤍"],
    },
    "Brownie": {
        "emoji": "🍫",
        "tagline": "Warm, cosy, and everyone's comfort person 🧸",
        "description": (
            "You're the friend people go to when they need a hug or good advice. "
            "You love quiet nights, deep talks, and a warm blanket. "
            "Being around you feels like coming home."
        ),
        "traits": ["Comforting 🫶", "A great listener 👂", "Loyal 🤎"],
    },
    "Donut": {
        "emoji": "🍩",
        "tagline": "Playful, chaotic, and absolutely unforgettable 🎢",
        "description": (
            "Life is never boring with you around! You're funny, unpredictable, "
            "and you make any room more fun. You don't take things too seriously, "
            "and your friends wouldn't have you any other way."
        ),
        "traits": ["Hilarious 😂", "Full of surprises 🎉", "Never boring 🤪"],
    },
}

# ---------- THE QUESTIONS ----------
# A list [] of dictionaries {}. Each dictionary is one question.
# "options" maps each answer text -> the dessert that answer points to.
# The user only sees the answer text. The dessert names stay hidden!
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
            "Cute sneakers 💖": "Cupcake",
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


# ---------- THE SCORING FUNCTION ----------
# This one takes the user's answers and gives back the winning dessert + the scores.
def calculate_result(answers):
    # Start every dessert on 0 points, e.g. {"Cupcake": 0, "Ice Cream": 0, ...}
    scores = {dessert: 0 for dessert in DESSERTS}

    # Go through each answer. i = question number, answer_text = what they picked
    for i, answer_text in enumerate(answers):
        # Look up the hidden dessert for this answer
        dessert = QUESTIONS[i]["options"][answer_text]
        # Give that dessert +1 point
        scores[dessert] += 1

    # Find the highest score
    top_score = max(scores.values())

    # Make a list of every dessert that has the top score
    winners = [dessert for dessert, score in scores.items() if score == top_score]

    # If there's a tie, random.choice picks one of the tied desserts
    result = random.choice(winners)

    return result, scores


# ---------- APP MEMORY ----------
# session_state remembers things between clicks.
if "started" not in st.session_state:
    st.session_state.started = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "result" not in st.session_state:
    st.session_state.result = None   # None = no result yet
if "scores" not in st.session_state:
    st.session_state.scores = {}
if "guess" not in st.session_state:
    st.session_state.guess = None    # the dessert the user GUESSES they are

# Shuffle the answer order ONCE per visitor, then remember it.
if "shuffled_options" not in st.session_state:
    st.session_state.shuffled_options = []   # one shuffled list per question
    for q in QUESTIONS:
        answer_texts = list(q["options"].keys())  # just the answer texts
        random.shuffle(answer_texts)              # mix them up
        st.session_state.shuffled_options.append(answer_texts)

# ---------- TITLE (shown on every page) ----------
st.title(f"✨ Which {QUIZ_TOPIC} Are You? 🧁")

# ---------- PAGE 4: RESULT PAGE ----------
# We have a result AND a guess, so show the big reveal!
if st.session_state.result is not None and st.session_state.guess is not None:
    result = st.session_state.result   # e.g. "Cupcake"
    guess = st.session_state.guess     # what they guessed
    info = RESULTS[result]             # the info card for the real result
    guess_emoji = RESULTS[guess]["emoji"]

    # ---- BONUS: guess vs real result ----
    st.write(f"🔮 You guessed: **{guess_emoji} {guess}**")

    if guess == result:
        st.balloons()  # 🎈 balloons float up the screen!
        st.success(f"And you were RIGHT! You're a {info['emoji']} {result}! You know yourself so well! 🎉")
    else:
        st.info(f"But you're actually a {info['emoji']} {result}! Surprise! 😆")

    st.markdown(f"# {info['emoji']}")
    st.header(f"{st.session_state.user_name}, you are a {result}!")
    st.subheader(info["tagline"])
    st.write(info["description"])

    # Show the traits one by one
    st.write("**Your sweet traits:**")
    for trait in info["traits"]:
        st.write(f"- {trait}")

    st.divider()  # a thin line to separate sections

    # Score breakdown: highest score first
    st.write("**Your full dessert breakdown:** 🍰")
    sorted_scores = sorted(
        st.session_state.scores.items(),
        key=lambda item: item[1],   # sort by the score (the 2nd part of each pair)
        reverse=True,               # biggest first
    )
    for dessert, score in sorted_scores:
        # Add a little marker next to the dessert they guessed
        marker = "  ← your guess 🔮" if dessert == guess else ""
        st.write(f"{RESULTS[dessert]['emoji']} {dessert}: {score}/{len(QUESTIONS)}{marker}")
        st.progress(score / len(QUESTIONS))   # a bar from 0.0 (empty) to 1.0 (full)

    st.divider()

    # Retake button: wipe the app's memory and start over
    if st.button("Retake the quiz 🔄"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ---------- PAGE 3: GUESS PAGE ----------
# We have a result, but no guess yet. Ask for the guess BEFORE revealing!
elif st.session_state.result is not None:
    st.header("🥁 Your answers are in!")
    st.write("Before I reveal your dessert... which one do you think you are? 🔮")

    # format_func changes how each option LOOKS (adds the emoji)
    # while the value we get back is still just the dessert name.
    guess_choice = st.radio(
        "Tag yourself! 🍰",
        DESSERTS,
        index=None,
        format_func=lambda dessert: f"{RESULTS[dessert]['emoji']} {dessert}",
    )

    if st.button("Reveal my dessert 🍧"):
        if guess_choice is None:
            st.warning("Make a guess first, no peeking! 🔮")
        else:
            st.session_state.guess = guess_choice   # remember the guess
            st.rerun()

# ---------- PAGE 1: WELCOME PAGE ----------
elif not st.session_state.started:
    st.write("Hello! Answer a few random questions and discover your sweet match. 💖")

    name = st.text_input("What's your name? 💌")

    if st.button("Start the quiz 🌈"):
        if name.strip() == "":
            st.warning("Please input your name first! ")
        else:
            st.session_state.user_name = name.strip()
            st.session_state.started = True
            st.rerun()

# ---------- PAGE 2: QUESTIONS PAGE ----------
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

        submitted = st.form_submit_button("Done! 🍧")

    if submitted:
        if None in answers:
            st.warning("Please answer every question! 🥺")
        else:
            # Work out the result and save it quietly (we DON'T show it yet!)
            result, scores = calculate_result(answers)
            st.session_state.result = result
            st.session_state.scores = scores
            st.rerun()
