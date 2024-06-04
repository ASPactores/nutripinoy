from dotenv import load_dotenv
import os
import requests

class NutritionApi:
    """
    Class to interact with the Nutrition API. The API key is stored in the .env file.
    Note: The API used for this project is the API Ninjas Nutrition API.
    """
    def __init__(self):
        """
        Initialize the class by loading the API key from the .env file.
        """
        load_dotenv()
        self.api_key = os.getenv('API_NINJA_KEY')
    
    def get_nutrition(self, food):
        """
        Get the nutrition information for the given food.
        """
        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={food}'
        response = requests.get(api_url, headers={'X-Api-Key': self.api_key})
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return None
