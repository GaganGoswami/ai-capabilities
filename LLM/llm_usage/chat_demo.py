from utils.prompt_loader import load_json_prompt

def get_chat_response(user_message):
    # Load the reusable prompt template
    prompt_template = load_json_prompt("chat_prompts")
    
    # For example, assume the JSON has a structure like:
    # { "greeting": "Hello, how can I assist you?", "farewell": "Goodbye!" }
    greeting = prompt_template.get("greeting", "Hi")
    
    # Compose the final prompt
    prompt = f"{greeting}\nUser: {user_message}\nAssistant:"
    
    # Process prompt with your LLM (dummy response shown here)
    response = f"Processed response to: {user_message}"
    return response