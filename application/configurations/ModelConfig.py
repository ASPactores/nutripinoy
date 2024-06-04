# import tensorflow as tf
import json
import os

class ModelConfig:
    """
    Class to hold the configuration of the model. Any changes to the model should be done here.
    """
    def __init__(self, class_names_file='class_names.json') -> None:
        """
        Initialize the configuration of the model (image width, image height, class names)
        """
        self.img_width = 215
        self.img_height = 215
        self.class_names = self.load_class_names(class_names_file)
    
    def load_class_names(self, class_names_file):
        """
        Load the class names from the class_names.json file.
        Note: The class_names.json file should be in the same directory as this script.
        """
        
        # Get the directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the class_names.json file
        file_path = os.path.join(base_dir, class_names_file)

        # Load the class names from the class_names.json file
        with open(file_path, 'r') as f:
            class_names = json.load(f)
        return class_names



