# import streamlit as st
# from transformers import pipeline
# import time

# # 💡 Use device=-1 to force CPU and avoid meta tensor bug
# classifier = pipeline(
#     "text-classification",
#     model="j-hartmann/emotion-english-distilroberta-base",
#     return_all_scores=True,
#     device=-1
# )

# # 🌈 Emotion → Emoji + Pastel Color
# emotion_map = {
#     "anger": {"emoji": "😠", "color": "#FFCCCC"},
#     "disgust": {"emoji": "🤢", "color": "#CCFFCC"},
#     "fear": {"emoji": "😨", "color": "#E0CCFF"},
#     "joy": {"emoji": "😊", "color": "#FFFFCC"},
#     "neutral": {"emoji": "😐", "color": "#EEEEEE"},
#     "sadness": {"emoji": "😢", "color": "#CCE5FF"},
#     "surprise": {"emoji": "😲", "color": "#FFDDAA"},
#     "love": {"emoji": "😍", "color": "#FFCCE5"}
# }

# # 🌟 Streamlit Page Config + Custom Style
# st.set_page_config(page_title="How Are You Feeling?", layout="centered")

# page_bg = """
# <style>
# [data-testid="stAppViewContainer"] {
#     background-image: linear-gradient(to right, #fff5f5, #f0f9ff);
#     background-size: cover;
#     font-family: 'Comic Sans MS', cursive, sans-serif;
# }
# h1, h2, h3 {
#     color: #ff4d6d;
# }
# textarea {
#     border-radius: 10px !important;
# }
# </style>
# """
# st.markdown(page_bg, unsafe_allow_html=True)

# # 🧠 App Title
# st.markdown("<h1 style='text-align: center;'>How Are You Feeling?</h1>", unsafe_allow_html=True)
# st.write("Enter a sentence below, and I’ll try to guess your emotion 💬")

# # 🧾 Input Box
# user_input = st.text_area("Your Text:", placeholder="e.g. I feel amazing today!", height=150)

# if st.button("✨ Analyze Emotion"):
#     if not user_input.strip():
#         st.warning("Please enter some text first.")
#     else:
#         with st.spinner("Analyzing your feelings..."):
#             time.sleep(1)
#             results = classifier(user_input)[0]
#             results = sorted(results, key=lambda x: x["score"], reverse=True)

#             top_emotion = results[0]["label"].lower()
#             emoji = emotion_map.get(top_emotion, {}).get("emoji", "🙂")
#             bg_color = emotion_map.get(top_emotion, {}).get("color", "#090808")

#             # 🎯 Display Emotion Card
#             st.markdown(
#                 f"""
#                 <div style='background-color: {bg_color}; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 4px 4px 10px rgba(0,0,0,0.1);'>
#                     <h1 style='font-size: 80px;'>{emoji}</h1>
#                     <h2 style='margin-top: 10px;'>You're feeling <b>{top_emotion.capitalize()}</b></h2>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             # 📊 Optional Score Breakdown
#             with st.expander("📈 Emotion Confidence Scores"):
#                 for item in results:
#                     st.write(f"**{item['label']}**: {item['score']:.3f}")


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

# 🌈 Emotion → Emoji + Color
emotion_map = {
    "anger": {"emoji": "😠", "color": "#FFB3B3"},
    "disgust": {"emoji": "🤢", "color": "#C2F0C2"},
    "fear": {"emoji": "😨", "color": "#D1C4E9"},
    "joy": {"emoji": "😊", "color": "#FFFACD"},
    "neutral": {"emoji": "😐", "color": "#E0E0E0"},
    "sadness": {"emoji": "😢", "color": "#AED6F1"},
    "surprise": {"emoji": "😲", "color": "#FAD7A0"},
    "love": {"emoji": "😍", "color": "#F9C6D2"}
}

# 🎨 Page Setup
st.set_page_config(page_title="How Are You Feeling?", layout="centered")

# 🌟 Background + Fonts + Emojis in Header
custom_css = """
<style>
/* Background gradient */
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(to right, #ffe4ec, #f3f8ff);
    background-size: cover;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* Title & Header */
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
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 🌟 Title
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
            emoji = emotion_map.get(top_emotion, {}).get("emoji", "🙂")
            bg_color = emotion_map.get(top_emotion, {}).get("color", "#FFFFFF")

            # 🎯 Display Emotion Result
            st.markdown(
                f"""
                <div style='background-color: {bg_color}; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 4px 4px 10px rgba(0,0,0,0.1);'>
                    <h1 style='font-size: 80px;'>{emoji}</h1>
                    <h2 style='margin-top: 10px;'>You're feeling <b>{top_emotion.capitalize()}</b></h2>
                </div>
                """,
                unsafe_allow_html=True
            )

            # 📊 Optional Confidence Scores
            with st.expander("📈 See Emotion Confidence"):
                for item in results:
                    st.write(f"**{item['label']}**: {item['score']:.3f}")
