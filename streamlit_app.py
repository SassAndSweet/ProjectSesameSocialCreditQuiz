import streamlit as st

# Add custom CSS for background image and text styling
st.markdown("""
<style>
    /* Background image for the whole app */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/SassAndSweet/ProjectSesameSocialCreditQuiz/main/sesame_background.png");
        background-size: cover;
        background-position: center;
    }
    
    /* Text styling */
    .stApp p, .stApp label, div.stRadio label, .stMarkdown p {
        font-weight: bold !important;
        color: white !important;
        font-size: 14pt !important;
    }
    
    /* Title styling */
    .stApp h1, .stApp h2, .stApp h3 {
        color: white !important;
        font-weight: bold !important;
    }
    
    /* Button styling */
    .stButton button, div[data-testid="stFormSubmitButton"] button {
        background-color: black !important;
        color: white !important;
        font-weight: bold !important;
        border: 2px solid red !important;
    }
    
    /* Style for the black content container */
    .quiz-container {
        background-color: black;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Create a container with black background
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    
    st.title("Sesame Credit Quiz")
    st.write("Answer the following questions to find out what exclusive social perks you might earn!")

    # Use a form to collect all responses at once.
    with st.form("quiz_form"):
        score_total = 0
        # Maximum possible score per question is 20, so for 10 questions:
        max_total = 20 * 10

        # 1. Bill Payment Frequency
        q1 = st.radio(
            "1. How frequently do you pay your bills?",
            (
                "Always on time – even my bills get a red carpet treatment!",
                "Usually on time – I'm no slacker.",
                "Sometimes a bit late – my procrastination is legendary.",
                "Often forget – my memes come before my bills.",
                "Never – I prefer living life on the wild side."
            )
        )
        if q1 == "Always on time – even my bills get a red carpet treatment!":
            score_total += 20
        elif q1 == "Usually on time – I'm no slacker.":
            score_total += 15
        elif q1 == "Sometimes a bit late – my procrastination is legendary.":
            score_total += 10
        elif q1 == "Often forget – my memes come before my bills.":
            score_total += 5
        else:
            score_total += 0

        # Copy all your remaining questions here...
        # (I'm omitting them for brevity, but keep them all in your code)

        # Submit button for the form.
        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        # Scale score: 350 (min) to 950 (max)
        predicted_credit = 350 + int((score_total / max_total) * 600)
        st.markdown("---")
        st.write(f"**Your total score is:** {score_total} out of {max_total}")
        st.write(f"**Predicted Social Credit Score:** {predicted_credit}")
        
        # Determine humorous social benefits
        if predicted_credit >= 900:
            benefits = (
                "VIP Access: You're a social superstar!\n"
                "Enjoy exclusive perks like red carpet service at coffee shops, priority invites to legendary parties, "
                "and an honorary title as the 'Mogul of Mingling.'"
            )
        elif predicted_credit >= 750:
            benefits = (
                "Gold Tier: Highly esteemed in the social scene.\n"
                "Reap benefits including premium networking opportunities, special discounts at trendy hotspots, "
                "and front-of-line status at community events."
            )
        elif predicted_credit >= 550:
            benefits = (
                "Silver Tier: You're doing well and have room to shine even brighter.\n"
                "Expect perks like discounts at your favorite hangouts, prioritized bookings for events, "
                "and occasional surprise bonuses for being awesome."
            )
        else:
            benefits = (
                "Bronze Tier: Time to boost that social karma!\n"
                "But don't despair – perks include modest discounts, a chance to earn extra points through community engagement, "
                "and plenty of opportunities to work your way up."
            )
        st.write("### Social Benefits Eligibility:")
        st.write(benefits)
        
        # Retake quiz option – rerun the app.
        if st.button("Retake Quiz"):
            st.rerun()
    
    # Close the black container div
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
