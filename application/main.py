"""
Project description:
    This file contains the main application code for the Filipino Food Classification and Nutrition Facts application.
    It uses PyQt5 to create the GUI and integrates the UseModel and NutritionApi classes to classify Filipino food images
    and retrieve nutrition facts using an external API.

    The application allows users to open an image file or capture an image using the camera. The image is then processed
    using a pre-trained model to classify the food in the image. The application displays the detected food, confidence level,
    and nutrition facts for the detected food.

Programmed by: Anakin Skywalker Pactores | 3-BSCS Student
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import numpy as np
import os

from utils.UseApi import NutritionApi
from utils.UseModel import *
from configurations.ModelConfig import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress most TensorFlow messages.

# Enable HighDPI display with PyQt5
QtWidgets.QApplication.setAttribute(
    QtCore.Qt.AA_EnableHighDpiScaling, True
)
QtWidgets.QApplication.setAttribute(
    QtCore.Qt.AA_UseHighDpiPixmaps, True
) 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Sets up the GUI components and connects signals to slots.
        Automatically generated by PyQt5 Designer.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        MainWindow.setStyleSheet("background-color: rgb(42, 49, 51);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.FilipinoFoodClassification = QtWidgets.QGroupBox(self.frame)
        self.FilipinoFoodClassification.setMinimumSize(QtCore.QSize(0, 100))
        self.FilipinoFoodClassification.setMaximumSize(QtCore.QSize(350, 400))
        self.FilipinoFoodClassification.setStyleSheet("color: rgb(255, 255, 255);")
        self.FilipinoFoodClassification.setObjectName("FilipinoFoodClassification")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.FilipinoFoodClassification)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.DetectedFood = QtWidgets.QFrame(self.FilipinoFoodClassification)
        self.DetectedFood.setStyleSheet("")
        self.DetectedFood.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DetectedFood.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DetectedFood.setObjectName("DetectedFood")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DetectedFood)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.DetectedFood)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.DetectedFoodOutput = QtWidgets.QLabel(self.DetectedFood)
        self.DetectedFoodOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.DetectedFoodOutput.setObjectName("DetectedFoodOutput")
        self.verticalLayout.addWidget(self.DetectedFoodOutput)
        self.verticalLayout_6.addWidget(self.DetectedFood)
        self.Confidence_Level = QtWidgets.QFrame(self.FilipinoFoodClassification)
        self.Confidence_Level.setStyleSheet("")
        self.Confidence_Level.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Confidence_Level.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Confidence_Level.setObjectName("Confidence_Level")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Confidence_Level)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.Confidence_Level)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ConfidenceOutput = QtWidgets.QLabel(self.Confidence_Level)
        self.ConfidenceOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.ConfidenceOutput.setObjectName("ConfidenceOutput")
        self.verticalLayout_2.addWidget(self.ConfidenceOutput)
        self.verticalLayout_6.addWidget(self.Confidence_Level)
        self.verticalLayout_7.addWidget(self.FilipinoFoodClassification)
        self.NutritionFacts = QtWidgets.QGroupBox(self.frame)
        self.NutritionFacts.setStyleSheet("color: rgb(255, 255, 255);")
        self.NutritionFacts.setObjectName("NutritionFacts")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.NutritionFacts)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.NutritionFacts)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.CaloriesOutput = QtWidgets.QLabel(self.frame_4)
        self.CaloriesOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.CaloriesOutput.setObjectName("CaloriesOutput")
        self.verticalLayout_4.addWidget(self.CaloriesOutput)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.NutritionFacts)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.CholesterolOutput = QtWidgets.QLabel(self.frame_5)
        self.CholesterolOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.CholesterolOutput.setObjectName("CholesterolOutput")
        self.verticalLayout_5.addWidget(self.CholesterolOutput)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.NutritionFacts)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.TotalFatsOutput = QtWidgets.QLabel(self.frame_6)
        self.TotalFatsOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalFatsOutput.setObjectName("TotalFatsOutput")
        self.verticalLayout_9.addWidget(self.TotalFatsOutput)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_7.addWidget(self.NutritionFacts)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.openFileButton = QtWidgets.QPushButton(self.frame_3)
        self.openFileButton.setStyleSheet("background-color: rgb(68, 80, 83);\n"
            "color: rgb(255, 255, 255);")
        self.openFileButton.setObjectName("openFileButton")
        self.verticalLayout_8.addWidget(self.openFileButton)
        self.openCameraButton = QtWidgets.QPushButton(self.frame_3)
        self.openCameraButton.setStyleSheet("background-color: rgb(68, 80, 83);\n"
            "color: rgb(255, 255, 255);")
        self.openCameraButton.setObjectName("openCameraButton")
        self.verticalLayout_8.addWidget(self.openCameraButton)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.frame_2.setStyleSheet("border-color: rgb(88, 88, 88);\n"
            "background-color: rgb(68, 80, 83);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.imageInput = QtWidgets.QLabel(self.frame_2)
        self.imageInput.setText("")
        self.imageInput.setObjectName("imageInput")
        self.gridLayout.addWidget(self.imageInput, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Lab Exercise 8/Final/icons/save-3-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Lab Exercise 8/Final/icons/file-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Image.setIcon(icon1)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionOpenImage = QtWidgets.QAction(MainWindow)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionSaveEdit = QtWidgets.QAction(MainWindow)
        self.actionSaveEdit.setObjectName("actionSaveEdit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # The following code is added manually to connect signals to slots and set up some UI components.

        # Button to capture the image
        self.captureButton = QtWidgets.QPushButton("Capture", self.frame_3) 
        self.captureButton.setStyleSheet("background-color: rgb(68, 80, 83);\n" "color: rgb(255, 255, 255);")
        self.captureButton.hide()  # Initially hide the capture button
        
        # Connected the buttons to their respective functions
        self.openFileButton.clicked.connect(self.openFile)
        self.openCameraButton.clicked.connect(self.openCamera)
        self.verticalLayout_8.addWidget(self.captureButton)
        self.captureButton.clicked.connect(self.captureImage)

    def retranslateUi(self, MainWindow):
        """
        Automatically generated by PyQt5 Designer to set the text and titles of the GUI components.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FilipinoFoodClassification.setTitle(_translate("MainWindow", "Filipino Food Classification"))
        self.label.setText(_translate("MainWindow", "Detected Food:"))
        self.DetectedFoodOutput.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "Confidence:"))
        self.ConfidenceOutput.setText(_translate("MainWindow", "-"))
        self.NutritionFacts.setTitle(_translate("MainWindow", "Nutrition Facts"))
        self.label_3.setText(_translate("MainWindow", "Calories:"))
        self.CaloriesOutput.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "Cholesterol (Mg):"))
        self.CholesterolOutput.setText(_translate("MainWindow", "-"))
        self.label_9.setText(_translate("MainWindow", "Total Fats:"))
        self.TotalFatsOutput.setText(_translate("MainWindow", "-"))
        self.openFileButton.setText(_translate("MainWindow", "Open File"))
        self.openCameraButton.setText(_translate("MainWindow", "Open Camera"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save Photo"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
        self.actionOpen_Image.setToolTip(_translate("MainWindow", "Open Image"))
        self.actionOpenImage.setText(_translate("MainWindow", "Open Image"))
        self.actionSaveEdit.setText(_translate("MainWindow", "Save Edit"))

    def openCamera(self):
        """
        Method to open the camera and start capturing frames.
        """
        self.movie = QtGui.QMovie('static/loading.gif')         # Load a loading animation
        
        self.imageInput.clear()                                 # Clear the current image display, if any
        self.imageInput.setScaledContents(False)                # Remove scaled contents if any
        
        self.movie.setScaledSize(QtCore.QSize(50, 50))          # Set the size of the loading animation
        self.imageInput.setAlignment(QtCore.Qt.AlignCenter)     # Center the movie in QLabel
        self.imageInput.setMovie(self.movie)                    # Set the movie to the QLabel
        self.movie.start()                                      # Start the loading animation   
        
        self.camera_thread = CameraThread()                     # Create a camera thread to capture frames in a separate thread
        self.camera_thread.update_frame.connect(self.updateFrame)
        self.camera_thread.start()                              # Start the camera thread
        self.openCameraButton.hide()                            # Hide the open camera button
        self.captureButton.show()                               # Show the capture button

    def updateFrame(self, image):
        """
        Method to update the image display with the latest frame from the camera.
        """
        if image is None:
            self.movie.stop()
            self.imageInput.clear()
            self.imageInput.setText("Camera disconnected or failed to start.")
        else:
            self.imageInput.setPixmap(QtGui.QPixmap.fromImage(image))

    def captureImage(self):
        """
        Method to capture the current frame from the camera and process it.
        """
        
        # Stop the camera thread and update the UI
        if self.camera_thread.isRunning():
            self.camera_thread.stop()                           # Stop the camera thread
            self.captureButton.hide()
            self.openCameraButton.show()
            self.movie.stop()                                   # Stop any loading animation if necessary
            self.imageInput.clear()
            self.imageInput.setText("Camera stopped.")          # Update the UI to reflect that the camera has stopped

            # Continue with processing the captured image if it exists
            if hasattr(self.camera_thread, 'last_frame') and self.camera_thread.last_frame is not None:
                frame = self.camera_thread.last_frame
                cv_image_path = "captured_image.jpg"
                cv2.imwrite(cv_image_path, frame)
                self.processImage(cv_image_path)                # Process the captured image
            else:
                print("No valid frame captured.")

    def processImage(self, image_path):
        """
        Method to process the captured image using the trained model.
        """
        self.image_location = image_path
        
        # Clear the current image display and show a loading animation or text
        self.imageInput.clear()
        self.imageInput.setScaledContents(False)                # Remove scaled contents if any

        self.movie = QtGui.QMovie('static/loading.gif')         # Load a loading animation
        self.movie.setScaledSize(QtCore.QSize(50, 50))
        self.imageInput.setAlignment(QtCore.Qt.AlignCenter)     # Center the movie in QLabel
        self.imageInput.setMovie(self.movie)
        self.movie.start()                                      # Start the loading animation
        
        # Create and start a worker thread to process the image in the background to avoid freezing the UI
        self.worker_thread = WorkerThread(self.image_location)
        self.worker_thread.start()
        self.worker_thread.prediction_completed.connect(self.updateGUI)

    def openFile(self):
        """
        Method to open a file dialog and select an image file for processing.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Images (*.png *.jpg *.jpeg)", options=options)
        if fileName:
            self.image_location = fileName
            
            # Reset the QLabel before starting new processing
            self.imageInput.clear()
            self.imageInput.setScaledContents(False)            # Remove scaled contents if any
            
            # Create a worker thread for processing the image in the background to avoid freezing the UI
            self.worker_thread = WorkerThread(self.image_location)
            self.worker_thread.start()
            
            self.movie = QtGui.QMovie('static/loading.gif')     # Load a loading animation
            self.movie.setScaledSize(QtCore.QSize(50, 50))
            self.imageInput.setAlignment(QtCore.Qt.AlignCenter) # Center the movie in QLabel
            self.imageInput.setMovie(self.movie)
            self.movie.start()                                  # Start the loading animation
            
            # Connect signals from the worker thread to update GUI
            self.worker_thread.prediction_completed.connect(self.updateGUI)

    def displayNutrition(self, food):
        """
        Method to display the nutrition facts of the detected food.
        """
        
        # Retrieve nutrition facts using the NutritionApi class
        nutrition = NutritionApi()
        nutrition_info = nutrition.get_nutrition(food)
        
        # Check if nutrition info is available. If not, display N/A.
        if not nutrition_info or len(nutrition_info) == 0:
            self.CaloriesOutput.setText('N/A')
            self.CholesterolOutput.setText('N/A')
            self.TotalFatsOutput.setText('N/A')
            return
        
        # Update GUI with nutrition info
        self.CaloriesOutput.setText(f"{nutrition_info[0]['calories']} kcal")
        self.CholesterolOutput.setText(f"{nutrition_info[0]['cholesterol_mg']} mg")
        self.TotalFatsOutput.setText(f"{nutrition_info[0]['fat_total_g']} g")
        

    def updateGUI(self, classification, confidence):
        """
        Method to update the GUI with the detected food classification and confidence level.
        """
        self.movie.stop()

        # Update GUI with prediction results
        food_classification = ' '.join(word.capitalize() for word in classification.split('_'))
        self.displayNutrition(food_classification)
        self.DetectedFoodOutput.setText(food_classification)
        self.ConfidenceOutput.setText(f"{confidence * 100:.2f}%")
        self.imageInput.setPixmap(QtGui.QPixmap(self.image_location))
        self.imageInput.setScaledContents(True)

class WorkerThread(QtCore.QThread):
    """
    Class to create a worker thread for processing the image using the trained model.
    """
    prediction_completed = QtCore.pyqtSignal(str, float)

    # Initialize the worker thread with the image location
    def __init__(self, image_location):
        super(WorkerThread, self).__init__()
        self.image_location = image_location

    # Load the model and predict the image
    def run(self):
        model = UseModel(os.path.join(os.path.dirname(__file__), 'resnet_model.h5'), ModelConfig())
        classification, confidence = model.predict(self.image_location)
        self.prediction_completed.emit(classification, confidence)

class CameraThread(QtCore.QThread):
    """
    Class to create a camera thread for capturing frames from the camera.
    """
    update_frame = QtCore.pyqtSignal(QImage)
    
    # Initialize the last_frame attribute
    last_frame = None   

    # Initialize the camera thread
    def __init__(self):
        super(CameraThread, self).__init__()
        self.capture = None
        self.running = False

    # Start the camera and capture frames
    def run(self):
        self.running = True
        self.capture = cv2.VideoCapture(0)              # Start the camera on a separate thread
        while self.running:
            ret, frame = self.capture.read()
            if ret:
                self.last_frame = frame.copy()          # Update last_frame with the latest captured frame
                image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
                self.update_frame.emit(image)

    # Stop the camera thread
    def stop(self):
        self.running = False
        if self.capture is not None:
            self.capture.release()                      # Release the camera resource
        self.quit()

# Main method to run the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
