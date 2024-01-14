# Implementación de Redes Neuronales

Este proyecto desarrolla un modelo de red neuronal utilizando TensorFlow para clasificar dígitos escritos a mano del dataset MNIST.

## Características
- Implementación con TensorFlow 2.
- Uso de la API Sequential para la construcción del modelo.
- Regularización con Dropout.
- Salida Softmax para clasificación multiclase.

## Requisitos
- Python 3.x
- TensorFlow 2.x
- Matplotlib (para visualización)

## Instalación
```bash
pip install tensorflow matplotlib
```

## Uso
1. Ejecuta el script principal para entrenar el modelo, evaluar su rendimiento y hacer predicciones:
```bash
python IntroRRNN.py
```

2. Para utilizar el modelo y predecir la clase de nuevas imágenes, coloca la imagen en el directorio del proyecto y especifica la ruta correcta en el script.

## Estructura del Modelo
- **Capa Flatten**: Convierte imágenes 2D de 28x28 en un arreglo plano.
- **Capa Densa**: Una capa completamente conectada con 128 neuronas y activación ReLU.
- **Capa de Dropout**: Aplica un dropout de 0.2 para regularización.
- **Capa de Salida**: Una capa densa con 10 neuronas (una para cada dígito) y activación softmax.

## Entrenamiento
El modelo se entrena durante 10 epochs con un split de validación del 20% para monitorear el rendimiento.

## Evaluación
Después del entrenamiento, se evalúa la precisión

del modelo en el conjunto de datos de prueba.

## Predicción
El script incluye una sección para cargar una imagen externa, preprocesarla y predecir el dígito usando el modelo entrenado.

## Nota
Asegúrate de que las imágenes de entrada para la predicción sean en escala de grises y redimensionadas a 28x28 píxeles, similar al conjunto de datos MNIST.

## Contribución
No dudes en hacer un fork del proyecto, enviar pull requests o aportar sugerencias para mejorar el modelo o ampliar las funcionalidades del proyecto.

## Licencia
Especifica aquí la licencia de tu proyecto, usualmente es MIT o GPL para proyectos de código abierto.

---

Recuerda reemplazar `"ruta/image5.png"` con la ruta real de tu imagen cuando uses la parte de predicción del script. Este README proporciona una guía simple y concisa para que los usuarios comiencen con tu proyecto de clasificación MNIST.
