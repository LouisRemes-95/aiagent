import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    parser = argparse.ArgumentParser(description="Process a prompt with gemini.")
    parser.add_argument("prompt", nargs="?", help="The prompt/question to process.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()

    if not args.prompt:
        print("Error: No prompt provided")
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = sys.argv[1]
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    response = client.models.generate_content(model = 'gemini-2.0-flash-001', contents = messages)

    if args.verbose: print(f"User prompt: {user_prompt}")
    print("Response:")
    print(response.text)
    if args.verbose: print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    if args.verbose: print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()