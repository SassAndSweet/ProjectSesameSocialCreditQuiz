import streamlit as st
import base64

# Load background image and encode as base64 for reliable embedding
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        return None

# Try local file first (works on Streamlit Cloud with repo image),
# fall back to raw GitHub URL as base64 isn't available
img_base64 = get_base64_image("sesame_background.png")

if img_base64:
    bg_image_css = f'url("data:image/png;base64,{img_base64}")'
else:
    bg_image_css = 'url("https://raw.githubusercontent.com/SassAndSweet/ProjectSesameSocialCreditQuiz/main/sesame_background.png")'

st.markdown(f"""
<style>
    /* Import Noto Serif SC from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&display=swap');

    /* Watermark background image via pseudo-element on stApp */
    .stApp {{
        position: relative;
        background-color: #f5f5f0;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: {bg_image_css};
        background-size: cover;
        background-position: center;
        opacity: 0.12;
        z-index: 0;
        pointer-events: none;
    }}

    /* Push all content above the watermark */
    .stApp > * {{
        position: relative;
        z-index: 1;
    }}

    /* Title */
    .stApp h1 {{
        color: #00008B !important;
        font-weight: bold !important;
        font-family: 'Noto Serif SC', serif !important;
    }}

    /* Subtitle / intro text */
    .stApp > div p {{
        color: #1a1a2e !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }}

    /* Question labels (radio group headers) */
    .stRadio label span {{
        color: #00008B !important;
        font-weight: bold !important;
        font-size: 15px !important;
        font-family: 'Noto Serif SC', serif !important;
    }}

    /* Radio option text */
    .stRadio div label {{
        color: #1a1a2e !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }}

    /* Section headers (h2, h3) */
    .stApp h2, .stApp h3 {{
        color: #00008B !important;
        font-weight: bold !important;
        font-family: 'Noto Serif SC', serif !important;
    }}

    /* Results / benefits text */
    .stMarkdown p {{
        color: #1a1a2e !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }}

    /* Submit button */
    div[data-testid="stFormSubmitButton"] button,
    div[data-testid="stFormSubmitButton"] button * {{
        background-color: #00008B !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        padding: 10px 24px !important;
        border-radius: 6px !important;
        font-size: 16px !important;
        cursor: pointer !important;
        transition: transform 0.1s ease, box-shadow 0.1s ease, background-color 0.15s ease !important;
        box-shadow: 0 2px 6px rgba(0, 0, 139, 0.4) !important;
    }}
    div[data-testid="stFormSubmitButton"] button:hover {{
        background-color: #0000a3 !important;
        box-shadow: 0 4px 10px rgba(0, 0, 139, 0.5) !important;
        transform: translateY(-1px) !important;
    }}
    div[data-testid="stFormSubmitButton"] button:active {{
        transform: scale(0.95) translateY(1px) !important;
        box-shadow: 0 1px 3px rgba(0, 0, 139, 0.3) !important;
        background-color: #000066 !important;
    }}

    /* Retake Quiz button */
    .stButton button,
    .stButton button * {{
        background-color: #00008B !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        padding: 10px 24px !important;
        border-radius: 6px !important;
        font-size: 16px !important;
        cursor: pointer !important;
        transition: transform 0.1s ease, box-shadow 0.1s ease, background-color 0.15s ease !important;
        box-shadow: 0 2px 6px rgba(0, 0, 139, 0.4) !important;
    }}
    .stButton button:hover {{
        background-color: #0000a3 !important;
        box-shadow: 0 4px 10px rgba(0, 0, 139, 0.5) !important;
        transform: translateY(-1px) !important;
    }}
    .stButton button:active {{
        transform: scale(0.95) translateY(1px) !important;
        box-shadow: 0 1px 3px rgba(0, 0, 139, 0.3) !important;
        background-color: #000066 !important;
    }}

    /* Results section - smooth slide-in */
    @keyframes slideIn {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    .results-section {{
        animation: slideIn 0.5s ease forwards;
    }}

    /* Confetti canvas */
    #confetti-canvas {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 999;
    }}
</style>
""", unsafe_allow_html=True)


