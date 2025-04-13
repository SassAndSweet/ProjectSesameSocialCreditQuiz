import streamlit as st

# Add custom CSS for background image, bold text, and white text
st.markdown("""
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/SassAndSweet/ProjectSesameSocialCreditQuiz/main/sesame_background.png");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    overflow-y: auto;
}

/* Semi-transparent overlay */
.stApp::after {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    z-index: 0;
    pointer-events: none;
}

/* Make content appear above overlay */
.stApp > header, .stApp > div {
    position: relative;
    z-index: 1;
}

/* Make all text bold and white */
.stApp, .stApp p, .stApp label, .stApp div, .stRadio label, .stMarkdown, .stForm {
    font-weight: bold !important;
    color: white !important;
}

/* Style buttons */
.stButton button, [data-testid="baseButton-secondary"] {
    color: #00008B !important; /* Dark blue text */
    background-color: white !important;
    font-weight: bold !important;
}

/* Adjust background of content areas to be more transparent */
.stApp > div {
    background-color: rgba(0, 0, 0, 0.4) !important;
}

/* Fix scrolling */
[data-testid="stAppViewContainer"] {
    overflow: auto;
    height: 100vh;
}

/* Style form elements */
.stForm [data-testid="stFormSubmitButton"] button {
