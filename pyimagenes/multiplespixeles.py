from PIL import Image

if __name__ == '__main__':
    try:
        #getpixel se usa para editar una cantidad de pixelis
        #getdata si queres editar todos los pixeles

        imagen = Image.open('imagenes/segunda.jpg')
        
        pixeles = imagen.getdata()#Va ser una lista(que va contener todos los pixeles)

        todos_pixeles = [
            (100, pixel[1], 0) #R, G, D
            for pixel in pixeles
        ]
        #Acá le pasaremos la lista a la imagen con .putdata
        imagen.putdata(todos_pixeles)
        imagen.show()
       
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')