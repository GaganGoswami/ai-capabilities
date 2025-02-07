import gradio as gr
from utils.prompt_loader import load_json_prompt

def process_prompt(user_input):
    # Load JSON prompts
    chat_prompts = load_json_prompt("chat_prompts") 
     # reads chat_prompts.json
   # greeting = chat_prompts.get(user_input, "I'm ready to help!")
    greeting = chat_prompts.get(user_input)
    #default_response = chat_prompts.get("default", "I'm ready to help!")

    #greeting = chat_prompts.get(user_input)

    if greeting:
        return f"{greeting}\nUser Prompt: {user_input}"
    else:
        default_response = chat_prompts.get("default", "I'm ready to help!")
        return f"{default_response}\nUser Prompt: {user_input}"

with gr.Blocks() as demo:
    # Load JSON prompts to get dropdown options
    chat_prompts = load_json_prompt("chat_prompts")
    dropdown_options = list(chat_prompts.keys())

    input_box = gr.Dropdown(label="Select a prompt", choices=dropdown_options)
    output_box = gr.Textbox(label="Response")
    gr.Button("Submit").click(process_prompt, inputs=input_box, outputs=output_box)

demo.launch()