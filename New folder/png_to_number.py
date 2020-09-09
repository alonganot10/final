from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model


def load_image(filename):
    img = load_img(filename, color_mode='grayscale', target_size=(28, 28))
    img = img_to_array(img)
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32')
    img = img / 255.0
    return img


def run_example():
    img = load_image('canvas.png')
    model = load_model('final_model.h5')
    digit = model.predict_classes(img)
    print(digit[0])
    return digit[0]
