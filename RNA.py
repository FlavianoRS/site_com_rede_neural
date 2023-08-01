import tensorflow as tf
import PIL
import os


class RNA:
    def __init__(self) -> None:
        pass

    def imagens(diretorio, extensao):
        imagens=[]
        for arqs in os.listdir(diretorio):
            if arqs.endswith(extensao):
                imagens.append(arqs)
                

    
    def ConstModel(self,num_neuro, num_camada, num_classes):
        self.num_neuro = num_neuro
        self.num_camada = num_camada
        self.num_classes = num_classes
        self.modelo  = tf.keras.models.Sequential()
        self.modelo.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu", input_shape=[32,32,3]))
        self.modelo.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding="valid"))
        self.modelo.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding="same", activation="relu"))
        self.modelo.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding="valid"))
        self.modelo.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding="same", activation="relu"))
        self.modelo.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding="valid"))
        self.modelo.add(tf.keras.layers.Flatten())
        for i in range(1, self.num_camada+1):
            if i == self.num_camada:
                self.modelo.add(tf.keras.layers.Dense(units=self.num_classes, activation="softmax"))
            else:
                aux = int(self.num_neuro / i)
                if aux <= self.num_classes:
                    self.modelo.add(tf.keras.layers.Dense(units=self.num_classes, activation="relu"))
                else:
                    self.modelo.add(tf.keras.layers.Dense(units=aux, activation="relu"))
                    
        self.modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['Accuracy'])
        
        return self.modelo