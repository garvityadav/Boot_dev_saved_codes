import os
import sys

from google import genai
from google.genai import types

# loads the env variables
from dotenv import load_dotenv
load_dotenv()
#----------------------------------

# declaring the api key

api_key = os.environ.get("GEMINI_API_KEY")
#-----------------------------------

# declaring the client instance
client = genai.Client(api_key=api_key)
#-----------------------------------



def main():
    args = sys.argv[1:]
    
    if not args:
        sys.exit(1) 

    userInput = args[0] 
    messages = [types.Content(role="user",parts=[types.Part(text=userInput)]),] 

    def generateContent(client,messages):
    
        response = client.models.generate_content(model='gemini-2.0-flash-001' , contents=messages)
        metadata = response.usage_metadata
        
        print("Response:")
        print(response.text)
        if len( args) >1 and args[1] == "--verbose":
            print(f"User prompt: {userInput}")
            print(f"Prompt tokens: {metadata.prompt_token_count}")
            print(f"Response tokens: {metadata.candidates_token_count}")


    generateContent(client,messages)
if __name__ == "__main__":

    main()
    
