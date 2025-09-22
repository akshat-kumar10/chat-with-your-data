import os
import pandas as pd
import google.generativeai as genai
import gradio as gr
from dotenv import load_dotenv

# Load environment variables from the .env file.
load_dotenv()

# Get the API key from the environment variables.
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    # Use a more user-friendly message for the Gradio interface
    api_key = "placeholder" # Set a placeholder to prevent immediate error on import

# Configure the Gemini API with your key.
genai.configure(api_key=api_key)

def load_csv_data(file_path):
    """
    Loads a CSV file into a pandas DataFrame and returns it as a string.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        str: A string representation of the CSV data, or None if the file is not found.
    """
    if not file_path:
        return None
    try:
        df = pd.read_csv(file_path)
        # Convert the DataFrame to a string for the AI to process.
        return df.to_string(index=False)
    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"An error occurred while loading the CSV: {e}"

def get_ai_response(csv_data, user_question):
    """
    Sends the CSV data and user question to the Gemini API and returns the response.

    Args:
        csv_data (str): The string representation of the CSV file.
        user_question (str): The user's question about the data.

    Returns:
        str: The AI's answer, or an error message if the API call fails.
    """
    if not csv_data:
        return "Please upload a valid CSV file first."
    
    if not user_question:
        return "Please enter a question."
        
    try:
        # Create an instance of the Generative Model.
        model = genai.GenerativeModel('gemini-1.0-pro')

        # Create a detailed prompt to guide the AI.
        prompt = (
            "You are a data analysis assistant. You will be given CSV data and a question about it. "
            "Your task is to provide a concise and accurate answer based *only* on the provided data. "
            "If the answer is not in the data, state that you cannot find it. "
            f"\n\n--- CSV Data ---\n{csv_data}\n\n--- User Question ---\n{user_question}\n\n--- Answer ---"
        )
        
        response = model.generate_content(prompt)
        
        return response.text.strip()

    except Exception as e:
        return f"An error occurred with the Gemini API: {e}"

def chatbot_interface(csv_file_path, user_question):
    """
    Main function for the Gradio interface.
    
    Args:
        csv_file_path (str): The temporary path to the uploaded CSV file.
        user_question (str): The user's question.
    """
    # Check if the API key is valid before proceeding
    if os.getenv("GEMINI_API_KEY") is None:
        return "Error: GEMINI_API_KEY not found in the .env file. Please add your key."
        
    csv_data = load_csv_data(csv_file_path)
    if csv_data and not csv_data.startswith("Error"):
        return get_ai_response(csv_data, user_question)
    else:
        return csv_data

# Gradio interface.
iface = gr.Interface(
    fn=chatbot_interface,
    inputs=[
        gr.File(label="Upload a CSV File"),
        gr.Textbox(label="Enter your question about the CSV data"),
    ],
    outputs="text",
    title="CSV Chatbot with Gemini",
    description="Ask questions about your uploaded CSV file. The bot will answer based on the data you provide.",
    theme=gr.themes.Monochrome(
        font=["Garamond", "serif"],
        font_mono=["Garamond", "serif"]
    )
)

if __name__ == "__main__":

    iface.launch()
