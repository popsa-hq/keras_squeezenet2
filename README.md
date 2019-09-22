# Keras-squeezenet2 

[![CircleCI](https://circleci.com/gh/daviddexter/keras_squeezenet2.svg?style=svg)](https://circleci.com/gh/daviddexter/keras_squeezenet2)



SqueezeNet v1.1 Implementation using tf.Keras for tensorflow version 2 

This is a rework of the original work by [Refik Can MALLI](https://github.com/rcmalli/keras-squeezenet)



~~~bash
git clone https://github.com/daviddexter/keras_squeezenet2
pip install -q keras_squeezenet2/
~~~


### Library Versions

- Tensorflow v2.rc1



### Example Usage

~~~python
import numpy as np
from keras_squeezenet_tf2 import SqueezeNet
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

model = SqueezeNet()

img = image.load_img('../images/cat.jpeg', target_size=(227, 227))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
print('Predicted:', decode_predictions(preds))

~~~


### References

1) [Tensorflow Framework](www.tensorflow.org)

2) [SqueezeNet Official Github Repo](https://github.com/DeepScale/SqueezeNet)

3) [SqueezeNet Paper](http://arxiv.org/abs/1602.07360)


### Licence 

MIT License 

Note: If you find this project useful, please include reference link in your work.
