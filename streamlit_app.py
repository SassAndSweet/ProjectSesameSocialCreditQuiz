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

/* Make sure form elements and buttons are still visible */
.stButton button {
    color: black !important;
    background-color: white !important;
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
</style>
""", unsafe_allow_html=True)

def main():
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

        # 2. Employment / Income Stability
        q2 = st.radio(
            "2. How long have you enjoyed stable employment/income?",
            (
                "I've been working since the dinosaurs roamed – a true career veteran!",
                "Over 10 years of steady work – reliability is my middle name.",
                "A few years – still figuring out the ropes.",
                "Just started – I'm the new kid on the block."
            )
        )
        if q2 == "I've been working since the dinosaurs roamed – a true career veteran!":
            score_total += 20
        elif q2 == "Over 10 years of steady work – reliability is my middle name.":
            score_total += 15
        elif q2 == "A few years – still figuring out the ropes.":
            score_total += 10
        else:
            score_total += 5

        # 3. Savings and Investment Habits
        q3 = st.radio(
            "3. How would you rate your savings and investment habits?",
            (
                "I'm squirreling away nuts like a financial fox!",
                "I save whenever possible – my piggy bank is growing.",
                "I try, but there's always a tempting sale.",
                "Spending is my cardio – live for today!"
            )
        )
        if q3 == "I'm squirreling away nuts like a financial fox!":
            score_total += 20
        elif q3 == "I save whenever possible – my piggy bank is growing.":
            score_total += 15
        elif q3 == "I try, but there's always a tempting sale.":
            score_total += 10
        else:
            score_total += 5

        # 4. Credit History Diversity
        q4 = st.radio(
            "4. How diverse is your credit history?",
            (
                "A rich cocktail of loans and cards – variety is the spice of life!",
                "I have a couple of credit cards and a small loan.",
                "Just one or two credit products, but they do the job.",
                "Credit? I barely know what that is!"
            )
        )
        if q4 == "A rich cocktail of loans and cards – variety is the spice of life!":
            score_total += 20
        elif q4 == "I have a couple of credit cards and a small loan.":
            score_total += 15
        elif q4 == "Just one or two credit products, but they do the job.":
            score_total += 10
        else:
            score_total += 5

        # 5. Loan Defaults History
        q5 = st.radio(
            "5. Have you ever defaulted on a loan?",
            (
                "Never defaulted – my record is as clean as a whistle!",
                "Defaulted once – a minor hiccup in an otherwise stellar journey.",
                "Multiple defaults – I like living on the edge!"
            )
        )
        if q5 == "Never defaulted – my record is as clean as a whistle!":
            score_total += 20
        elif q5 == "Defaulted once – a minor hiccup in an otherwise stellar journey.":
            score_total += 10
        else:
            score_total += 0

        # 6. Community Involvement
        q6 = st.radio(
            "6. How active are you in community or volunteer work?",
            (
                "I'm practically a neighborhood superhero – always ready to lend a hand!",
                "I help out when asked – I'm a team player.",
                "I'm occasionally involved, when I remember.",
                "I'm more of a silent observer – my aura speaks for itself."
            )
        )
        if q6 == "I'm practically a neighborhood superhero – always ready to lend a hand!":
            score_total += 20
        elif q6 == "I help out when asked – I'm a team player.":
            score_total += 15
        elif q6 == "I'm occasionally involved, when I remember.":
            score_total += 10
        else:
            score_total += 5

        # 7. Social Media Behavior
        q7 = st.radio(
            "7. What's your style on social media?",
            (
                "I spread positive vibes and constructive memes like confetti!",
                "Mostly upbeat posts – I like to keep it friendly.",
                "I scroll through life, posting only when inspired.",
                "I lurk in the shadows – mystery is my trademark."
            )
        )
        if q7 == "I spread positive vibes and constructive memes like confetti!":
            score_total += 20
        elif q7 == "Mostly upbeat posts – I like to keep it friendly.":
            score_total += 15
        elif q7 == "I scroll through life, posting only when inspired.":
            score_total += 10
        else:
            score_total += 5

        # 8. Conflict Resolution Skills
        q8 = st.radio(
            "8. How do you handle conflicts?",
            (
                "I handle disputes like a zen master – calm and collected.",
                "I try to settle matters with cool-headed debates.",
                "I avoid conflict – silence is golden.",
                "I let frustrations simmer until they boil over."
            )
        )
        if q8 == "I handle disputes like a zen master – calm and collected.":
            score_total += 20
        elif q8 == "I try to settle matters with cool-headed debates.":
            score_total += 15
        elif q8 == "I avoid conflict – silence is golden.":
            score_total += 10
        else:
            score_total += 5

        # 9. Community Contributions
        q9 = st.radio(
            "9. How engaged are you with your community (e.g., reviews, feedback)?",
            (
                "I actively contribute – think of me as a one-person cheer squad!",
                "I drop a review or comment when something catches my eye.",
                "I contribute every now and then, on special occasions.",
                "I prefer to silently admire from afar."
            )
        )
        if q9 == "I actively contribute – think of me as a one-person cheer squad!":
            score_total += 20
        elif q9 == "I drop a review or comment when something catches my eye.":
            score_total += 15
        elif q9 == "I contribute every now and then, on special occasions.":
            score_total += 10
        else:
            score_total += 5

        # 10. Personal Style and Presentation
        q10 = st.radio(
            "10. How would you rate your personal style and presentation?",
            (
                "Always runway-ready – a true style icon!",
                "Chic and comfortable – I know how to dress the part.",
                "I have my own quirky style.",
                "I'm rocking the 'just rolled out of bed' chic."
            )
        )
        if q10 == "Always runway-ready – a true style icon!":
            score_total += 20
        elif q10 == "Chic and comfortable – I know how to dress the part.":
            score_total += 15
        elif q10 == "I have my own quirky style.":
            score_total += 10
        else:
            score_total += 5

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

if __name__ == "__main__":
    main()
