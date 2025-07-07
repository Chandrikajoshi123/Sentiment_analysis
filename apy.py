import streamlit as st
from transformers import pipeline
from PIL import Image
import base64

# Load Hugging Face pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# Map emotion to emoji and background color
emotion_map = {
    "anger": {"emoji": "😠", "color": "#FFCCCC"},
    "disgust": {"emoji": "🤢", "color": "#CCFFCC"},
    "fear": {"emoji": "😨", "color": "#E0CCFF"},
    "joy": {"emoji": "😊", "color": "#FFFFCC"},
    "neutral": {"emoji": "😐", "color": "#EEEEEE"},
    "sadness": {"emoji": "😢", "color": "#CCE5FF"},
    "surprise": {"emoji": "😲", "color": "#FFDDAA"},
    "love": {"emoji": "😍", "color": "#FFCCE5"}
}

st.set_page_config(page_title="How Are You Feeling?", layout="centered")
st.markdown("<h1 style='text-align: center;'>How Are You Feeling?</h1>", unsafe_allow_html=True)

st.markdown("Enter a sentence below to detect the emotion 👇")

user_input = st.text_area("Your text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            results = classifier(user_input)[0]
            results = sorted(results, key=lambda x: x['score'], reverse=True)
            top_emotion = results[0]['label'].lower()

            emoji = emotion_map.get(top_emotion, {}).get("emoji", "🙂")
            bg_color = emotion_map.get(top_emotion, {}).get("color", "#FFFFFF")

            st.markdown(
                f"<div style='background-color: {bg_color}; padding: 40px; border-radius: 20px; text-align: center;'>"
                f"<h1 style='font-size: 80px;'>{emoji}</h1>"
                f"<h2 style='margin-top: 10px;'>You seem to be feeling <b>{top_emotion.capitalize()}</b></h2>"
                "</div>",
                unsafe_allow_html=True
            )

            # Show all emotions scores (optional)
            with st.expander("See emotion scores"):
                for item in results:
                    st.write(f"{item['label']}: {item['score']:.3f}")
