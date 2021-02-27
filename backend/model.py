'''
THIS MODEL RECOGNIZES:

apple
banana
beetroot
bell pepper
cabbage
capsicum
carrot
cauliflower
chilli pepper
corn
cucumber
eggplant
garlic
ginger
grapes
jalepeno
kiwi
lemon
lettuce
mango
onion
orange
paprika
pear
peas
pineapple
pomegranate
potato
raddish
soy beans
spinach
sweetcorn
sweetpotato
tomato
turnip
watermelon
'''

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.densenet import preprocess_input, decode_predictions
# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="./model.tflite")#take in tflite file
interpreter.allocate_tensors()
img_path = './model_test/chillipepper.jpg'#image path
img = image.load_img(img_path, target_size=(224, 224))#resize image
x = image.img_to_array(img)#transform image file to array of numbers
x = np.expand_dims(x, axis=0)#add another dim to fit input of model
x = preprocess_input(x)#process input
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(input_details)
interpreter.set_tensor(input_details[0]['index'], x)#interpretor takes in data
interpreter.invoke()#invoke interpretor
output_data = interpreter.get_tensor(output_details[0]['index'])#get ouput data
print(output_data)#print data
label_array=['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelo']
#fruit labels
max=0
label_loc=0
for i in range (0,len(output_data[0])):#finds highest probability and location
    if(output_data[0][i]>max):
        max=output_data[0][i]
        label_loc=i
print(max)#print max prob
print(label_array[label_loc])#using location of highest probability, find what fruit it is from label_array