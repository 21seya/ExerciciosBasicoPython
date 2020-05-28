import urllib.request 
import urllib.parse
import urllib.error

print("Permite urllib")

input()

#Requisita que se abra um website
google = "https://www.xvideos.com"
pagina = urllib.request.urlopen(google)

print(pagina.read())

input()

print("Mais do que isso podemos até mesmo reter uma página da web ou alguma imagem")

input()

