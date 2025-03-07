import streamlit as st
import random

# Streamlit Page Config
st.set_page_config(page_title="🎲 Dice Game", page_icon="🎲", layout="centered")

# CSS for Styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            color: white;
            text-align: center;
        }
        .title {
            font-size: 30px;
            font-weight: bold;
            color: white;
            text-align: center;
        }
        .winner {
            font-size: 24px;
            font-weight: bold;
            color: #00ff00;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Dice Images
DICE_ICONS = {
    1: "🎲 1",
    2: "🎲 2",
    3: "🎲 3",
    4: "🎲 4",
    5: "🎲 5",
    6: "🎲 6"
}

MAX_ROLLS = 10  # Maximum rolls before the game ends

# Game State (Stored in Session)
if "game_state" not in st.session_state:
    st.session_state.game_state = {
        "player1_name": "",
        "player2_name": "",
        "player1_score": 0,
        "player2_score": 0,
        "turn": "player1",
        "roll_count": 0,
        "game_started": False,
        "winner": None
    }

state = st.session_state.game_state

# Title
st.markdown("<div class='title'>🎲 Dice Game 🎲</div>", unsafe_allow_html=True)

# Player Name Input
if not state["game_started"]:
    st.subheader("Enter Player Names:")
    state["player1_name"] = st.text_input("Player 1 Name", value="Player 1")
    state["player2_name"] = st.text_input("Player 2 Name", value="Player 2")
    
    if st.button("Start Game"):
        state["game_started"] = True
        st.rerun()

# Game Logic
else:
    st.subheader(f"🎲 {state['player1_name']} vs {state['player2_name']}")
    st.write(f"**Current Turn:** {state['player1_name'] if state['turn'] == 'player1' else state['player2_name']}")
    st.write(f"Rolls Left: {MAX_ROLLS - state['roll_count']}")

    if state["winner"]:
        st.markdown(f"<div class='winner'>{state['winner']} 🎉</div>", unsafe_allow_html=True)
    else:
        if st.button("Roll Dice 🎲"):
            roll_value = random.randint(1, 6)
            dice_icon = DICE_ICONS[roll_value]
            state["roll_count"] += 1

            if state["turn"] == "player1":
                state["player1_score"] += roll_value
                state["turn"] = "player2"
            else:
                state["player2_score"] += roll_value
                state["turn"] = "player1"

            # Display Dice Roll
            st.markdown(f"<h1>{dice_icon}</h1>", unsafe_allow_html=True)

            # Check for game over
            if state["roll_count"] >= MAX_ROLLS:
                if state["player1_score"] > state["player2_score"]:
                    state["winner"] = f"{state['player1_name']} Wins! 🏆"
                elif state["player2_score"] > state["player1_score"]:
                    state["winner"] = f"{state['player2_name']} Wins! 🏆"
                else:
                    state["winner"] = "It's a Tie! 🎲"

            st.rerun() 

    # Display Scores
    st.write(f"🔹 **{state['player1_name']}'s Score:** {state['player1_score']}")
    st.write(f"🔹 **{state['player2_name']}'s Score:** {state['player2_score']}")

    # Restart Button
    if st.button("Restart Game 🔄"):
        st.session_state.game_state = {
            "player1_name": "",
            "player2_name": "",
            "player1_score": 0,
            "player2_score": 0,
            "turn": "player1",
            "roll_count": 0,
            "game_started": False,
            "winner": None
        }
        st.rerun()  
