# NutriPinoy: A Computer Vision-Based Classifier for Filipino Food and Nutritional Facts

### Prerequisite
- Python 3.9.18
- Anaconda **(Make sure you are in an environment with the correct python version)**

### Install Dependencies
- Run `conda create -n python=3.9.18 yourenv pip` to create an environment with pip installed.
- Run `conda activate yourenv` to activate your virtual environment.
- (While at the root of the project directory) Run `pip install -r requirements.txt` to install the necessary dependencies.

## Model Training Guide
- In the `model_training` directory, you can find the `image_data` folder. This is where the dataset is stored. You can view it and add your own data. Just make sure to follow the same folder structure.

- You can run the `train_classifier.ipynb` to train your own data. You can also change some parameters, such as the epoch, image dimension, etc., in the Jupyter notebook.

- **Important:** After running the Jupyter notebook, two files will be generated: `resnet_model.h5` and `class_names.json`. If you train your own data, you need to relocate `resnet_model.h5` to the root of the `application` folder and transfer `class_names.json` to `/applications/configurations`



## Running the application
**Reminders:** Before running the application, ensure that you have the generated `resnet_model.h5` from the model training on the root directory of the application folder. Moreover, make sure that `class_names.json` is available in the configurations folder.

**Activate your anaconda environment first by inputting the following command into the terminal:** 
```
conda activate yourenv
```

**Go to the `application` directory in the terminal through (assuming your terminal working directory is the root directory of the project folder):**
```
cd application
```

**To run the application, input the following command in the terminal:**

```
python main.py
```

## Useful Information

### File Structure
- `application`: Contains the files for running the application
- `model_training`: Contains the files for training the ResNet50 image classification model.

### Application Directories
- The `utils` directory contains the helper classes.
- The `configurations` folder contains the class which for the application configurations which you can modify.

### Application Classes
- **UseApi:** Class for calling the API Ninjas which is used to obtain data about nutritional facts
- **UseModel:** Class to load the image and make predictions using the trained model.
- **ModelConfig:** Class for modifying applications configurations, such as the dimensions of the image.

