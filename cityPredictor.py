import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = load_model('my_model.h5')

# Load and preprocess the input image
img_path = 'C:\\Users\\lenovo\\Desktop\\DATA_VIS\\impact\\Cities\\Testing_Data\\Delhi\\Delhi-Test (55).jpg'
img = image.load_img(img_path, target_size=(150, 150))
img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)
img = img / 255.0

# Make predictions on the input image
predictions = model.predict(img)
class_labels = ['Ahmedabad', 'Delhi', 'Kerala', 'Kolkata', 'Mumbai']

# Set the threshold for minimum accuracy
threshold = 0.7

# Get the predicted class label and accuracy
predicted_class_index = np.argmax(predictions)
predicted_class_label = class_labels[predicted_class_index]
accuracy = predictions[0][predicted_class_index]

# Check if accuracy is below the threshold for all classes
if all(accuracy < threshold for accuracy in predictions[0]):
    print("This location is not in our database.")
else:
    print('Predicted class:', predicted_class_label)
    print('Accuracy:', accuracy)
