import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="MetroEye Dashboard", layout="centered")

st.title("🚉 MetroEye: Live Occupancy")
st.write("Real-time crowd monitoring for Coach #03")

# Create a placeholder for live updates
placeholder = st.empty()

while True:
    try:
        # Read the data from the CSV file
        df = pd.read_csv('live_data.csv')
        count = df['count'].iloc[0]
        
        with placeholder.container():
            # Logic for Status
            if count < 10:
                st.success(f"### Status: SEATS AVAILABLE 🟢")
                color = "green"
            elif count < 25:
                st.warning(f"### Status: STANDING ROOM ONLY 🟡")
                color = "orange"
            else:
                st.error(f"### Status: HEAVILY CROWDED 🔴")
                color = "red"
            
            # Big Metric Display
            st.metric(label="Current Passengers", value=count)
            
            # Progress Bar for Visualizing Capacity
            capacity_pct = min(count / 40, 1.0) # Assuming 40 is max
            st.progress(capacity_pct)
            
    except:
        st.info("Waiting for Vision Engine to start...")
    
    time.sleep(1) # Refresh every second