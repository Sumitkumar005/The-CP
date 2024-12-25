import streamlit as st
import json

# Load student progress data from JSON
def load_progress_data():
    with open('data/progress.json') as f:
        return json.load(f)

def progress_tracker_page():
    st.title("Progress Tracker")
    
    progress_data = load_progress_data()
    
    st.subheader(f"Total Problems Solved: {progress_data['total_solved']}")
    st.subheader(f"Current Rating: {progress_data['current_rating']}")
    
    # Display progress in categories
    st.markdown("**Topics Covered:**")
    for topic, status in progress_data['topics'].items():
        st.write(f"{topic}: {status}%")
    
    st.button("Update Progress", key="update")