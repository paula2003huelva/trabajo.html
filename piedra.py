import random
 
# Tipo enumerado de los posibles valores asociados a un código
(PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK) = range(5)
 
# Valores ordenados por posición
valores = ["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"]
 
# Reglas del juego. La clave representa la posición en el vector de valores. El valor de cada clave es la manera en que un elemento vence a otro y los elentos a los que puede vencer.
# Por ejemplo, la posición 0 representa PIEDRA. PIEDRA aplasta a LAGARTO y PIEDRA aplasta a TIJERA
reglas = {0: [["aplasta", "aplasta"],[LAGARTO, TIJERA]], 1: [["tapa", "desautoriza"],[PIEDRA, SPOCK]], 2: [["corta", "decapita"],[PAPEL, LAGARTO]], 3: [["envenena", "come"],[SPOCK, PAPEL]], 4: [["rompe", "vaporiza"],[TIJERA, PIEDRA]]}
(GANAUSUARIO, GANAMAQUINA, EMPATE) = range(3)
 
# Obtiene una cadena de texto a partir del código de la tirada
# Ej: valorTexto(0) = PIEDRA
def valorTexto(codigo):
    return valores[codigo]
 
# Devuelve el código de la tirada a partir de la cadena de texto de la tirada
# Ej: textoValor("PIEDRA") = 0
def textoValor(texto):
    for i, valor in enumerate(valores):
        if (texto == valor):
            return i
 
# Tirada de la máquina
def sacaMaquina():
        tirada = random.randint(0,5)
        return tirada;
 
# Tirada del usuario
def sacaUsuario():
        tirada = ""
        while not tirada in valores:
            tirada = input("¡Mucha suerte!(PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK):")
            return textoValor(tirada);
 
# Valida la jugada
def juego(usuario, maquina):
    if maquina in reglas[usuario] [1]:
        return GANAUSUARIO
    elif usuario in reglas[maquina][1]:
        return GANAMAQUINA
    else:
        return EMPATE
 
# Explica la jugada
# Ej: explica(TIJERA, PAPEL) =
def explica(ganador, perdedor):
        for i in enumerate(reglas[ganador][1]):
                if (perdedor == valor):
                    print (ganador), reglas[ganador][0][i], valor(perdedor)
 
########################
### CUERPO PRINCIPAL ###
########################
 
# Tiradas de los usuarios
usuario = sacaUsuario()
maquina = sacaMaquina()
print (usuario), "VS", valorTexto(maquina)
 
# Comprueba la jugada y muestra el resultado
resultado = juego(usuario, maquina)
if resultado == GANAUSUARIO:
        explica(usuario, maquina)
        print ("¡Has ganado!")
elif resultado == GANAMAQUINA:
        explica(maquina, usuario)
        print ("¡Has perdido!")
else:
        print ("¡Empate!")
