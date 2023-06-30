import json
import random

# Get recent messages
def get_recent_message():

    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job as a retail assistant. Ask short question that are relevant to the junior position. Your name is Rachel. The user is called Shaun. Keep you answers to under 30 words.",
    }
