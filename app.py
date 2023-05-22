import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import random

# Load the trained model
model = load_model('my_model.h5')

# Define class labels
class_labels = ['Ahmedabad', 'Delhi', 'Kerala', 'Kolkata', 'Mumbai']

# Set the threshold for minimum accuracy
threshold = 0.7


# Create a function to process the uploaded image
def process_image(uploaded_image):
    # Load and preprocess the input image
    img = image.load_img(uploaded_image, target_size=(150, 150))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    # Make predictions on the input image
    predictions = model.predict(img)

    # Get the predicted class label and accuracy
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
    accuracy = predictions[0][predicted_class_index]

    # Check if accuracy is below the threshold for all classes
    if all(accuracy < threshold for accuracy in predictions[0]):
        return "This location is not in our database."
    else:
        output = f"<span style='font-size: 24px; color: {random.choice(['#FF9800', '#FF5722', '#673AB7', '#009688'])};'>Predicted class: <strong>{predicted_class_label}</strong></span>"
        acc = f"<span style='font-size: 24px; color: {random.choice(['#FF9800', '#FF5722', '#673AB7', '#009688'])};'>Accuracy: <strong>{accuracy*100:.02f}%</strong></span>"
        return output + "<br>" + acc


# Set Streamlit app title
st.title("Location Classification")

# Add a file uploader to the app
uploaded_image = st.file_uploader("Upload an image (JPG or JPEG format)", type=["jpg", "jpeg"])

# Process the uploaded image and display the result
if uploaded_image is not None:
    st.write("Uploaded image:")
    st.image(uploaded_image, use_column_width=True)

    # Convert the uploaded image to a file path
    image_path = "./uploaded_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_image.getvalue())

    # Process the image and display the result
    result = process_image(image_path)
    st.markdown(result, unsafe_allow_html=True)
