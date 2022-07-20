
from PIL import Image

if __name__ == '__main__':
    try:
        imagen = Image.open('imagenes/primera.jpg')#Open es para cargar la imagen

        #imagen.show() #El show sirve para imprimir la imagen en pantalla

        print(imagen.size) # Me muesta (Ancho, Alto)

        whidth, height = imagen.size
        print('Ancho', whidth)
        print('Alto', height)

        print(imagen.mode) #Sirve para ver cuantos colores tiene una imange RGB(Tres colores)
        print(imagen.format) #Sirve para ver el formato de la imange

        """el .convert 
        Para convertir una imagen en otro color en este caso será blanco y 
        negro, se usa el L para una imagen blanco y negro"""
        convertido = imagen.convert('L')
        #convertido.show() # Imprimir la imagen
        #.save se usa para guardar esa imagen en algun que se quiera
        convertido.save('imagenes/white_and_black.jpg')
        
        """Rotar una imange
        Se usa el metodo .rotate para rocatar poco grados 45 y trambien
        se usa el expand, para que no se vea la imagen cortada,
        y el metodo .transpose este usa constantes .ROTATE_90"""
        rotar = imagen.rotate(45, expand =True )#Rotara 45 grados
        #rotar.show()
        rotar2 = imagen.transpose(Image.ROTATE_90)
        #rotar2.show()

        """Cambiar el tamaño de una imangen se usa el metodo
        rasize"""
        ancho = imagen.size[0]
        alto = imagen.size[1]

        cambiar_tamaño = imagen.resize((600,300))#600 es el ancho y 300altura
        cambiar_tamaño.show()
    
        
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')