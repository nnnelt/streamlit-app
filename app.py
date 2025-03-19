import math
import streamlit as st

st.title("📡 Wireless Link Budget & Fresnel Zone Calculator")

# User Inputs
P_t_mW = st.number_input("Transmit Power (mW)", value=9.0)
G_t = st.number_input("Transmit Antenna Gain (dB)", value=10.0)
G_r = st.number_input("Receive Antenna Gain (dB)", value=6.0)
d_km = st.number_input("Distance (km)", value=10.9)
f_GHz = st.number_input("Frequency (GHz)", value=2.5)
P_min_dBm = st.number_input("Minimum Required Signal Strength (dBm)", value=-100.0)

# Convert units
d = d_km * 10**3
f = f_GHz * 10**9
c = 3 * 10**8

# Convert P_t from mW to dBm
P_t_dBm = 10 * math.log10(P_t_mW)

# Calculate Free-Space Path Loss (L_f)
L_f = 20 * math.log10(d) + 20 * math.log10(f) - 147.56

# Compute Received Power (P_r)
P_r = P_t_dBm + G_t + G_r - L_f

# Calculate Fade Margin
Fade_Margin = P_r - P_min_dBm

# Calculate First Fresnel Zone Radius
lambda_m = c / f
F1 = math.sqrt((lambda_m * d / 2))
Fresnel_Clearance = 0.6 * F1

# Display Results
st.write(f"### 📊 Results:")
st.write(f"**Received Power:** {P_r:.2f} dBm")
st.write(f"**Fade Margin:** {Fade_Margin:.2f} dB")
st.write(f"**Fresnel Zone Radius:** {F1:.2f} m")
st.write(f"**Required Fresnel Clearance:** {Fresnel_Clearance:.2f} m")