"Contador_de_palabras"
print("Escriba una frase para contar las palabras que tiene"),
x = input()
result = x.split(' ')
number_of_words=str(len(result))
print("Tu frase: " + x + " tiene " + number_of_words + " palabras")
       