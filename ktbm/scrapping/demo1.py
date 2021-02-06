# Importar módulos
import requests
import os
import urllib.request
import ebooklib
from ebooklib import epub
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# tipo de archivo a buscar
type_file = "epub"
url_aux_download = ""
# Ingreso nombre del libro
name_book = "el problema de los tres cuerpos"
name_book_page_search = "/book/"+"-".join(name_book.split())
# Dirección path para guardar libros
path_out = os.getcwd() + "\\book_download\\"
#    Creando paths de salida del libro (carpeta y archivo nombre)
sub_folder = path_out + name_book.upper() + "\\"
os.makedirs(sub_folder, exist_ok=True)
# Direcciones de la páginas web a utilizar
url_main = "https://www.lectulandia.co{}"
url_main_out = "https://www.antupload.com{}"
# Dirección donde se encuentra el libro en Lectulandia
url_book = url_main.format(name_book_page_search)
# Ejecutar GET-Request
response = requests.get(url_book)
# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')

#Todo: imprimir la información del libro encontrado

# Extraer todas las citas y autores del archivo HTML
download_html = html.find_all(class_="stackButton")
for index_value in range(len(download_html)):
    tag_download = download_html[index_value]
    # Sacando atributo value del tag actual
    type_file_url = tag_download.attrs["value"]
    # Seleccionando url según tipo de archivo a descargar
    if type_file_url == type_file:
        url_aux_download = tag_download.parent.attrs["href"]
# Creando link de redirección
url_download = url_main.format(url_aux_download)
# TODO: Validador de url de descarga a rederigir
# Todo: Generar funcion de lo de abajo
# Creando driver para apertura de pagina
## Configurando opciones para descarga en folder especifico
f_options = FirefoxOptions()
f_options.add_argument("download.default_directory=\"{}\"".format(sub_folder))
## Creando driver con opciones
browser = webdriver.Firefox(options=f_options)
#Abriendo pagina de descarga
browser.get(url_download)
time.sleep(16)
# Buscando ID asociado a descarga
id_download = "downloadB"
name = browser.find_element_by_id(id_download)
name.click()
browser.quit()








# # Pagina final de redirección con objeto a descargar
# html_end = browser.page_source
# # Transformando a objeto de busqueda BS4
# soup = BeautifulSoup(html_end, 'lxml')
# # Buscando ID asociado a descarga
# id_download = "fileDownload"
# div_download = soup.find("div", {"id":id_download})
# # Sacando URL de descarga final de libro
# url_end_download = div_download.contents[1].attrs["href"]
# url_book_download = url_main_out.format(url_end_download)
# # browser.quit()
# # # Todo:Generar funcion para guardado de epub
# # # Creando paths de salida del libro (carpeta y archivo nombre)
# # sub_folder = path_out + name_book.upper() + "\\"
# # file_out = sub_folder + name_book.upper() + ".epub"
# # # Creando sub-folder
# # os.makedirs(sub_folder, exist_ok=True)
# # browser_epub = webdriver.Firefox()
# # browser_epub.get(url_book_download)
# #
#
#
#
#
#
#

# # Generando request de descarga del libro
# with urllib.request.urlopen(url_book_download) as url:
#     epub_script = url.read()
# # Guardando EPUB en carpeta de salida
# with open(file_out, 'wb') as path:
#     path.write(epub_script)
# # Muestra del libro final
# book = epub.read_epub("r{}".format(file_out))
# for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
#     print(image)
#


