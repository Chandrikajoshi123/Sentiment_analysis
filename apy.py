import streamlit as st
from transformers import pipeline
import time

# 💡 Use CPU to avoid meta tensor error
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True,
    device=-1
)

# 🌈 Emotion → Emoji, Color, Quote, Prompt
emotion_map = {
    "anger": {
        "emoji": "😠", "color": "#FFB3B3",
        "quote": "Holding onto anger is like drinking poison and expecting the other person to die.",
        "prompt": "What made you feel angry today? How did you react? Could you respond differently next time?"
    },
    "disgust": {
        "emoji": "🤢", "color": "#C2F0C2",
        "quote": "Disgust helps us understand our values. What are you standing against?",
        "prompt": "What triggered your sense of disgust? Was it related to a belief or expectation?"
    },
    "fear": {
        "emoji": "😨", "color": "#D1C4E9",
        "quote": "Everything you’ve ever wanted is on the other side of fear.",
        "prompt": "What are you afraid of right now? Is this fear protecting or limiting you?"
    },
    "joy": {
        "emoji": "😊", "color": "#FFFACD",
        "quote": "Joy is not in things; it is in us.",
        "prompt": "What made you smile today? What moments filled you with joy?"
    },
    "neutral": {
        "emoji": "😐", "color": "#E0E0E0",
        "quote": "Even the still moments carry meaning.",
        "prompt": "How does it feel to be in a neutral state? What do you want more or less of?"
    },
    "sadness": {
        "emoji": "😢", "color": "#AED6F1",
        "quote": "Tears come from the heart, not the brain.",
        "prompt": "What’s making you feel down? Is there someone or something you miss or need to release?"
    },
    "surprise": {
        "emoji": "😲", "color": "#FAD7A0",
        "quote": "Surprise is the seed of change. Everything begins with a wow.",
        "prompt": "What surprised you today? Was it positive or negative? Why?"
    },
    "love": {
        "emoji": "😍", "color": "#F9C6D2",
        "quote": "Where there is love, there is life.",
        "prompt": "Who or what do you love today? How does that shape your actions?"
    }
}

# 🌟 Page Style
st.set_page_config(page_title="How Are You Feeling?", layout="centered")

custom_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(to right, #ffe4ec, #f3f8ff);
    background-size: cover;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.big-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #ff4d6d;
    margin-bottom: 0px;
}
.subtext {
    text-align: center;
    font-size: 20px;
    color: #333333;
    margin-top: 0px;
    margin-bottom: 40px;
}
textarea {
    border-radius: 12px !important;
    font-size: 16px !important;
}
.confidence-score {
    font-size: 16px;
    color: #333333;
    font-weight: 500;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 🧠 Title
st.markdown("<div class='big-title'>🎈 How Are You Feeling? 💬</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Tell me something and I’ll guess your emotion using AI 🤖</div>", unsafe_allow_html=True)

# 📥 Input
user_input = st.text_area("Your Text:", placeholder="e.g. I feel amazing today!", height=150)

if st.button("✨ Analyze Emotion"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing your feelings..."):
            time.sleep(1)
            results = classifier(user_input)[0]
            results = sorted(results, key=lambda x: x["score"], reverse=True)

            top_emotion = results[0]["label"].lower()
            emoji = emotion_map[top_emotion]["emoji"]
            bg_color = emotion_map[top_emotion]["color"]
            quote = emotion_map[top_emotion]["quote"]
            prompt = emotion_map[top_emotion]["prompt"]

            # 🌟 Emotion Card
            st.markdown(
                f"""
                <div style='background-color: {bg_color}; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 4px 4px 10px rgba(0,0,0,0.1);'>
                    <h1 style='font-size: 80px;'>{emoji}</h1>
                    <h2 style='margin-top: 10px; color: #222;'>You're feeling <b>{top_emotion.capitalize()}</b></h2>
                </div>
                """,
                unsafe_allow_html=True
            )

            # 🧠 Quote
            st.markdown(f"<div style='color:#222; font-size:20px;'><b>🌸 Motivation:</b> <i>{quote}</i></div>", unsafe_allow_html=True)


            # 📝 Prompt
            st.markdown(f"#### 📓 Journaling Prompt: {prompt}")

            # 📊 Confidence Scores
            with st.expander("📈 See Emotion Confidence"):
                for item in results:
                    label = item["label"].capitalize()
                    score = round(item["score"], 3)
                    st.markdown(f"<div class='confidence-score'>{label}: {score}</div>", unsafe_allow_html=True)
