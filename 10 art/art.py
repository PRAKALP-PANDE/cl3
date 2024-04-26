import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt

# Function to load an image
def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

# Function to display an image
def show_image(image,title='Image'):
    image = tf.squeeze(image, axis=0)
    plt.imshow(image)
    plt.title(title)
    
# Load content and style images
content_image = load_image(r"C:\Users\Prakalp\Downloads\image1.jpg")
style_image = load_image(r"C:\Users\Prakalp\Downloads\image2.jpg")

# Load the style transfer model
#arbitrary-image-stylization-v1
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Perform style transfer
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]

# Display the images
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
show_image(content_image, 'Content Image')
plt.subplot(1, 3, 2)
show_image(style_image, 'Style Image')
plt.subplot(1, 3, 3)
show_image(stylized_image, 'Stylized Image')
plt.show()