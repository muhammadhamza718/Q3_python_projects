import streamlit as st

# Custom Styling
st.markdown(
    """
    <style>
    body {
        background-color: #0f0f1a;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55);
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    h1 {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #f8f8f8;
        text-shadow: 2px 2px 10px rgba(0, 255, 255, 0.7);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white;
        font-size: 18px;
        padding: 14px 22px;
        border-radius: 12px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 5px 15px rgba(255, 69, 0, 0.5);
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: scale(1.07);
        background: linear-gradient(45deg, #12c2e9, #c471ed);
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
    }
    .result-box {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 12px;
        margin-top: 25px;
        box-shadow: 0 5px 20px rgba(0, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #ffffff;
        opacity: 0.7;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #0d1b2a, #1b263b); /* Dark blue theme */
        color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    }

    [data-testid="stSidebar"] h2 {
        color: #f8f8f8;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0, 255, 255, 0.5);
    }

    [data-testid="stSidebar"] .stSelectbox, 
    [data-testid="stSidebar"] .stNumberInput {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(8px);
    }

    [data-testid="stSidebar"] .stSelectbox:hover, 
    [data-testid="stSidebar"] .stNumberInput:hover {
        border: 1px solid rgba(0, 255, 255, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown("<h1>⚡ Unit Convertor - Streamlit</h1>", unsafe_allow_html=True)

st.write("🔹 Convert units of Length, Weight, and Temperature easily with an interactive UI.")

# Sidebar Selection
conversion_type = st.sidebar.selectbox("📌 Choose Conversion Type", [
                                       "Length", "Weight", "Temperature"])
value = st.number_input("📝 Enter the value:", value=0.0,
                        min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("🔄 From", [
                                 "Meters", "Kilometers", "Centimeters", "Millimeters", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("➡️ To", [
                               "Meters", "Kilometers", "Centimeters", "Millimeters", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox(
            "🔄 From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox(
            "➡️ To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("🔄 From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("➡️ To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions


def length_convertor(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Yards": 1.09361, "Inches": 39.37, "Feet": 3.28084
    }
    return (value / length_units[from_unit]) * length_units[to_unit]


def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]


def temp_convertor(value, from_unit, to_unit):
    temp_conversions = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
    }
    return temp_conversions.get((from_unit, to_unit), lambda x: x)(value)


# Convert Button
if st.button("🚀 Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_convertor(value, from_unit, to_unit)

    st.markdown(
        f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>⚡ Developed by Muhammad Hamza</div>",
            unsafe_allow_html=True)
