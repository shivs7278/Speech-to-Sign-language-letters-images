import streamlit as st
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image
import string

# List of predefined words that have associated sign language GIFs
isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 
           'are you sick', 'be careful', 'can we meet tomorrow', 'did you book tickets',
           'good morning', 'good night', 'hello what is your name', 'i am fine',
           'i am sorry', 'i am thinking', 'i am tired', 'nice to meet you', 'sign language interpreter']

alphabet = list(string.ascii_lowercase)

st.title("SIGN LANGUAGE ASSISTANT")
st.write("Convert spoken words into sign language letters.")

def recognize_speech():
    """Captures and processes speech input."""
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        st.info("Start Speaking !!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)  # Using Google Speech Recognition
            text = text.lower().strip()
            st.success(f"Your words: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand. Try again.")
        except sr.RequestError:
            st.error("Could not request results. Check your internet connection.")
    return None

def display_gif(word):
    """Displays a sign language GIF if available."""
    gif_path = f'ISL_images/{word}.gif'
    if os.path.exists(gif_path):
        st.image(gif_path, caption=f"Sign Language for '{word}'", use_column_width=True)
    else:
        st.warning("No GIF found for this word.")

def display_letters(word):
    """Displays sign language images for individual letters."""
    st.write("Displaying sign images for letters:")
    cols = st.columns(len(word))  # Create a dynamic grid

    for i, letter in enumerate(word):
        if letter in alphabet:
            img_path = f'images_of_letters/{letter}.jpg'
            if os.path.exists(img_path):
                with cols[i]:  # Display images in a row
                    st.image(img_path, caption=letter, width=70)
            else:
                st.warning(f"No image for '{letter}'")

# Button to start voice recognition
if st.button("Start Speaking..."):
    result = recognize_speech()
    
    if result:
        if result in isl_gif:
            display_gif(result)
        else:
            display_letters(result)

st.write("Try saying common phrases like 'hello what is your name' or 'i am fine' to see sign language letter images.")
    
    