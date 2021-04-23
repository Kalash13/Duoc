# #Validacion de edad
# input ("Ingrese su edad ")
# edad = int (0)
# if edad >= 18: 
#     print("Podi en entrar cabro qlo grande")

# else:
#     print("Sale altoke pendejo qlo")

#Validacion de usuario y contraseña

#user = (input("Username:"))

#Esto es para sacar el promedio
# nota1 = float  (input("ingrese primera nota"))
# nota2 = float (input("Ingrese segunda nota"))
# nota3 = float  (input("Ingrse tercera nota"))
# promedio = (nota1+nota2+nota3)/3
# print(promedio)
# if promedio >= 4:
#     print(f"Su promedio es: {promedio} Felicidades aprobo el ramo " )

# else: 
#     print("Usted reprobo el Ramo ")


print("¿Cuál de los siguientes animales vive en el agua?")
animals= ["1. perro", "2. cocodrilo", "3. conejo" , "4. tiburón"]
for x in animals:
    print(x)


respuesta = int (input("Ingrese su respuesta con el numero asignado al animal: "))
points = 0

if respuesta == 2:
    points = (points + 0.5)

elif respuesta == 4:
    points = (points + 1)

else:
    print("Intente nuevamente")

print(f"Su puntaje es de : {points} ")












