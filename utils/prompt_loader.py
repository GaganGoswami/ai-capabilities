import os
import json
import yaml

def load_json_prompt(prompt_name, prompts_dir="prompts"):
    """Load a prompt template stored as a JSON file."""
    prompt_path = os.path.join(prompts_dir, f"{prompt_name}.json")
    with open(prompt_path, "r") as f:
        return json.load(f)

def load_text_prompt(prompt_name, prompts_dir="prompts"):
    """Load a prompt template stored as a plain text file."""
    prompt_path = os.path.join(prompts_dir, f"{prompt_name}.txt")
    with open(prompt_path, "r") as f:
        return f.read()

def load_yaml_prompt(prompt_name, prompts_dir="prompts"):
    """Load a prompt template stored as a YAML file."""
    prompt_path = os.path.join(prompts_dir, f"{prompt_name}.yaml")
    with open(prompt_path, "r") as f:
        return yaml.safe_load(f)
    