import streamlit as st

# Add custom CSS for background image and general styling
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

/* Adjust background of content areas to be more transparent */
.stApp > div {
    background-color: rgba(0, 0, 0, 0.4) !important;
}

/* Fix scrolling */
[data-testid="stAppViewContainer"] {
    overflow: auto;
    height: 100vh;
}

/* Custom button style */
.custom-button {
    background-color: white !important;
    color: #00008B !important;
    font-weight: bold !important;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    margin: 10px 0;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Sesame Credit Quiz")
    st.write("Answer the following questions to find out what exclusive social perks you might earn!")

    # Initialize session state for storing the score and quiz completion
    if 'score_total' not in st.session_state:
        st.session_state.score_total = 0
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
    if 'predicted_credit' not in st.session_state:
        st.session_state.predicted_credit = 0

    # Function to calculate score
    def calculate_score():
        score = 0
        if st.session_state.q1 == "Always on time – even my bills get a red carpet treatment!":
            score += 20
        elif st.session_state.q1 == "Usually on time – I'm no slacker.":
            score += 15
        elif st.session_state.q1 == "Sometimes a bit late – my procrastination is legendary.":
            score += 10
        elif st.session_state.q1 == "Often forget – my memes come before my bills.":
            score += 5
        
        if st.session_state.q2 == "I've been working since the dinosaurs roamed – a true career veteran!":
            score += 20
        elif st.session_state.q2 == "Over 10 years of steady work – reliability is my middle name.":
            score += 15
        elif st.session_state.q2 == "A few years – still figuring out the ropes.":
            score += 10
        else:
            score += 5
        
        # Add similar logic for all other questions
        # ...
        
        return score

    # Function to submit quiz
    def submit_quiz():
        st.session_state.score_total = calculate_score()
        max_total = 20 * 10  # Maximum possible score
        st.session_state.predicted_credit = 350 + int((st.session_state.score_total / max_total) * 600)
        st.session_state.quiz_submitted = True

    # Function to reset quiz
    def reset_quiz():
        st.session_state.quiz_submitted = False
        st.session_state.score_total = 0
        st.session_state.predicted_credit = 0
        # Reset all question answers
        # ...
        st.rerun()

    # If quiz hasn't been submitted, show the questions
    if not st.session_state.quiz_submitted:
        # Use a form to collect all responses at once
        with st.form("quiz_form"):
            # 1. Bill Payment Frequency
            st.session_state.q1 = st.radio(
                "1. How frequently do you pay your bills?",
                (
                    "Always on time – even my bills get a red carpet treatment!",
                    "Usually on time – I'm no slacker.",
                    "Sometimes a bit late – my procrastination is legendary.",
                    "Often forget – my memes come before my bills.",
                    "Never – I prefer living life on the wild side."
                ),
                key="q1"
            )

            # 2. Employment / Income Stability
            st.session_state.q2 = st.radio(
                "2. How long have you enjoyed stable employment/income?",
                (
                    "I've been working since the dinosaurs roamed – a true career veteran!",
                    "Over 10 years of steady work – reliability is my middle name.",
                    "A few years – still figuring out the ropes.",
                    "Just started – I'm the new kid on the block."
                ),
                key="q2"
            )

            # Add all other questions here
            # ...

            # Custom submit button
            st.markdown("""
            <button class="custom-button" type="submit">Submit Quiz</button>
            """, unsafe_allow_html=True)
            
            submitted = st.form_submit_button("Submit Quiz", type="primary")
            if submitted:
                submit_quiz()

    # If quiz has been submitted, show results
    else:
        max_total = 20 * 10
        st.markdown("---")
        st.write(f"**Your total score is:** {st.session_state.score_total} out of {max_total}")
        st.write(f"**Predicted Social Credit Score:** {st.session_state.predicted_credit}")
        
        # Determine humorous social benefits
        if st.session_state.predicted_credit >= 900:
            benefits = (
                "VIP Access: You're a social superstar!\n"
                "Enjoy exclusive perks like red carpet service at coffee shops, priority invites to legendary parties, "
                "and an honorary title as the 'Mogul of Mingling.'"
            )
        elif st.session_state.predicted_credit >= 750:
            benefits = (
                "Gold Tier: Highly esteemed in the social scene.\n"
                "Reap benefits including premium networking opportunities, special discounts at trendy hotspots, "
                "and front-of-line status at community events."
            )
        elif st.session_state.predicted_credit >= 550:
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
        
        # Custom retake button
        st.markdown("""
        <button class="custom-button" onclick="parent.window.location.reload()">Retake Quiz</button>
        """, unsafe_allow_html=True)
        
        # Alternate button method
        if st.button("Restart Quiz"):
            reset_quiz()

if __name__ == "__main__":
    main()
