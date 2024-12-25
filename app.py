import streamlit as st
import json
import time
import requests
import matplotlib.pyplot as plt
import numpy as np

import os

st.set_page_config(page_title="Infinity Loops - CP Community", page_icon=":rocket:", layout="wide")

# Apply custom CSS
def apply_custom_css():
    with open(os.path.join("assets", "styles.css")) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function to apply CSS
apply_custom_css() 

# Your Codeforces API key and secret (use them to authenticate API calls)
API_KEY = 'baf2b3a0f4a4c8ed5e70ed9db0087e4d56bafdec'
API_SECRET = 'b6e698b911e886c4015f61be7d3569a8db7e728f'

# App Configuration

# Function to Load JSON data
def load_data():
    with open("data/group_data.json") as f:
        group_data = json.load(f)
    return group_data

# Function to fetch user info from Codeforces API using the API key
@st.cache_data
def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    
    headers = {
        "X-API-KEY": API_KEY,
        "X-API-SECRET": API_SECRET
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()

    if data["status"] == "OK":
        user_data = data["result"][0]
        return {
            "username": user_data["handle"],
            "rating": user_data.get("rating", "Not Available"),
            "rank": user_data.get("rank", "Not Ranked"),
            "solved_problems": user_data.get("solved_problems_count", 0),
            "contribution": user_data.get("contribution", "Not Available")
        }
    else:
        return None

# Function to generate a simple leaderboard (static for now)
def generate_leaderboard():
    st.header("Leaderboard")
    leaderboard_data = [
        {"username": "User1", "rating": 2500, "solved_problems": 200},
        {"username": "User2", "rating": 2400, "solved_problems": 180},
        {"username": "User3", "rating": 2300, "solved_problems": 160},
        {"username": "User4", "rating": 2200, "solved_problems": 150},
        {"username": "User5", "rating": 2100, "solved_problems": 140}
    ]
    
    for user in leaderboard_data:
        st.write(f"{user['username']} - Rating: {user['rating']} - Solved Problems: {user['solved_problems']}")

# Function to display achievements for the user
def display_achievements(user_info):
    st.header("Your Achievements")
    
    achievements = []
    
    if user_info['solved_problems'] > 100:
        achievements.append("🎉 Solved 100 problems!")
    
    if user_info['rating'] > 2000:
        achievements.append("🌟 Mastered Codeforces with a rating over 2000!")
    
    if achievements:
        for achievement in achievements:
            st.write(achievement)
    else:
        st.write("No achievements yet! Keep solving!")

# Welcome Section
def welcome_section():
    st.title("Welcome to Infinity Loops - Competitive Programming Group")
    st.image("assets/images/logo.png", width=300)
    st.subheader("Where Problem Solvers Thrive!")
    st.write("""
    **Core Objective**: We focus on enhancing cognitive skills and problem-solving abilities.
    
    - Commitment of 5-6 months for skill enhancement.
    - Goal: Develop cognitive and problem-solving proficiency.
    - Participate in contests, upsolve problems, and track your progress.
    """)
    st.markdown("[Join Our Group](https://chat.whatsapp.com/EgEOYmZFjAEIFMgcWKB9nl)")

# Resources Section
def resources_section():
    st.header("Learning Resources")
    st.write("""
    Check out these platforms to hone your skills and keep improving:
    """)
    st.markdown("""
    - [LeetCode](https://leetcode.com/) : Solve problems to sharpen your skills.
    - [Codeforces](https://codeforces.com/) : Compete in real-time coding contests.
    - [CodeChef](https://www.codechef.com/) : Improve your problem-solving abilities.
    - [AtCoder](https://atcoder.jp/) : Participate in international coding challenges.
    - [HackerRank](https://www.hackerrank.com/) : Practice algorithms and data structures.
    """)

# Progress Tracker Section
import streamlit as st
import matplotlib.pyplot as plt

def progress_tracker_section():
    st.header("Your Progress")
    st.write("Keep track of your growth and achievements!")

    # Placeholder for progress data (can be connected to a backend)
    progress = {
        "Problems Solved": 25,
        "Contests Participated": 5,
        "Streak": "7 days of continuous coding!"  # This is a string
    }
    
    st.write(f"**Problems Solved**: {progress['Problems Solved']}")
    st.write(f"**Contests Participated**: {progress['Contests Participated']}")
    st.write(f"**Streak**: {progress['Streak']}")

    st.write("### Progress Chart")
    
    # Create a new dictionary excluding non-numeric values
    numeric_progress = {
        key: value for key, value in progress.items() if isinstance(value, (int, float))
    }
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(numeric_progress.keys(), numeric_progress.values(), color='blue')
    st.pyplot(fig)

    # User Profile (Integration with Codeforces API)
    handle = st.text_input("Enter your Codeforces Handle to fetch profile stats:")
    if handle:
        user_info = get_user_info(handle)

        if user_info:
            st.subheader(f"Username: {user_info['username']}")
            st.write(f"Rating: {user_info['rating']}")
            st.write(f"Rank: {user_info['rank']}")
            st.write(f"Solved Problems: {user_info['solved_problems']}")
            st.write(f"Contribution: {user_info['contribution']}")
            display_achievements(user_info)
        else:
            st.error("User  not found. Please check the handle and try again.")

# Motivation Section
def motivation_section():
    st.header("Stay Motivated!")
    st.write("""
    Competitive programming is a journey of constant improvement. Here are some motivational quotes to fuel your coding adventure:
    """)
    
    motivational_quotes = [
        '"The only way to learn a new programming language is by writing programs in it." — Dennis Ritchie',
        '"In theory, theory and practice are the same. In practice, they’re not." — Yogi Berra',
        '"It’s not that I’m so smart, it’s just that I stay with problems longer." — Albert Einstein'
    ]
    
    for quote in motivational_quotes:
        st.write(f"- {quote}")

# Daily Challenges Section
def daily_challenges_section():
    st.header("Daily Coding Challenges")
    st.write("Solve one challenge a day to keep improving!")
    
    challenges = [
        "Find the nth Fibonacci number.",
        "Sort a list of integers using Merge Sort.",
        "Implement a binary search algorithm."
    ]
    st.write(f"**Today's Challenge**: {challenges[time.localtime().tm_yday % len(challenges)]}")

# Group Info Section
def group_info_section():
    st.header("About Infinity Loops - CP Group")
    st.write("""
    The **Infinity Loops - CP Group** is designed to help you grow as a coder. We are committed to:
    - Helping you build resilience through challenging problems.
    - Improving your decision-making and project management skills.
    - Encouraging teamwork and personal growth.
    """)
    st.write("""
    **Our Approach**:
    - **Independent Problem-Solving**: Minimal curated content. You’ll learn by solving problems.
    - **Practice-Focused Learning**: Solve problems on platforms like LeetCode and Codeforces.
    """)

# Footer Section
def footer_section():
    st.markdown("""
    ----
    **Follow Us**: 
    - [Linkedin](https://www.linkedin.com/posts/theinfinityloops_competitiveprogramming-codingchallenges-maangprep-activity-7273282337767923712-XsIA?utm_source=share&utm_medium=member_desktop)
    """)
    st.write("© 2024 Infinity Loops - CP Group. All rights reserved.")

# Navigation
def show_navigation():
    st.sidebar.title("Navigation")
    navigation_options = ["Home", "Progress Tracker", "Resources", "Motivation", "Group Info", "Leaderboard"]
    selection = st.sidebar.radio("Select a Page", navigation_options)

    if selection == "Home":
        welcome_section()
    elif selection == "Progress Tracker":
        progress_tracker_section()
    elif selection == "Resources":
        resources_section()
    elif selection == "Motivation":
        motivation_section()
    elif selection == "Group Info":
        group_info_section()
    elif selection == "Leaderboard":
        generate_leaderboard()
    
    footer_section()

# Main Function
def main():
    show_navigation()

if __name__ == "__main__":
    main()