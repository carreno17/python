from PIL import Image

if __name__ == '__main__':
    try:
        imagen = Image.open('imagenes/tercera.jpg')
        imagen.show()
        """Para recortar una imagen se usa el metodo .crop y le pasamos una
        tupla con las cordenadas"""
        recortar = imagen.crop(
           (100, 152, 300,400) #(left, upper, right, lower) 
        )
        #Agrando está imagen recortada a la carpeta save que están las 
        #Imagenes editadas
        recortar.save('imagenessave/imagen_recortada.jpg')
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')