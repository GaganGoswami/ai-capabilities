import unittest
from unittest.mock import patch, MagicMock
import gradio as gr
from gradio.components import Dropdown, Textbox
from gradio.components import Button
from gradio.blocks import Blocks
from UI.gradio_multi_demo import process_prompt, demo

class TestGradioMultiDemo(unittest.TestCase):

    @patch('utils.prompt_loader.load_json_prompt')
    def test_process_prompt_with_valid_input(self, mock_load_json_prompt):
        mock_load_json_prompt.return_value = {
            "hello": "Hi there!",
            "default": "I'm ready to help!"
        }
        user_input = "hello"
        expected_output = "Hi there!\nUser Prompt: hello"
        self.assertEqual(process_prompt(user_input), expected_output)

    @patch('utils.prompt_loader.load_json_prompt')
    def test_process_prompt_with_invalid_input(self, mock_load_json_prompt):
        mock_load_json_prompt.return_value = {
            "hello": "Hi there!",
            "default": "I'm ready to help!"
        }
        user_input = "unknown"
        expected_output = "I'm ready to help!\nUser Prompt: unknown"
        self.assertEqual(process_prompt(user_input), expected_output)

    @patch('utils.prompt_loader.load_json_prompt')
    def test_demo_interface(self, mock_load_json_prompt):
        mock_load_json_prompt.return_value = {
            "hello": "Hi there!",
            "default": "I'm ready to help!"
        }
        with demo:
            self.assertIsInstance(demo, Blocks)
            self.assertIsInstance(demo.children[0], Dropdown)
            self.assertIsInstance(demo.children[1], Textbox)
            self.assertIsInstance(demo.children[2], Button)



if __name__ == '__main__':
    unittest.main()