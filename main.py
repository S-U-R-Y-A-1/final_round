import streamlit as st
import time
from groq import Groq
import base64

import requests

def get_gif_base64(url):
    response = requests.get(url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode()
    else:
        st.error("Failed to load GIF from GitHub.")
        return None

# GitHub raw URL of the GIF
gif_url = "https://raw.githubusercontent.com/S-U-R-Y-A-1/final_round/main/anode-avaxnode.gif"
gif_base64 = get_gif_base64(gif_url)

# Use session state to track first load
if "show_gif" not in st.session_state:
    st.session_state.show_gif = True  # Show GIF initially
    st.session_state.start_time = time.time()  # Store the start time

# Display GIF only if it was successfully loaded
if gif_base64 and st.session_state.show_gif and (time.time() - st.session_state.start_time < 7):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/gif;base64,{gif_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}

        .title-box {{
    position: absolute;
    width: 600px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #FFFFFF; /* Solid white background */
    color: black;
    padding: 30px 50px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    margin-top: 200px;
    border: 2px solid black;
    opacity: 0;  /* Initially hidden */
    animation: fadeIn 1s ease-in-out forwards;
    animation-delay: 4s;  /* Delay title appearance by 4 seconds */
}}

.title-box h1, .title-box p {{
    color: gold;
    text-shadow: 0 0 10px gold, 0 0 20px #FFD700, 0 0 30px #FFA500, 0 0 40px #FF8C00;
}}

        </style>

        <div class="title-box">
            <h1 style="color: black;">WELCOME TO THE VAULT OF FORTUNE</h1>
            <p>Let the AI Heist Begin!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Wait for 7 seconds
    time.sleep(7)

    # Refresh the page
    st.session_state.show_gif = False
    st.rerun()


else:
# Set page config
    st.set_page_config(page_title="Quiz Game", page_icon="🎯", layout="wide")

# ✅ Load the uploaded image
    image_url = "https://raw.githubusercontent.com/S-U-R-Y-A-1/final_round/main/background.jpg"

# ✅ Function to fetch image from URL and convert to Base64
    def get_base64_from_url(image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
        else:
            st.error("Failed to load background image from GitHub.")
            return None

# ✅ Convert image to Base64
    image_base64 = get_base64_from_url(image_url)

# ✅ Custom CSS for Full-Page Background    
    background_css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{image_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)
    box_css = """
<style>
    .centered-box {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: 0px;
    margin-top: 100px;
    background-color: white; /* Fully solid white */
    border: 2px solid black;
    transform: translate(-50%, -50%);
    padding: 40px 60px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    width: 50%;
    
    word-wrap: break-word;
    overflow-wrap: break-word;
    white-space: normal;
    overflow: hidden;
}



    
    .centered-box1 {
        position: absolute;
        width: 300px;
        height: 250px;
        top: 50%;
        left: 50%;
        margin-left: 0px;
        margin-top: 300px;
        background-color: white; /* Changed to solid white */
    border: 2px solid black; /* Added black border */

        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.7);
        color:black;
        padding: 40px 60px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        width: 50%;
         word-wrap: break-word; /* Ensures long words wrap */
    overflow-wrap: break-word; /* Ensures text doesn't overflow */
    white-space: normal; /* Allows text wrapping */
    overflow: hidden; /* Hides any overflowing content */
    }
    .centered-box2 {
        position: absolute;
        width: 300px;
        height: 200px;
        top: 50%;
        left: 50%;
        margin-left: 0px;
        margin-top: 450px;
        background-color: white; /* Changed to solid white */
    border: 2px solid black; /* Added black border */

        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.2);
        padding: 40px 60px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        width: 50%;
    }
    
    

    .timer {
        font-size: 20px;
        font-weight: bold;
        color: #FFD700;
    }
    .next-btn {
        background-color: #FFD700 !important;
        color: black !important;
        font-size: 18px !important;
        border-radius: 5px !important;
    }
</style>
"""

    st.markdown(box_css, unsafe_allow_html=True)  # Open Glassmorphic Box
    

# ✅ UI Content



# Initialize Groq client
    client = Groq(api_key="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")
# Define quiz questions in a dictionary
questions = [
    
    {
        "question": "Loki’s Time Loop Mystery:\n\nLoki finds himself trapped in a time loop inside the TVA (Time Variance Authority). Every time he tries to stop the Temporal Loom from overloading, he fails and is sent back to the same moment—again and again. He soon realizes that he must keep repeating the loop until he learns exactly how to fix the problem.\n\nDuring one loop, OB (Ouroboros) tells Loki that he has been in this loop for centuries, trying to figure it out.\n\nIf Loki has been in the loop for centuries, and assuming he restarts the loop once every hour, what is the minimum number of loops he must have gone through over 10 years?\n\n(Consider 1 year = 365 days, ignoring leap years.)\n\nWin Amount : $2300",
        "answer": [56, 49, 48, 48, 48],  # ASCII for "87600"
        "amount": 2300,
        "loss": 0
    },
    {
        "question": "Loki’s Multiversal Branching Dilemma:\n\nAt the TVA, Loki learns that every decision creates a branching timeline. The Temporal Loom is designed to manage these branches, but if too many appear at once, the system becomes unstable.\n\nWhile analyzing TVA records, Loki discovers that each person’s single choice can create 3 possible new branches. If those branches continue creating more branches in the same pattern, the number of timelines grows exponentially.\n\nIf Loki starts with one timeline and allows branching to continue for 5 decision cycles, how many total timelines will exist at the end?\n\n(Each timeline splits into 3 new branches per cycle.)\n\nWin Amount : $2500",
        "answer": [50, 52, 51],  # ASCII for "243"
        "amount": -200,
        "loss": -500
    },
    {
        "question": "Graph Theory – Hidden Relationship in the Murder Network:\n\nArun, the investigator, discovers that the killer has been using a hidden graph structure to determine the pattern of murders. The victims are not randomly chosen; instead, their locations form a mathematical network, where each victim is a node, and certain victims are connected based on a hidden rule.\n\nThe known relationships are:\n\nNode 1 (Victim 1) is directly connected to Node 3 (Victim 3)\nNode 2 (Victim 2) is directly connected to Node 4 (Victim 4)\n\nEach victim's location is given in GPS coordinates:\nNode 1 (Victim 1): (10, 20)\nNode 2 (Victim 2): (30, 40)\nNode 3 (Victim 3): (12, 22)\nNode 4 (Victim 4): (32, 42)\n\nArun notices that certain high-value links (strong relationships) exist in the network, meaning that two victims are more likely to be related if their Euclidean distance is smaller or if they share a hidden numerical property.\n\nGiven this information, find out whether there is a hidden relationship between:\n\n- Node 1 and Node 2\n- Node 2 and Node 3\n- Node 1 and Node 4\n- Node 3 and Node 4\n\nAdditionally, if there is a strong connection between two nodes, predict which Node 5 could be added to this network.\n\nWin Amount : $2800",
        "answer": [50, 51],  # ASCII for "23" (strongest link)
        "amount": 2800,
        "loss": 0
    },
    {
        "question": "The Doll’s Hidden Evidence:\n\nDuring the investigation of a serial killer case, Arun finds an old, tattered doll near the latest crime scene. The forensic team suspects that the killer is leaving behind these dolls as a signature. Upon closer inspection, Arun notices something unusual—the doll’s button eyes are positioned in an asymmetric way, and its stitches form a specific angle.\n\nWhile examining the past crime scenes, he realizes that every murder site had a similar doll, and the position of its button eyes always points toward the next crime scene.\n\nArun takes measurements from the doll’s button positions at the latest crime scene and finds the following:\n\nLeft Eye Coordinate: (5, 10)\nRight Eye Coordinate: (15, 20)\n\nHe remembers that in the last case, the killer had positioned the doll’s eyes such that the midpoint between them pointed towards the next location. If this pattern continues, where should the police search next?\n\nWin Amount : $3000",
        "answer": [49, 48, 49, 53],  # ASCII for "10,15"
        "amount": -300,
        "loss":-500,
        
    },
    {
        "question": "Squid Game – Tug of War Physics Question:\n\nIn Squid Game, the Tug of War game is a battle of strength, strategy, and physics. Each team must pull the rope with enough force to overpower the opposing team and make them fall off the platform.\n\nTwo teams are competing in Tug of War:\n• Team A has 5 players, each with an average mass of 70 kg.\n• Team B has 5 players, each with an average mass of 75 kg.\n• Each team pulls with a force equal to their combined weight (mass × gravity).\n• Assume gravitational acceleration (g) = 9.8 m/s².\n\nWhich team exerts more force (Difference), and by how much?\n\nWin Amount : $0",
        "answer": [50, 52, 53],  # ASCII for "245"
        "amount": 3500,
        "loss": 0
        
    },
    {
        "question": "Squid Game Season 2 – Russian Roulette Probability:\n\nIn Squid Game Season 2, one of the deadly games is a version of Russian Roulette, where players must pull the trigger of a revolver with a single bullet loaded in one of the chambers.\n\nA revolver has 6 chambers, but only 1 chamber contains a bullet. If a player pulls the trigger once at random, what is the probability that they survive (i.e., the chamber is empty)?\n\nWin Amount : $0",
        "answer": [56, 51],  # ASCII for "83" (83.33%)
        "amount": -500,
        "loss":-700
    },
        {
        "question": "Titanic – Iceberg Collision Impact Calculation:\n\nIn Titanic (1997), the ship collided with an iceberg, leading to one of the most infamous maritime disasters in history. Let's calculate the force of impact when the Titanic struck the iceberg.\n\nThe Titanic had a mass of 52,310 metric tons (52,310,000 kg) and was moving at 22.5 knots (11.57 m/s) when it hit the iceberg. Assuming the ship came to a stop in 30 seconds after impact, what was the average force exerted on the Titanic during the collision?\n\n(Hint: Use the formula **Force = (mass × velocity) / time**)\n\nWin Amount : $0",
        "answer": [50, 48, 49, 55, 51, 52, 53, 55],  # ASCII for "20173457"
        "amount": 4500,
        "loss": 0

    },
    {
        "question": "Titanic – Lifeboat Survival Probability:\n\nIn Titanic (1997), there were not enough lifeboats for all passengers, leading to a highly unequal survival rate. Let's analyze the probability of survival based on lifeboat capacity.\n\nThe Titanic had 2,224 passengers and crew on board but only 20 lifeboats, each capable of holding 65 people. If a random passenger tried to board a lifeboat, what was their probability of survival, assuming all lifeboats were filled to capacity?\n\nWin Amount : $0",
        "answer": [53, 57],  # ASCII for "59"
        "amount": -700,
        "loss":-900
    },
    {
        "question": "Nanban – Cracking the Locker Code 🔐\n\nIn the movie Nanban, Vijay (Pari) tries to steal the question paper for his friend. Imagine that the question paper is locked inside a digital safe, which is protected by a 4-digit passcode.\n\n**Question:** Finding the Total Possible Passcodes\nThe passcode consists of 4 unique digits (0-9), meaning repetition is not allowed.\n\nHow many different 4-digit passcodes can be created under this rule?\n\n(Hint: Use the formula **n! / (n-r)!**)\n\nWin Amount : $0",
        "answer": [53, 48, 52, 48],  # ASCII for "5040"
        "amount": 5000,
        "loss": 0

    },
    {
        "question": "Nanban – Maximum Time Required to Crack the Code ⏳\n\nIf a wrong attempt results in a **10-second delay** before retrying, what is the maximum time required to try all possible passcodes? (Answer in hours)\n\nWin Amount : $0",
        "answer": [49, 52],  # ASCII for "14"
        "amount": -1000,
        "loss":-1200
    },
    {
        "question": "A drone in Interstellar flew at 150 km/h for 10 years. Calculate the total distance it traveled.\n\nWin Amount : $3500",
        "answer": [49, 51, 49, 48, 48, 48, 48, 48],  # ASCII for "13140000"
        "amount": 3500,
        "loss": 0

    },
    {
        "question": "Vikram Movie – Bullet Trajectory Calculation:\n\nIn Vikram (2022), there are several high-intensity action sequences where bullets travel through multiple objects before hitting the target. One of the most thrilling moments involves calculating the trajectory of a bullet to ensure a precise kill.\n\nA sniper fires a bullet at 900 m/s towards an enemy 600 meters away. However, the bullet must pass through two glass panes, which each reduce the bullet’s speed by 10% upon impact.\n\nWhat is the final velocity of the bullet when it reaches the target?\n\n(Ignore air resistance and assume each glass pane reduces the speed before the bullet continues its path.)\n\nWin Amount : $7500",
        "answer": [55, 50, 57],  # ASCII for "729"
        "amount": -1500,
        "loss":2000
    },
    {
        "question": "Enthiran Movie – Speed Required to Run on Walls:\n\nIn Enthiran (2010), Chitti the Robot performs incredible stunts, including running on walls. To achieve this, he must generate enough centripetal force to counteract gravity.\n\nIf the radius of his running path (his turn curve) is 5 meters, what minimum speed (in m/s) does he need to maintain to stay on the wall without falling? hint: use the formula, v = square root( r * 9.8 )\n\nWin Amount : $8500",
        "answer": [55],  # ASCII for "70" (7 m/s)
        "amount": 8500,
        "loss": 0

    }
]

# Initialize session state variables
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = []
    if "validation_results" not in st.session_state:
        st.session_state.validation_results = []
    if "timer_running" not in st.session_state:
        st.session_state.timer_running = False
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    if "remaining_time" not in st.session_state:
        st.session_state.remaining_time = 10  # Set initial timer

# Time limit per question
    time_limit = 180  # seconds

# Function to validate answers using Groq API
    def validate_answer(index, user_answer):
        correct_answer = questions[index]["answer"]
        ans = ""
        if index == 2:
            for i in correct_answer:
                ans += str(ord(i))
        elif index == 5:
            ans = str(bin(correct_answer)[2:])
        else:
            for i in correct_answer:
                ans += chr(int(i))
                
        correct_answer = ans
    # If answer is already known, compare directly
        if user_answer.strip().lower() == correct_answer.lower():
            return "Correct"

    # Otherwise, send to Groq API for validation
        validation_prompt = """
        Given the question: "{questions[index]['question']}"
        The correct answer is: "{correct_answer}"
        The user answered: "{user_answer}"
        Check whether the correct answer is presented in the user answer.
        Respond only with "Correct" or "Incorrect".
        """

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": validation_prompt}],
            temperature=0,
            max_completion_tokens=20,
            top_p=1,
            stream=False,
        )

        result = completion.choices[0].message.content.strip()
        return result  # Either 'Correct ✅' or 'Incorrect ❌'
    # ✅ Custom CSS to position text input at the bottom
    input_css = """
<style>
    .input-container {
        position: absolute;
        bottom: 15%;  /* Adjust this value to move it up/down */
        left: 50%;
        margin-left: 0px;
        margin-top: 150px;
        transform: translateX(-50%);
        background: rgba(255, 255, 255, 0.2); /* Glassmorphic effect */
        padding: 10px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        width: 50%;
        z-index: 100;  /* Ensures it stays on top */
    }
    
    
</style>
"""

# Display the quiz
    if st.session_state.current_question < len(questions):
        
        q = questions[st.session_state.current_question]

    
        st.markdown(
    f'<div class="centered-box">'
    f'<h2 style="color: black; font-weight: bold;">Question {st.session_state.current_question + 1}:</h2>'
    f'</div>',
    unsafe_allow_html=True
        )
        st.markdown(f'<div class="centered-box1"><p style="color: black; font-weight: bold;">{q["question"]}</p></div>', unsafe_allow_html=True)
        st.markdown(input_css, unsafe_allow_html=True)

# ✅ Wrap st.text_input inside a div positioned at the bottom
        st.markdown("<div style='margin-top: 375px;'></div>", unsafe_allow_html=True)  # Adjust margin as needed

    # User input box
        user_answer = st.text_input("Your Answer:", key=f"answer_{st.session_state.current_question}")

    # Countdown Timer Display
        countdown_placeholder = st.empty()

    # Timer logic
        if not st.session_state.timer_running:
            st.session_state.start_time = time.time()
            st.session_state.remaining_time = time_limit
            st.session_state.timer_running = True

        elapsed_time = time.time() - st.session_state.start_time
        st.session_state.remaining_time = max(0, int(time_limit - elapsed_time))

        countdown_placeholder.write(f"⏳ Time left: *{st.session_state.remaining_time} seconds*")

    # Refresh the timer every second
        if st.session_state.remaining_time > 0:
            time.sleep(10)
            st.rerun()  # ✅ Fixed: Uses st.rerun() instead of deprecated st.experimental_rerun()

    # Auto-move to next question when timer runs out
        if st.session_state.remaining_time == 0:
            st.session_state.user_answers.append(user_answer if user_answer else "No answer")
            validation_result = validate_answer(st.session_state.current_question, user_answer)
            st.session_state.validation_results.append(validation_result)
            st.session_state.current_question += 1
            st.session_state.timer_running = False  # Reset timer for next question
            st.session_state.remaining_time = time_limit  # Reset timer for next question
            st.rerun()  # ✅ Fixed: Uses st.rerun()

    # Manual "Next" button
        if st.button("Next") and user_answer:
            st.session_state.user_answers.append(user_answer)
            validation_result = validate_answer(st.session_state.current_question, user_answer)
            st.session_state.validation_results.append(validation_result)
            st.session_state.current_question += 1
            st.session_state.timer_running = False  # Reset timer for next question
            st.session_state.remaining_time = time_limit  # Reset timer for next question
            st.rerun()  # ✅ Fixed: Uses st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


    else:
        st.write("### Quiz Completed! 🎉")
        st.write("Your Answers:", st.session_state.user_answers)
        st.write("### Validation Results:")
        points = 2000
        for i, result in enumerate(st.session_state.validation_results):
            if result == "Correct":
                points += questions[i]["amount"]
            else:
                points += questions[i]["loss"]
                
            st.write(f"Question {i+1}: {result}")
        st.write(f"Points : ${points}")
