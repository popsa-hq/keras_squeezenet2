# keras-squeezenet [![Build Status](https://travis-ci.org/rcmalli/keras-squeezenet.svg?branch=master)](https://travis-ci.org/rcmalli/keras-squeezenet)

# Keras-squeezenet2

SqueezeNet v1.1 Implementation using tf.Keras for tensorflow version 2 

This is a rework of the original work by [Refik Can MALLI](https://github.com/rcmalli/keras-squeezenet)



~~~bash
# Most Recent One
pip install git+https://github.com/rcmalli/keras-squeezenet.git

~~~

### News

- Project is now up-to-date with the new Keras version (2.0).

- Old Implementation is still available at 'keras1' branch but not updated.

### Library Versions

- Tensorflow v2.rc1

### Example Usage

~~~python
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.preprocessing import image

model = SqueezeNet()

img = image.load_img('../images/cat.jpeg', target_size=(227, 227))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
print('Predicted:', decode_predictions(preds))

~~~


### References

1) [Keras Framework](www.keras.io)

2) [SqueezeNet Official Github Repo](https://github.com/DeepScale/SqueezeNet)

3) [SqueezeNet Paper](http://arxiv.org/abs/1602.07360)


### Licence 

MIT License 

Note: If you find this project useful, please include reference link in your work.
