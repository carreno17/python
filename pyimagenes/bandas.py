from PIL import Image

if __name__ == '__main__':
    try:
        imagen = Image.open('imagenes/tercera.jpg')
        """Para las bandas se usa don modos"""
        bans = imagen.getbands()#1
        print(bans) #Obtendremos los colores
        red, grend, blue = imagen.split()
        red.show()
        grend.show()
        blue.show()


    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')