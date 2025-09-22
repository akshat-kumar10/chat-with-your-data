# 📊 CSV Chatbot with Gradio and Gemini

This is a **simple yet powerful chatbot** that allows you to ask questions about your CSV data in natural language. It uses a web-based interface built with **Gradio** and leverages the power of the **Google Gemini API** to analyse the data and provide accurate answers.

---

## ✨ Features

- **📁 CSV Upload:** Easily upload a CSV file directly through the web interface.  
- **💬 Natural Language Queries:** Ask questions about your data as if you were talking to a data analyst.  
- **🤖 Gemini API Integration:** The chatbot uses the `gemini-1.0-pro` model to understand and process your queries.  
- **🖥️ User-Friendly UI:** The Gradio frontend provides a clean and intuitive interface for a seamless user experience.  

---

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.6 or higher 🐍  
- A **Google Gemini API Key** 🔑  

---

## 📦 Installation

1. Clone this repository or download the project files.  
2. Navigate to the project directory in your terminal.  
3. Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## ⚙️ Setup

Create a file named .env in the same directory as chatbot.py.

Add your Gemini API key to this file in the following format:
```bash
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

Replace "YOUR_API_KEY_HERE" with your actual key. 🔑

##🚀 Usage

To start the chatbot, run the Python script from your terminal:
```bash
python chatbot.py
```

This will launch a local web server. Open the URL provided in your terminal (usually http://127.0.0.1:7860) in your web browser to access the chatbot interface. 🌐

On the web page, click the "Upload a CSV File" button to upload your data. 📁
There is already a sample CSV file provided in the repository.

In the text box below, enter your question about the CSV data. 💬

The chatbot will process your request and display the answer. ✅
