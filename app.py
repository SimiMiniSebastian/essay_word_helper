import streamlit as st
from nltk.corpus import wordnet
import re

# Page configuration
st.set_page_config(page_title="Essay Word Helper", page_icon="📝", layout="centered")

# Custom CSS for background and style
st.markdown("""
    <style>
    .stApp {
       background-image: url("https://unsplash.com/photos/the-night-sky-with-stars-above-a-mountain-9aCkSl6YcXg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #fff;
    }
    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        padding: 10px;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
    }
    .section {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>📝 Essay Word Helper</div>", unsafe_allow_html=True)

# Description
st.markdown("""
<div class="section">
<h4>📌 What is this?</h4>
<p>This tool helps you understand <i>advanced English words</i> used in essays by giving you <b>simple WordNet definitions</b>.</p>

<h4>👥 Who is it for?</h4>
<ul>
<li>IELTS, TOEFL, and other English exam takers</li>
<li>Students writing academic essays</li>
<li>Anyone learning English vocabulary</li>
</ul>

<h4>🛠️ How to use:</h4>
<ol>
<li>Paste your essay in the box below</li>
<li>Click the <b>"Find Difficult Words & Meanings"</b> button</li>
<li>Read the definitions of tricky words</li>
</ol>
</div>
""", unsafe_allow_html=True)

# Text area
essay = st.text_area("✍️ Paste your essay here:", height=200)

# Basic words to exclude
basic_words = set([
    'the', 'is', 'in', 'on', 'it', 'and', 'a', 'an', 'to', 'this', 'that', 'of', 'for',
    'with', 'as', 'by', 'was', 'are', 'from', 'at', 'be', 'or', 'not', 'but', 'has',
    'have', 'had', 'will', 'would', 'can', 'could', 'should', 'i', 'you', 'he', 'she',
    'we', 'they', 'them', 'my', 'your', 'his', 'her', 'their', 'our', 'its'
])

# Functions
def get_difficult_words(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    unique_words = set(words)
    difficult = [word for word in unique_words if word not in basic_words]
    return difficult

def get_wordnet_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return "Meaning not found ❌"

# Main button
if st.button("📚 Find Difficult Words & Meanings"):
    if essay.strip() == "":
        st.warning("⚠️ Please paste your essay first.")
    else:
        st.markdown("<div class='section'><h4>📘 Difficult Words and Meanings</h4>", unsafe_allow_html=True)
        difficult_words = get_difficult_words(essay)
        if not difficult_words:
            st.success("🎉 No difficult words found!")
        else:
            for word in difficult_words:
                meaning = get_wordnet_meaning(word)
                st.markdown(f"<p><b><i>{word.capitalize()}</i></b>: {meaning}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Rating
st.markdown("<br><div class='section'>", unsafe_allow_html=True)
st.subheader("🌟 Rate This Tool")

rating = st.radio(
    "How helpful was this app?",
    ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    index=4,
    horizontal=True
)
if rating:
    st.success(f"Thank you for rating us: {rating}")
st.markdown("</div>", unsafe_allow_html=True)
