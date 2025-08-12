from dotenv import load_dotenv
import os

# Try to load the .env file from the current directory
is_loaded = load_dotenv()

print("--- Environment Check ---")
print(f"Was a .env file found and loaded? -> {is_loaded}\n")

# Check for the specific keys
openai_key = os.getenv("OPENAI_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")

print(f"Found OPENAI_API_KEY: {openai_key}")
print(f"Found GOOGLE_API_KEY: {google_key}")
print("-------------------------")

if not openai_key or not google_key:
    print("\nError: One or both API keys were NOT found.")
    print("Please check your .env file's name, location, and content carefully.")
else:
    print("\nSuccess! Both API keys were found successfully.")