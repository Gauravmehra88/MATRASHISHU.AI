import google.generativeai as genai

genai.configure(api_key="your_actual_api_key_here")

# Use a valid model name
model = genai.GenerativeModel("gemini-1.5-pro-latest")

response = model.generate_content("Hello, how can I help you?")
print(response.text)

