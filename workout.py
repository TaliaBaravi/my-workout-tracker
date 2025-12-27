import streamlit as st
import pandas as pd
import os

# The name of our "database" file
DATA_FILE = "workout_logs.csv"

st.title("🏋️ Workout Tracker")
# Add a slider to track your energy level
energy = st.slider("How is your energy level today?", 1, 10, 5)

if energy > 8:
    st.balloons() # This adds a fun animation!
    st.write("🔥 You're on fire! Time for a PR (Personal Record)!")
elif energy < 4:
    st.write("🥤 Take it easy today. Focus on form.")
else:
    st.write("💪 Solid energy. Let's get to work!")

# Create the file if it doesn't exist
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Exercise", "Weight", "Reps"])
    df.to_csv(DATA_FILE, index=False)

# User Input
with st.form("workout_form"):
    ex_name = st.text_input("Exercise (e.g., Squat)")
    weight = st.number_input("Weight (kg)", min_value=0)
    reps = st.number_input("Reps", min_value=0)
    submit = st.form_submit_button("Log Workout")

if submit:
    # Append new data to the CSV
    new_data = pd.DataFrame([[pd.Timestamp.now().date(), ex_name, weight, reps]], 
                            columns=["Date", "Exercise", "Weight", "Reps"])
    new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
    st.success(f"Logged {ex_name}!")

# Show the history
st.subheader("Recent History")
history_df = pd.read_csv(DATA_FILE)
st.dataframe(history_df.tail(10)) # Show last 10 entries