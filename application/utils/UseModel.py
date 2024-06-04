import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2

class UseModel:
    """
    Class to use the trained model for prediction.
    """
    def __init__(self, model_path, config) -> None:
        """
        Initialize the class by loading the trained model.
        """
        self.config = config
        self.model_path = model_path
        self.classififer_model = tf.keras.models.load_model(self.model_path)
        
    def load_image(self, image):
        """
        Load the image and resize it to the required dimensions.
        """
        image = cv2.imread(image)
        image_resized = cv2.resize(image, (self.config.img_height, self.config.img_width))
        image = np.expand_dims(image_resized, axis=0)
        return image
    
    def predict(self, image):
        """
        Predict the class of the given image.
        """
        self.pred = self.classififer_model.predict(self.load_image(image))
        return self.config.class_names[np.argmax(self.pred)], np.max(self.pred)