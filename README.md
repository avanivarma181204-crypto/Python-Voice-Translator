# 🎙️ Python Voice Translator

A Python-based voice translation application that captures speech from the user's microphone, converts it into text, translates the text into a selected language, and converts the translated text into speech.

## 📌 Overview

The Python Voice Translator combines speech recognition, language translation, and text-to-speech technologies into a single application.

The application follows this workflow:

**Voice Input → Speech-to-Text → Translation → Text-to-Speech → Voice Output**

It is designed as a simple project for exploring practical applications of Python and language-processing libraries.

## ✨ Features

* 🎤 Captures speech through a microphone
* 📝 Converts speech into text
* 🌐 Translates text into another language
* 🔊 Converts translated text into speech
* 🗣️ Supports voice-based interaction
* ⚠️ Handles basic recognition errors
* 🐍 Built using Python libraries

## 🛠️ Technologies Used

* **Python**
* **SpeechRecognition**
* **gTTS (Google Text-to-Speech)**
* **deep-translator**
* **OS module**

## 📂 Project Structure

```text
Python-Voice-Translator/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    └── screenshot.png
```

> Adjust the filenames above to match the actual files in your project.

## 🔄 How It Works

```text
        🎤 User Speech
              ↓
      Speech Recognition
              ↓
        Text Conversion
              ↓
       Language Translation
              ↓
       Translated Text
              ↓
        Text-to-Speech
              ↓
        🔊 Voice Output
```

### Step 1 — Voice Input

The application listens to the user's speech through the microphone.

### Step 2 — Speech Recognition

The captured speech is processed and converted into text using the SpeechRecognition library.

### Step 3 — Translation

The recognized text is passed to the translation component and translated into the selected target language.

### Step 4 — Text-to-Speech

The translated text is converted into spoken audio using gTTS.

### Step 5 — Voice Output

The generated audio is played back to the user.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/avanivarma181204-crypto/Python-Voice-Translator.git
```

### 2. Open the project folder

```bash
cd Python-Voice-Translator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Run:

```bash
python main.py
```

Allow microphone access when requested and follow the instructions provided by the application.

## 📦 Requirements

Create a `requirements.txt` file containing the packages actually used by your project.

For example:

```text
SpeechRecognition
gTTS
deep-translator
PyAudio
```

> If your project uses a different microphone/audio package, replace `PyAudio` with the package you actually use.

## 🖥️ Example

Example workflow:

```text
User speaks:
"Hello, how are you?"

        ↓

Speech converted to text

        ↓

Text translated to selected language

        ↓

Translated text converted to speech

        ↓

User hears translated output
```

## 🎯 Learning Outcomes

Through this project, I practiced:

* Python programming
* Working with external libraries
* Speech recognition
* Text-to-speech conversion
* Language translation
* Exception handling
* Integrating multiple Python modules
* Building a practical Python application

## 🔮 Future Improvements

Possible future improvements include:

* Add a graphical user interface
* Add more language-selection options
* Improve error handling
* Add automatic language detection
* Add text-based translation mode
* Add translation history
* Improve audio controls
* Deploy the application as a web application

## 👩‍💻 Author

**Avani Varma**

B.Tech – Electronics & Communication Engineering

GitHub: https://github.com/avanivarma181204-crypto

LinkedIn: Add your LinkedIn profile here

## 📄 License

This project is created for educational and portfolio purposes.
