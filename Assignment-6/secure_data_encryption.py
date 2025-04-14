import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Initialize session state variables if they don't exist
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}  # Will store our encrypted data

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

if 'key' not in st.session_state:
    # Generate a key (in a real app, this should be stored securely)
    st.session_state.key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.key)

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to encrypt data
def encrypt_data(text, passkey):
    # We'll use the passkey as a unique identifier and the cipher for encryption
    encrypted_text = st.session_state.cipher.encrypt(text.encode()).decode()
    return encrypted_text

# Function to decrypt data
def decrypt_data(data_id, passkey):
    hashed_passkey = hash_passkey(passkey)
    
    # Check if the data_id exists and the passkey matches
    if data_id in st.session_state.stored_data:
        if st.session_state.stored_data[data_id]["passkey"] == hashed_passkey:
            encrypted_text = st.session_state.stored_data[data_id]["encrypted_text"]
            decrypted_text = st.session_state.cipher.decrypt(encrypted_text.encode()).decode()
            st.session_state.failed_attempts = 0
            return decrypted_text
    
    # Increment failed attempts if decryption fails
    st.session_state.failed_attempts += 1
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")
    
    # Show number of stored items
    data_count = len(st.session_state.stored_data)
    st.info(f"You currently have {data_count} encrypted data entries stored.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data, passkey)
            
            # Generate a unique ID for this data
            data_id = hashlib.md5(f"{encrypted_text}{hashed_passkey}".encode()).hexdigest()[:10]
            
            # Store the encrypted data with its passkey
            st.session_state.stored_data[data_id] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            
            st.success("✅ Data stored securely!")
            
            # Display the data ID for retrieval
            st.code(data_id, language="text")
            st.info("⚠️ Keep this Data ID safe! You'll need it to retrieve your data.")
            
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    
    # Check if there are too many failed attempts
    if st.session_state.failed_attempts >= 3:
        st.warning("🔒 Too many failed attempts! Please reauthorize.")
        st.experimental_rerun()  # Redirect to the Login page
        
    data_id = st.text_input("Enter Data ID:")
    passkey = st.text_input("Enter Passkey:", type="password")
    
    # Show attempts remaining
    attempts_remaining = 3 - st.session_state.failed_attempts
    st.info(f"Attempts remaining: {attempts_remaining}")

    if st.button("Decrypt"):
        if data_id and passkey:
            decrypted_text = decrypt_data(data_id, passkey)

            if decrypted_text:
                st.success("✅ Data decrypted successfully!")
                st.text_area("Decrypted Data:", value=decrypted_text, height=200)
            else:
                st.error(f"❌ Incorrect passkey or Data ID! Attempts remaining: {3 - st.session_state.failed_attempts}")

                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    # Set the sidebar selection to "Login"
                    st.session_state.failed_attempts = 3  # Ensure it doesn't go over 3
                    st.rerun()
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    st.warning("You have reached the maximum number of failed attempts. Please reauthorize.")
    
    # Display the correct password for demonstration purposes
    st.info("For demonstration purposes, the password is: admin123")
    
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # In a real app, use a more secure authentication method
            st.session_state.failed_attempts = 0
            st.session_state.login_success = True
            st.success("✅ Reauthorized successfully! You can now retrieve data again.")
            
            # Add a button to manually redirect
            if st.button("Continue to Retrieve Data"):
                st.query_params["redirect"] = "retrieve"
                st.rerun()
        else:
            st.error("❌ Incorrect password! Please try again with the correct password.")

# Auto-redirect from Login to Retrieve Data if successful
# Use the recommended query_params instead of experimental_get_query_params
if "redirect" in st.query_params and st.query_params["redirect"] == "retrieve":
    # Clear query params
    st.query_params.clear()
    st.sidebar.selectbox("Navigation", menu, index=menu.index("Retrieve Data"))
    st.rerun()