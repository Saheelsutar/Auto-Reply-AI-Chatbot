import requests

# Set the API endpoint and your API key
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyATjzBlxzDeD7d3aMH7giduu6bNMVC8wrQ'
headers = {
    'Content-Type': 'application/json',
}
command='''[9:32 pm, 29/9/2024] Saheel Sutar: You will be printing tomorrow any stuff?
[9:32 pm, 29/9/2024] Satvik: No
[9:32 pm, 29/9/2024] Saheel Sutar: Ok
[9:34 pm, 29/9/2024] Satvik: Might need to go during the 15 min break, not sure'''
# Define the request data with role information within the user text
data = {
  "contents": [
    {
      "role": "model",
      "parts": [
        {
              "text": "You are a person named saheel who speaks hindi as well as english and you are from india and you are a coder. You analyse chat history and respond like saheel. give it reply as from saheel. Reply in english if the conversation is in english, else if reply in hindi if the conversation is in hindi, else reply in hindi and english mix in between if the conversation is hindi and english mix. Don't include date,time and name in the message. Analyse chat_history properly and then reply.If you are including emojis then make sure that those emojis perfectly matches the reply.Please remember instructions. Output should be the next response as Saheel"
        }
      ]
    },
    {
      "role": "user",
      "parts": [
        {
          "text": command
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
    
    # Extract the token count if it's available in the response
    token_count = result.get('usageMetadata', {}).get('totalTokenCount', 'N/A')
    
    # Print the filtered output
    print(f"Answer: {answer}")
    print(f"Token Count: {token_count}")
else:
    print(f"Error: 'candidates' key not found in the response. Full response: {result}")
