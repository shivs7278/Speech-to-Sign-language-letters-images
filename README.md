# Speech-to-Sign-language-letters-images

# 🧏‍♂️ Speech-to-Sign Language Converter

## 📌 Overview
This application converts spoken words into sign language gestures, helping bridge communication gaps for individuals with hearing impairments. The app listens to speech, recognizes the words, and displays corresponding sign language images or GIFs.

## 🚀 Features
- 🎤 **Speech Recognition**: Converts live voice input into text using `speech_recognition`.
- 🖼 **Sign Language Display**: Maps recognized words to corresponding sign language GIFs.
- 🔠 **Letter-by-Letter Representation**: If a word is not found, the app spells it out using individual sign images.
- 🖥 **Streamlit Integration**: Provides an easy-to-use web interface.

## 🛠 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/speech-to-sign.git
cd speech-to-sign
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

## 📦 Dependencies
- `speech_recognition`
- `numpy`
- `matplotlib`
- `opencv-python`
- `easygui`
- `pillow`
- `tkinter`
- `streamlit`

Install missing packages using:
```bash
pip install package-name
```

## 🖼 Usage
1. Start the app and click **Live Voice**.
2. Speak into the microphone.
3. If the spoken phrase is recognized, a corresponding sign language GIF is displayed.
4. If the phrase is not found, the app spells it out using letter images.
5. Click **All Done!** to exit the app.

## 🔥 Contributing
Feel free to fork the repository and submit pull requests! 🚀

 
 Developed with ♥  by Shivs

 

