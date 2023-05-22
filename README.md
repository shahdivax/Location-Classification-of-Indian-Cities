## Location Classification of Indian Cities

This Streamlit app is designed to detect the location of an Indian city in an uploaded image. It uses a deep learning model trained on 10,500 images classified into 5 classes of cities including Ahmedabad, Delhi, Kerala, Kolkata, and Mumbai. The model was trained in association with Parul University and currently has a test accuracy of 55.6%.

## How to Use the App
1. Clone the GitHub repository:
   ```
   git clone https://github.com/shahdivax/Location-Classification-of-Indian-Cities.git
   ```
2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```
4. Upload an image in JPG or JPEG format.
5. The app will display the uploaded image and predict the location of the city in the image.
6. The predicted location and accuracy percentage will be displayed.

Please note that the app may not work accurately for images that are not clear or do not have a distinct view of the city's landmarks.

## Live Demo
A live demo of the app is available [here](https://shahdivax-location-classification-of-indian-cities-app-dx9t3a.streamlit.app/) hosted with Streamlit.

## Code
The code for this app was written in Python. It uses the following libraries:
* Streamlit: To build the app user interface
* TensorFlow and Keras: To load the pre-trained model and process images
* Numpy and Random: For data processing and random color selection

The application flow follows the steps below:
1. Load the trained deep learning model.
2. Define the class labels for the 5 Indian cities.
3. Set a minimum accuracy threshold for predictions.
4. Create a function to process uploaded images.
5. Create a Streamlit app interface with a file uploader.
6. Process uploaded images and display the predicted location and accuracy.

## Future Work
This app can be improved by increasing the size of the training dataset and fine-tuning the pre-trained model to increase its accuracy. Additionally, the app can be trained to recognize city landmarks to improve its performance.
