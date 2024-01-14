#Importar tensorflow
import tensorflow as tf

#Comprobar versión
print(tf.__version__)

#Crear una red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)), #Aplanar la entrada
    tf.keras.layers.Dense(128, activation='relu'), #Capa oculta con 128 neuronas
    tf.keras.layers.Dropout(0.2), #Regularización con dropout
    tf.keras.layers.Dense(10, activation='softmax') #Última capa con softmax
])

#Carga de los datos
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

#Normalizar los datos
x_train, x_test = x_train/255.0, x_test/255.0

#Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Entrenar la red neuronal
model.fit(x_train, y_train, epochs=10, validation_split=0.2)

#Evaluar la red neuronal
score = model.evaluate(x_test, y_test, verbose=2)
print(f'Precisión en el conjunto de prueba:',score[1])


#Cargar la imagen
image = tf.keras.preprocessing.image.load_img(
    "path/image5.png",
    color_mode="grayscale",
    target_size=(28,28)
)

#Convertir la imagen a una matriz de pixeles y normaliza
image = tf.keras.preprocessing.image.img_to_array(image) / 255.0

#Ajustar la forma de la imagen (añadiendo una dimensión de batch)
image = tf.expand_dims(image,0)

#Predcir la clase de la imagen
prediction = model.predict(image)

#Imprime la prediccion
print(prediction)
