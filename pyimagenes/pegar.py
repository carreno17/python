"""Para pegar una imagen en otra se usa el metodo .paste, este recibe
dos argumentos, la imagen que vamos a pegar y las coordenadas(x, y) 
cabe destacar que tiene que ser enteros los numeros"""
from PIL import Image

if __name__ == '__main__':
    try:
        imagen = Image.open('imagenes/tercera.jpg')#Imagen donde vamos a pegar
        imagen_a_pegar = Image.open('imagenessave/img_sinfondo.png')

        """Para que nuesta imagen no se vea como si estuviese pegada,
        debemos convertirla a png para poder colocarle el fondo transparente
        con la pagina removebg lo hacemos, luego guardamos esa imagen 
        y le cambiamos la ruta a imagen_a_pegar
        """
        imagen.paste(
            imagen_a_pegar,
            (2000, 200), #(x,y)
        )

        imagen.show()
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')