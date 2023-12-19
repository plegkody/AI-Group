import os
from dotenv import load_dotenv
from datetime import datetime
import json

# Initialize chat history
messages = []

while True:
    # React to user input
    prompt = input("User: ")

    if prompt == "exit":
        break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if prompt:
        messages.append(
            {"role": "user", 
             "content": prompt,
             "timestamp": timestamp}
        )

        response = f"Assistant: {prompt}"
        messages.append(
            {"role": "assistant", 
             "content": response,
             "timestamp": timestamp}
        )
        print(response)

# Save chat history as json to a file
filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".json"
filepath = os.path.join("data", filename)

with open(filepath, "w") as f:
    json.dump(messages, f)