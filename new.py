import streamlit as st
import pywhatkit as kit
from datetime import datetime

# Streamlit page configuration
st.set_page_config(page_title="WhatsApp Messenger", page_icon="🖌", layout="centered")

# Page header
st.title("WhatsApp Message Sender")
st.write("Send personalized WhatsApp messages with ease.")

# Input fields for name and phone number
name = st.text_input("Enter the recipient's name:", placeholder="John Doe")
phone_number = st.text_input("Enter the recipient's phone number:", placeholder="+911234567890")
message_template = (
    "Hello {name}, 👋\n\n"
    "Thank you for visiting Hyderabad Hardware! 🏠\n\n"
    "We are delighted to have had the opportunity to serve you. Your trust and support mean a lot to us. 🙏\n"
    "If you have any questions, need assistance, or have suggestions for us, please do not hesitate to get in touch.\n\n"
    "We look forward to welcoming you back in the future and continuing to provide you with the best products and services.\n\n"
    "Warm regards,\n"
    "Pavan Kumar Kanodia\n"
    "Email: hydexcl@gmail.com\n"
    "Ph. No.: +91 98492 44555\n"
    "Hyderabad Hardware 🏠"
)

# Button to send the message
if st.button("Send Message"):
    if name and phone_number:
        try:
            # Get current time and schedule the message for the next minute
            now = datetime.now()
            send_time_hour = now.hour
            send_time_minute = now.minute + 1

            # Format the message
            personalized_message = message_template.format(name=name)

            # Send the WhatsApp message using pywhatkit
            kit.sendwhatmsg(phone_number, personalized_message, send_time_hour, send_time_minute)

            st.success(f"Message scheduled successfully to {name} at {phone_number}!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both name and phone number.")
