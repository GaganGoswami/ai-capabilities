import gradio as gr
from utils.prompt_loader import load_text_prompt

# import sys
# import os

# # Add the parent directory to the sys.path to resolve the utils module
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def process_prompt(user_input):
    # Load a text prompt template and replace a placeholder with the user input
    template = load_text_prompt("qa_prompts")  # e.g., "Question: {question}\nAnswer:"
    prompt = template.format(question=user_input)
    # Dummy answer generation
    return f"Simulated answer for prompt:\n{prompt}"

with gr.Blocks() as demo:
    input_box = gr.Textbox(label="Ask your question")
    output_box = gr.Textbox(label="Answer")
    gr.Button("Submit").click(process_prompt, inputs=input_box, outputs=output_box)

demo.launch()