# --- Confetti + scroll JS (injected once on results render) ---
CONFETTI_AND_SCROLL_JS = """
<script>
(function() {
    // --- AUTO-SCROLL to results ---
    var resultsEl = document.getElementById('results-anchor');
    if (resultsEl) {
        resultsEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // --- CONFETTI (only fires if gold-confetti anchor exists) ---
    var confettiTrigger = document.getElementById('gold-confetti-trigger');
    if (!confettiTrigger) return;

    var canvas = document.createElement('canvas');
    canvas.id = 'confetti-canvas';
    document.body.appendChild(canvas);
    var ctx = canvas.getContext('2d');

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    var pieces = [];
    var colors = ['#FFD700','#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FFEAA7','#DDA0DD','#98D8C8','#F7DC6F','#BB8FCE'];

    function Piece(x, y) {
        this.x = x;
        this.y = y;
        this.vx = (Math.random() - 0.5) * 12;
        this.vy = (Math.random() - 3) * 10;
        this.gravity = 0.15;
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.size = Math.random() * 8 + 4;
        this.rotation = Math.random() * Math.PI * 2;
        this.rotSpeed = (Math.random() - 0.5) * 0.3;
        this.shape = Math.random() > 0.5 ? 'rect' : 'circle';
        this.alpha = 1;
    }

    // Burst from top-center
    function burst() {
        var cx = canvas.width / 2;
        var cy = canvas.height * 0.25;
        for (var i = 0; i < 150; i++) {
            pieces.push(new Piece(cx + (Math.random()-0.5)*60, cy + (Math.random()-0.5)*60));
        }
    }
    burst();

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (var i = pieces.length - 1; i >= 0; i--) {
            var p = pieces[i];
            p.vy += p.gravity;
            p.x += p.vx;
            p.y += p.vy;
            p.rotation += p.rotSpeed;
            p.vx *= 0.995;

            if (p.y > canvas.height) {
                p.alpha -= 0.05;
            }
            if (p.alpha <= 0) {
                pieces.splice(i, 1);
                continue;
            }

            ctx.save();
            ctx.globalAlpha = p.alpha;
            ctx.fillStyle = p.color;
            ctx.translate(p.x, p.y);
            ctx.rotate(p.rotation);
            if (p.shape === 'rect') {
                ctx.fillRect(-p.size/2, -p.size/2, p.size, p.size * 0.6);
            } else {
                ctx.beginPath();
                ctx.arc(0, 0, p.size/2, 0, Math.PI * 2);
                ctx.fill();
            }
            ctx.restore();
        }

        if (pieces.length > 0) {
            requestAnimationFrame(animate);
        } else {
            canvas.remove();
        }
    }
    animate();
})();
</script>
"""


def main():
    st.title("Sesame Credit Quiz")
    st.write("Answer the following questions to find out what exclusive social perks you might earn!")

    with st.form("quiz_form"):
        score_total = 0
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

        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        predicted_credit = 350 + int((score_total / max_total) * 600)

        # Scroll anchor — JS will smooth-scroll here
        st.markdown('<div id="results-anchor"></div>', unsafe_allow_html=True)

        # Results wrapped in slide-in animation
        st.markdown('<div class="results-section">', unsafe_allow_html=True)
        st.markdown("---")
        st.write(f"**Your total score is:** {score_total} out of {max_total}")
        st.write(f"**Predicted Social Credit Score:** {predicted_credit}")

        is_gold = False
        if predicted_credit >= 900:
            benefits = (
                "VIP Access: You're a social superstar!\n"
                "Enjoy exclusive perks like red carpet service at coffee shops, priority invites to legendary parties, "
                "and an honorary title as the 'Mogul of Mingling.'"
            )
        elif predicted_credit >= 750:
            is_gold = True
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
        st.markdown('</div>', unsafe_allow_html=True)

        # Gold Tier confetti trigger anchor
        if is_gold:
            st.markdown('<div id="gold-confetti-trigger"></div>', unsafe_allow_html=True)

        # Inject JS — always scrolls, confetti only if Gold trigger exists
        st.markdown(CONFETTI_AND_SCROLL_JS, unsafe_allow_html=True)

        if st.button("Retake Quiz"):
            st.rerun()

if __name__ == "__main__":
    main()
