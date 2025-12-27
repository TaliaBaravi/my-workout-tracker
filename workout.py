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
# UPDATE: Your form section should now look like this
with st.form("workout_form"):
    ex_name = st.text_input("Exercise (e.g., Squat)")
    weight = st.number_input("Weight (kg)", min_value=0)
    reps = st.number_input("Reps", min_value=0)
    
    # NEW: Add the RIR slider
    rir = st.slider("Reps in Reserve (RIR)", 0, 5, 2, help="0 = failure, 5 = very easy")
    
    submit = st.form_submit_button("Log Workout")

if submit:
    # UPDATE: Add 'RIR' to your data collection
    new_data = pd.DataFrame([[pd.Timestamp.now().date(), ex_name, weight, reps, rir]], 
                            columns=["Date", "Exercise", "Weight", "Reps", "RIR"])
    
    # Save as before
    new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
    st.success(f"Logged {ex_name} with {rir} RIR!")

# Show the history
st.subheader("Recent History")
history_df = pd.read_csv(DATA_FILE)
st.dataframe(history_df.tail(10)) # Show last 10 entries
