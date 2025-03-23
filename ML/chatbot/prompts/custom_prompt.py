
def get_custom_prompt(user_input):
    """
    Generates a customized prompt based on user input.
    """
    return f"""
    You are a helpful AI assistant. The user has asked the following question:

    "{user_input}"

    Please provide a detailed and friendly response.
    """
