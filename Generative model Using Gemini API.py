import google.generativeai as genai
API_KEY="AIzaSyCzKPYIPgksFCUVKxpN3zyDWt7-ru9l6vg"
#instantiate the model
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')


while True:
    query = input("What do you want to know today?\nYour Response: ")
    if query=="exit":
        print("Gemini: Bye bye!!")
        break
    response = model.generate_content(query)
    print("Gemini: ", response.text)