import streamlit as st
# import your ML libraries here
# from joblib import load   # if using .pkl or .joblib later

st.title("🌩️🌊🌪️ Disaster Prediction & Monitoring App")

# Sidebar navigation
option = st.sidebar.selectbox(
    'Choose a disaster type:',
    ('Cyclone Prediction', 'Earthquake Prediction', 'Flood Prediction', 'Rainfall Prediction')
)

# Cyclone Prediction
if option == 'Cyclone Prediction':
    st.markdown("## 🌪️ Cyclone Prediction")
    st.markdown("Provide the required inputs:")
    
    wind_speed = st.number_input("Enter Wind Speed (km/h)")
    pressure = st.number_input("Enter Atmospheric Pressure (hPa)")
    sea_temp = st.number_input("Enter Sea Surface Temperature (°C)")

    if st.button("Predict Cyclone"):
        # prediction = cyclone_model.predict([[wind_speed, pressure, sea_temp]])
        prediction = "✅ No Cyclone Detected. Weather is stable."
        st.success(f"Predicted Cyclone Category: {prediction}")

# Earthquake Prediction
elif option == 'Earthquake Prediction':
    st.markdown("## 🌎 Earthquake Prediction")
    st.markdown("Provide the required inputs:")
    
    magnitude = st.number_input("Enter Earthquake Magnitude")
    depth = st.number_input("Enter Depth (km)")
    distance_from_epicenter = st.number_input("Enter Distance from Epicenter (km)")

    if st.button("Predict Earthquake Impact"):
        # prediction = earthquake_model.predict([[magnitude, depth, distance_from_epicenter]])
        prediction = "✅ No Earthquake Detected."
        st.success(f"Predicted Earthquake Impact: {prediction}")

# Flood Prediction
elif option == 'Flood Prediction':
    st.markdown("## 🌊 Flood Prediction")
    st.markdown("Provide the required inputs:")
    
    rainfall_mm = st.number_input("Enter Recent Rainfall (mm)")
    river_level = st.number_input("Enter River Water Level (meters)")
    soil_saturation = st.number_input("Enter Soil Saturation (%)")

    if st.button("Predict Flood Risk"):
        # prediction = flood_model.predict([[rainfall_mm, river_level, soil_saturation]])
        prediction = "✅ No Harm Detected. Weather is stable."
        st.success(f"Predicted Flood Risk: {prediction}")

# Rainfall Prediction
elif option == 'Rainfall Prediction':
    st.markdown("## 🌧️ Rainfall Prediction")
    st.markdown("Provide the required inputs:")
    
    humidity = st.number_input("Enter Humidity (%)")
    temperature = st.number_input("Enter Temperature (°C)")
    pressure_rain = st.number_input("Enter Atmospheric Pressure (hPa)")

    if st.button("Predict Rainfall"):
        # prediction = rainfall_model.predict([[humidity, temperature, pressure_rain]])
        prediction = "✅ It's Safe"
        st.success(f"Predicted Rainfall Category: {prediction}")
