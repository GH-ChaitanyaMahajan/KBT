import google.generativeai as genai

genai.configure(api_key = "AIzaSyDn5awyp03f343tFSJQHs_accstYayzQh8")

for m in genai.list_models():
    print(m.name)


