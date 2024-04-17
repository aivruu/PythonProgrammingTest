# Class Test N~1 - 16/04/2024

# We request the values the variables needed to perform
# this exercise, and perform some necessary checks with
# the parameters before execute some action.

# If some condition is not fulfilled, will terminate the
# program with a specific exit message for the not fulfilled
# condition.
armyMember = input("Eres un miembro del ejercito del señor oscuro?")
if armyMember == "Si":
    pass
elif armyMember == "No":
    exit("No formas parte del ejercito del señor oscuro!")
else:
    exit("La respuesta no es válida.")

height = int(input("Cuál es tu estatura?"))
if height >= 140:
    exit("Debes medir menos de 1.40 de estatura.")

color = input("Cuál es tu color?")
if not color == "verde" and not color == "rojo":
    exit("Debes ser de color 'verde', o 'rojo'!")

weight = int(input("Cuál es tu peso?"))
if weight < 30:
    exit("Debes pesar al menos 30 kg!")

# We want to check if our friend will launch a "Trasgo",
# if not, will terminate the program with the next message.
launchTrasgo = input("Lanzar un Trasgo?")
if launchTrasgo == "Si":
    pass
elif launchTrasgo == "No":
    exit("No se ha lanzado un Trasgo.")

# We check the distance that will cover the launch using two
# formulas, one for "green" color, and another for the "red"
# color.
distance = 0
if color == "verde":
    # We multiply the 10, two times by the weight, and by the
    # height one time.
    distance = 10 * weight * weight * height
else:
    # We multiply the 2, one time by the weight, and two times by
    # the height.
    distance = 2 * weight * height * height

# We show some information to the user.
print("===========")
print("Verdepus ha lanzado un Trasgo y grita:")
print("- Wooyah!")
print()
print("El Trasgo llegará a una distancia de " + str(distance) + " metros.")
print("===========")

# We check if the calculated distance for the launch
# is higher or equal than 1000000 (1.000 km) meters.
if distance >= 1000000:
    print("El Trasgo ha recorrido 1.000 km y se ha prendido en llamas!")

# We say that program execution has ended.
print("Ejecución del programa finalizada!")
