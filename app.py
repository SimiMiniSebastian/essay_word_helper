import streamlit as st
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
import re

# Page configuration
st.set_page_config(page_title="Essay Word Helper", layout="centered")

# Custom CSS for ash background
st.markdown("""
    <style>
    .stApp {
        background-color: #2f2f2f;
        color: #ffffff;
    }
    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        padding: 10px;
        background-color: #444444;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .section {
        background-color: #3b3b3b;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>Essay Word Helper</div>", unsafe_allow_html=True)

# Description
st.markdown("""
<div class="section">
<h4>What is this?</h4>
<p>This tool helps you understand <i>advanced English words</i> in your essay by providing <b>simple definitions</b> using WordNet.</p>

<h4>Who is it for?</h4>
<ul>
<li>IELTS, TOEFL, and other English exam takers</li>
<li>Students writing academic essays</li>
<li>Anyone improving their English vocabulary</li>
</ul>

<h4>How to use:</h4>
<ol>
<li>Paste your essay below</li>
<li>Click "Find Difficult Words & Meanings"</li>
<li>View definitions for tricky words</li>
</ol>
</div>
""", unsafe_allow_html=True)

# Text area
essay = st.text_area("Paste your essay here:", height=200)

# Basic words to exclude
basic_words = set([
    'the', 'is', 'in', 'on', 'it', 'and', 'a', 'an', 'to', 'this', 'that', 'of', 'for',
    'with', 'as', 'by', 'was', 'are', 'from', 'at', 'be', 'or', 'not', 'but', 'has',
    'have', 'had', 'will', 'would', 'can', 'could', 'should', 'i', 'you', 'he', 'she',
    'we', 'they', 'them', 'my', 'your', 'his', 'her', 'their', 'our', 'its'
])

# Function to find difficult words
def get_difficult_words(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    unique_words = set(words)
    difficult = [word for word in unique_words if word not in basic_words]
    return difficult

# Get meaning from WordNet
def get_wordnet_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        definition = synsets[0].definition()
        if definition.strip():
            return definition
        else:
            return "No clear definition found."
    else:
        return "Word not found in dictionary."

# Button action
if st.button("Find Difficult Words & Meanings"):
    if essay.strip() == "":
        st.warning("Please paste your essay first.")
    else:
        st.markdown("<div class='section'><h4>Difficult Words and Meanings</h4>", unsafe_allow_html=True)
        difficult_words = get_difficult_words(essay)
        if not difficult_words:
            st.success("No difficult words found.")
        else:
            for word in difficult_words:
                meaning = get_wordnet_meaning(word)
                st.markdown(f"<p><b><i>{word.capitalize()}</i></b>: {meaning}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Rating section
st.markdown("<br><div class='section'>", unsafe_allow_html=True)
st.subheader("Rate This Tool")

rating = st.radio(
    "How helpful was this app?",
    ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    index=4,
    horizontal=True
)
if rating:
    st.success(f"Thank you for your rating: {rating}")
st.markdown("</div>", unsafe_allow_html=True)
