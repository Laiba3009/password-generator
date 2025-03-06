import streamlit as st
import re
import random
import string

# Set the page title and icon
st.set_page_config(page_title="Password Strength Meter", page_icon="\U0001F510")

# Function to check the strength of a given password
def check_password_strength(password):
    score = 0  # Initialize the score
    feedback = []  # Store improvement suggestions
    weak_passwords = ["password", "123456", "12345678", "qwerty", "abc123"]  # Common weak passwords
    
    # Check if the password is too common
    if password in weak_passwords:
        return "Weak", "❌ This password is too common! Choose a more secure one."

    # Check length requirement (at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make the password at least 8 characters long.")

    # Check for both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*).")

    # Determine password strength based on score
    if score == 5:
        return "Strong", "✅ Great job! Your password is strong!"
    elif score >= 3:
        return "Moderate", "⚠️ Your password is okay, but could be improved:<br>" + "<br>".join(feedback)
    else:
        return "Weak", "❌ Your password is weak! <br>" + "<br>".join(feedback)

# Function to generate a strong random password
def generate_strong_password():
    length = 12  # Define password length
    characters = string.ascii_letters + string.digits + "!@#$%^&*"  # Include letters, numbers, and special characters
    return "".join(random.choice(characters) for _ in range(length))

# Apply custom CSS for UI styling
st.markdown(
    """
    <style>
    .stApp {
       background: linear-gradient(#e66465, #9198e5);
        color: #002050;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    }
    .password-box {
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
    }
    .weak {
        background-color: #ffcccc;
        color: #d8000c;
    }
    .moderate {
        background-color: #fff4cc;
        color: #9f6000;
    }
    .strong {
        background-color: #d5f5e3;
        color: #006400;
    }
    .stTextInput input {
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .suggestion-box {
        background-color: white;
        color: #002050;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display title
st.markdown("<h1 class='title'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)

# Input field for the user to enter a password
password = st.text_input("Enter your password:", type="password")

# Evaluate the password strength when input is provided
if password:
    strength, message = check_password_strength(password)
    class_name = "weak" if strength == "Weak" else "moderate" if strength == "Moderate" else "strong"
    st.markdown(f"<div class='password-box {class_name}'>{message}</div>", unsafe_allow_html=True)

# Button to generate a strong password suggestion
if st.button("💡 Suggest a Strong Password"):
    st.markdown(f"<div class='suggestion-box'>🔑 Try this strong password: `{generate_strong_password()}`</div>", unsafe_allow_html=True)

# Display feature list
st.markdown("""
### Features:
- ✅ Password strength analysis (Weak, Moderate, Strong)
- ✅ Provides improvement tips for weak passwords
- ✅ Generates strong, secure passwords
- ✅ User-friendly interface with clear feedback
""")
