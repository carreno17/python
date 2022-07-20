from PIL import Image
"""Para poder colocar un fondo debemos tener una imagen png, sin fondo,
es decir que el fondo sea 0, transparente"""
if __name__ == '__main__':
    try:
        imagen = Image.open('imagenessave/img_sinfondo.png')

        """Esto quiere sir si los pixeles son == 0, me realiza el for
        y agrega los colores que puse en la tupla, de lo contrarío
        me imprime el pixel si tiene un valor diferente de 0"""
        new_lista = [
            (200,600,400) if pixel[3] == 0 else pixel
            for pixel in imagen.getdata() #Recorre todos los pixeles
        ]
        imagen.putdata(new_lista)
        imagen.show()
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')