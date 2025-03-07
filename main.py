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
        margin-top: 600px;
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
        "question": "Loki is trapped in a time loop, restarting every hour for centuries. If this continues for 10 years, how many loops has he experienced?",
        "answer": [56, 49, 48, 48, 48],  # ASCII for "87600"
        "amount": 2300,
        "loss": 0
    },
    {
        "question": "Loki learns that each decision creates 3 new timeline branches. Starting with one timeline, how many total timelines will exist after 5 decision cycles?",
        "answer": [50, 52, 51],  # ASCII for "243"
        "amount": -200,
        "loss": -500
    },
    {
        "question": "Arun investigates a murder network where victims form a graph based on Euclidean distance or hidden properties. Given victim nodes with coordinates—Node 1 (10,20), Node 2 (30,40), Node 3 (12,22), and Node 4 (32,42)—he must determine hidden relationships between (1,2), (2,3), (1,4), and (3,4) and predict a possible Node 5.",
        "answer": [50, 51],  # ASCII for "23" (strongest link)
        "amount": 2800,
        "loss": 0
    },
    {
        "question": "In Squid Game’s Tug of War, Team A (5 players, 70 kg each) and Team B (5 players, 75 kg each) pull with a force equal to their combined weight (mass × 9.8 m/s²). Determine which team exerts more force and by how much.",
        "answer": [50, 52, 53],  # ASCII for "245"
        "amount": 3500,
        "loss": 0
        
    },
    {
        "question": "In Squid Game Season 2’s Russian Roulette, a revolver has 6 chambers with 1 bullet. What is the probability that a player survives after pulling the trigger once at random?",
        "answer": [56, 51],  # ASCII for "83" (83.33%)
        "amount": -500,
        "loss":-700
    },
        {
        "question": "Calculate the average force exerted on the Titanic during its iceberg collision, given its mass (52,310,000 kg), speed (11.57 m/s), and stopping time (30 seconds) using **Force = (mass × velocity) / time**.",
        "answer": [50, 48, 49, 55, 51, 52, 53, 55],  # ASCII for "20173457"
        "amount": 4500,
        "loss": 0

    },
    {
        "question": "Calculate the probability of a random Titanic passenger surviving, given 2,224 people on board, 20 lifeboats, and each lifeboat holding 65 people at full capacity.",
        "answer": [53, 57],  # ASCII for "59"
        "amount": -700,
        "loss":-900
    },
    {
        "question": "In *Nanban*, a digital safe has a 4-digit passcode using unique digits (0-9) with no repetition. Calculate the total possible passcodes using **n! / (n-r)!**.",
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
        "question": "In *Vikram* (2022), a sniper fires a bullet at 900 m/s toward a target 600 meters away, passing through two glass panes that each reduce its speed by 10%. Calculate the bullet's final velocity upon reaching the target.",
        "answer": [55, 50, 57],  # ASCII for "729"
        "amount": -1500,
        "loss":2000
    },
    {
        "question": "In *Enthiran* (2010), Chitti runs on walls. Given a turn radius of 5 meters, calculate the minimum speed he needs to stay on the wall using **v = √(r × 9.8)**.",
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
    time_limit = 2  # seconds

# Function to validate answers using Groq API
    def validate_answer(index, user_answer):
        correct_answer = questions[index]["answer"]
        ans = ""
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
        st.markdown("<div style='margin-top: 700px;'></div>", unsafe_allow_html=True)  # Adjust margin as needed

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
