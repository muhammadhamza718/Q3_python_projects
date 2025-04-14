import streamlit as st
import random
import string
import re

# 🔐 Common weak passwords list
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "admin", "letmein", "welcome"}

# 🎯 **Regex-based Strength Scoring**
def check_password_strength(password):
    score = 0
    feedback = []

    st.write(f"🔍 Checking password: `{password}`")

    # 🚨 Blacklist Check
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ This password is too common. Choose a more unique password."]

    # ✅ Length Check (8+ chars)
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # ✅ Upper & Lowercase Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 2
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # ✅ Digit Check
    if re.search(r'\d', password):
        score += 2
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # ✅ Special Character Check
    if re.search(r'[!@#$%^&*]', password):
        score += 2
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # ✅ **Extra Security Boost**
    if len(password) >= 12:
        score += 2  # Bonus for longer passwords
    if re.search(r'\d{3,}', password):  # 3+ digits
        score += 1
    if re.search(r'[!@#$%^&*]{2,}', password):  # 2+ special chars
        score += 1

    # 🔢 **Final Strength Score**
    return score, feedback

# 🎲 Generate a strong password
def generate_strong_password(length=16):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(all_chars, k=length))
    return password

# 🚀 Streamlit App Interface
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # 📊 Strength Output
        if score >= 9:
            st.success("🔥 Ultra Strong Password! Your password is very secure. 🔥")
        elif score >= 7:
            st.success("✅ Strong Password! Your password is secure. 👍")
        elif score >= 5:
            st.warning("⚠️ Almost Strong - Consider a minor improvement.")
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        for msg in feedback:
            st.write(msg)

        if score < 7:
            strong_password = generate_strong_password()
            st.write("🔹 Suggested Strong Password: ", strong_password)
    else:
        st.warning("⚠️ Please enter a password!")
