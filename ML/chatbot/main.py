from chat_model import get_chat_response
from prompts.custom_prompt import get_custom_prompt

def main():
    # Get user input
    user_input = input("What's on your mind?\n ")

    # Generate a customized prompt
    prompt = get_custom_prompt(user_input)

    # Get the chat model's response
    response = get_chat_response(prompt)

    # Display the results
    print("Query: ", user_input)
    print("Response: ", response)

if __name__ == "__main__":
    main()
