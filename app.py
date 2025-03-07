import streamlit as st
import random

# Streamlit Page Config
st.set_page_config(page_title="🎲 Dice Game", page_icon="🎲", layout="centered")

# CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            text-align: center;
        }
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
        .lost {
            font-size: 24px;
            font-weight: bold;
            color: #ff0000;
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
if "player1_name" not in st.session_state:
    st.session_state.player1_name = ""
    st.session_state.player2_name = ""
    st.session_state.player1_score = 0
    st.session_state.player2_score = 0
    st.session_state.turn = "player1"
    st.session_state.roll_count = 0
    st.session_state.game_started = False
    st.session_state.winner = None

# Title
st.markdown("<div class='title'>🎲 2-Player Dice Game 🎲</div>", unsafe_allow_html=True)

# Player Name Input
if not st.session_state.game_started:
    st.subheader("Enter Player Names:")
    st.session_state.player1_name = st.text_input("Player 1 Name", value="Player 1")
    st.session_state.player2_name = st.text_input("Player 2 Name", value="Player 2")
    if st.button("Start Game"):
        st.session_state.game_started = True
        st.experimental_rerun()

# Game Logic
else:
    st.subheader(f"🎲 {st.session_state.player1_name} vs {st.session_state.player2_name}")
    st.write(f"**Current Turn:** {st.session_state.player1_name if st.session_state.turn == 'player1' else st.session_state.player2_name}")
    st.write(f"Rolls Left: {MAX_ROLLS - st.session_state.roll_count}")

    if st.session_state.winner:
        st.markdown(f"<div class='winner'>{st.session_state.winner} 🎉</div>", unsafe_allow_html=True)
    else:
        if st.button("Roll Dice 🎲"):
            roll_value = random.randint(1, 6)
            dice_icon = DICE_ICONS[roll_value]
            st.session_state.roll_count += 1

            if st.session_state.turn == "player1":
                st.session_state.player1_score += roll_value
                st.session_state.turn = "player2"
            else:
                st.session_state.player2_score += roll_value
                st.session_state.turn = "player1"

            # Display Dice Roll
            st.markdown(f"<h1>{dice_icon}</h1>", unsafe_allow_html=True)

            # Check for game over
            if st.session_state.roll_count >= MAX_ROLLS:
                if st.session_state.player1_score > st.session_state.player2_score:
                    st.session_state.winner = f"{st.session_state.player1_name} Wins! 🏆"
                elif st.session_state.player2_score > st.session_state.player1_score:
                    st.session_state.winner = f"{st.session_state.player2_name} Wins! 🏆"
                else:
                    st.session_state.winner = "It's a Tie! 🎲"

            st.experimental_rerun()

    # Display Scores
    st.write(f"🔹 **{st.session_state.player1_name}'s Score:** {st.session_state.player1_score}")
    st.write(f"🔹 **{st.session_state.player2_name}'s Score:** {st.session_state.player2_score}")

    # Restart Button
    if st.button("Restart Game 🔄"):
        st.session_state.player1_score = 0
        st.session_state.player2_score = 0
        st.session_state.roll_count = 0
        st.session_state.turn = "player1"
        st.session_state.winner = None
        st.experimental_rerun()
