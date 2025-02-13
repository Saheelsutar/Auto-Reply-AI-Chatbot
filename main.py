import pyautogui
import time
import pyperclip
import requests

def last_message_from_sender(messages, sender_name="Saheel Sutar"):
    msg = messages.strip().split("/2024] ")[-1]
    return sender_name not in msg  # Returns True if the last message is not from Saheel Sutar

# Wait a moment before running to switch windows if needed
time.sleep(3)

# Click on the icon at (1377, 1048)
pyautogui.click(1377, 1048)
time.sleep(2)  # Allow a short delay for processing

while True:
    #click and drag to select text from 
    pyautogui.click(724,210)

    pyautogui.moveTo(724,210, duration=0.5)
    pyautogui.dragTo(1823,932, duration=1.5, button='left')

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Allow time for copying

    # Get text from clipboard using pyperclip
    chat_history = pyperclip.paste()
    print(last_message_from_sender(chat_history))
    
    if last_message_from_sender(chat_history):
        # Set the API endpoint and your API key
        url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyATjzBlxzDeD7d3aMH7giduu6bNMVC8wrQ'
        headers = {
            'Content-Type': 'application/json',
        }
        
        # Define the request data with role information within the user text
        data = {
            "contents": [
                {
                    "role": "model",
                    "parts": [
                        {
                            "text": '''You are Saheel, a coder from India who speaks both Hindi and English. 

                        1. Analyze the chat history and respond as if you are Saheel.
                        2. If the conversation is in English, reply in English.
                        3. If the conversation is in Hindi, reply in Hindi.
                        4. If the conversation mixes Hindi and English, respond using both languages appropriately.
                        5. Do not include the date, time, or sender's name in your message.
                        6. Ensure that any emojis used are relevant to the context of your response.

                        Follow these instructions carefully, and provide your response as if you were Saheel.'''

                        }
                    ]
                },
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": chat_history
                        }
                    ]
                }
            ]
        }

        # Send the POST request
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # Check if 'candidates' key exists in the response
        if 'candidates' in result:
            # Extract the answer, remove newlines, and make sure it's in one line
            answer = " ".join(result['candidates'][0]['content']['parts'][0]['text'].split())
            pyperclip.copy(answer)

            # Step 2: Click at the specified location (849, 954)
            pyautogui.click(849, 954)
            time.sleep(2)  # Small delay to make sure the click registers

            # Step 3: Paste the text from clipboard
            pyautogui.hotkey('ctrl', 'v')  # Simulates pressing Ctrl + V to paste the text

            # Wait a moment for the paste to complete
            time.sleep(2)

            # Step 4: Press Enter
            pyautogui.press('enter')

            # Extract the token count if it's available in the response
            token_count = result.get('usageMetadata', {}).get('totalTokenCount', 'N/A')
            # Optionally print token count for debugging
            print(f"Token Count: {token_count}")
        else:
            print(f"Error: 'candidates' key not found in the response. Full response: {result}")
