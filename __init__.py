'''
    Vehiculo - Clase padre

    - Atributos, esta clase contara con ciertos atributos que las clases hijas podrán heredar
        > marca
        > color
        > numeroRuedas
        > numeroAsientos
    - Constructor __init__ que recibe varios parámetros de entrada y una validación del tipo de dato
    de ciertos parámetros (numRuedas, numAsientos).
    - Método informacion() que ofrece una plantilla para las clases hijas donde podrán añadir contenido
    dependiendo de cada clase hija.
'''
class Vehiculo():
    # Constructor
    def __init__(self, color, marca, numRuedas, numAsientos):
        # Validacion de parámetros 'numeroRuedas' y 'numeroAsientos' que sean valores númericos
        if not isinstance(numRuedas, int) or not isinstance(numAsientos, int):
            raise ValueError("Valores incorrectos")
        
        # Guardado parámetros como atributos
        self.__marca = marca
        self.__color = color
        self.__numeroRuedas = numRuedas
        self.__numeroAsientos = numAsientos

    # Métodos
    def informacion(self, tipoVehiculo):
        mensaje_plantilla = f'[VEHICULO - {tipoVehiculo}]\n-=-=-=- CARACTERÍSTICAS -=-=-=- \nMarca: {self.__marca} \nColor: {self.__color} \nNumero de ruedas: {self.__numeroRuedas} \nNumero de asientos: {self.__numeroAsientos}'
        return mensaje_plantilla


'''
    VehiculoCoche - Clase hija que era de 'Vehiculo'

    - Atributos, atributos propios de esta clase:
        > (atributos de la clase padre 'Vehiculo')
        > numero_puertas
        > capacidad_maletero
    - Constructor __init__ que recibe varios parámetros de entrada y una validación del tipo de dato
    de ciertos parámetros (numRuedas, numAsientos, numPuertas).
    - Método informacion(), recibe como parámetro el 'tipoVehiculo' para especificar de que clase se
    esta llamando (en este caso desde un 'Coche') donde se aplica polimorfismo agrando mas contenido al metodo. Además se 
    emplea la función super() para poder llamar al metodo de la clase padre.
    - Método guardarObjetosMaletero(), aplicando ciertas validaciones que comprueba si hay capacidad en el
    maletero para seguir guardando cosas. Lanzando errores que posteriormente seran capturadas por medio del
    bloque try-except con mensajes de información para el usuario del estado del maletero.
'''
class VehiculoCoche(Vehiculo):
    # Constructor
    def __init__(self, marca, color, numRuedas, numAsientos, numPuertas):
        # Validacion de parámetros 'numRuedas' y 'numAsientos' que sean valores númericos
        if not isinstance(numRuedas, int) or not isinstance(numAsientos, int) or not isinstance(numPuertas, int):
            raise ValueError("Valores incorrectos")

        super().__init__(marca, color, numRuedas, numAsientos)
        self.__numero_puertas = numPuertas
        self.__capacidad_maletero = 0 # Este valor se trata como porcentaje (%)

    # Métodos
    def informacion(self, tipoVehiculo="Coche"):
        mensaje = super().informacion(tipoVehiculo)
        mensaje += f'\n\t-=-=-=-\nNumero de puertas: {self.__numero_puertas} \n-=-=-=--=-=-=--=-=-=-'

        return mensaje
    
    def guardarObjetosMaletero(self, cantidad):
        if self.__capacidad_maletero >= 100:
            raise ValueError("El maletero se encuentra lleno!")

        conversion = cantidad * 10 # Por cada objeto lo multiplicamos por 10 para un mejor manejo en porcentajes para las validaciones
        if conversion > 100:
            raise ValueError("El maletero se encuentra lleno!")

        self.__capacidad_maletero += conversion
        print(f'[i] Guardado exitosamente (Capacidad restante: {self.__capacidad_maletero}/100)')

'''
    VehiculoMotocicleta - Clase hija que era de 'Vehiculo'

    - Atributos, atributos propios de esta clase:
        > (atributos de la clase padre 'Vehiculo')
        > maleteroInstalado
    - Constructor __init__ que recibe varios parámetros de entrada y una validación del tipo de dato
    de ciertos parámetros (numRuedas, numAsientos).
    - Método informacion(), recibe como parámetro el 'tipoVehiculo' para especificar de que clase se
    esta llamando (en este caso desde un 'Motocicleta') donde se aplica polimorfismo agrando mas contenido al metodo. Además se 
    emplea la función super() para poder llamar al metodo de la clase padre.
'''
class VehiculoMotocicleta(Vehiculo):
    # Constructor
    def __init__(self, marca, color, numRuedas, numAsientos, llevaMaletero):
        # Validacion de parámetros 'numRuedas' y 'numAsientos' que sean valores númericos
        if not isinstance(numRuedas, int) or not isinstance(numAsientos, int):
            raise ValueError("Valores incorrectos")
        
        super().__init__(marca, color, numRuedas, numAsientos)
        self.__maleteroInstalado = llevaMaletero

    # Métodos
    def informacion(self, tipoVehiculo="Motocicleta"):
        mensaje = super().informacion(tipoVehiculo)
        mensaje += f'\n\t-=-=-=-\nLleva malatero?: {self.__maleteroInstalado} \n-=-=-=--=-=-=--=-=-=-'

        return mensaje

'''
    VehiculoCamion - Clase hija que era de 'Vehiculo'

    - Atributos, atributos propios de esta clase:
        > (atributos de la clase padre 'Vehiculo')
        > cargaInstalado
    - Constructor __init__ que recibe varios parámetros de entrada y una validación del tipo de dato
    de ciertos parámetros (numRuedas, numAsientos).
    - Método informacion(), recibe como parámetro el 'tipoVehiculo' para especificar de que clase se
    esta llamando (en este caso desde un 'Camion') donde se aplica polimorfismo agrando mas contenido al metodo. Además se 
    emplea la función super() para poder llamar al metodo de la clase padre.
'''
class VehiculoCamion(Vehiculo):
    # Constructor
    def __init__(self, marca, color, numRuedas, numAsientos, llevaCarga):
        # Validacion de parámetros 'numRuedas' y 'numAsientos' que sean valores númericos
        if not isinstance(numRuedas, int) or not isinstance(numAsientos, int):
            raise ValueError("Valores incorrectos")
        
        super().__init__(marca, color, numRuedas, numAsientos)
        self.__cargaInstalado = llevaCarga

    # Métodos
    def informacion(self, tipoVehiculo="Camion"):
        mensaje = super().informacion(tipoVehiculo)
        mensaje += f'\n\t-=-=-=-\nLleva carga?: {self.__cargaInstalado} \n-=-=-=--=-=-=--=-=-=-'

        return mensaje



# -=-=-=-=-=-=-=-=-=-=-=-=
'''
    Por medio del bloque try-except capturaremos los errores y excepciones que puedan
    suceder en las validaciones implementadas dentro del 'try'. Evitando que el programa no
    se detenga de golpe, sino que ejecute una alternativa o muestre un mensajes amigable.
'''
try:
    ''' VEHICULO - COCHE '''
# Creacion de objeto 'coche' de la clase 'VehiculoCoche'
    coche = VehiculoCoche("rojo", "KIA", 4, 3, 4)
    print(coche.informacion())

# Guardar cosas en el maletero
    # En este caso indicamos que queremos guardar 3 objetos en el maletero, mostrando por consola
    # si la operación fue exitosa o no.
    coche.guardarObjetosMaletero(3)

    ''' VEHICULO - MOTOCICLETA '''
# Creacion de objeto 'motocicleta' de la clase 'VehiculoMotocicleta'
    motocicleta = VehiculoMotocicleta("azul", "HONDA", 2, 2, "no")
    print(motocicleta.informacion())
    
    ''' VEHICULO - CAMION '''
# Creacion de objeto 'camion' de la clase 'VehiculoCamion'
    camion = VehiculoCamion("blanco", "VOLVO", 4, 3, "si")
    print(camion.informacion())

except ValueError as e:
    # Captura de errores/excepciones que seran mostradas por medio de la función 'print'
    print(f'Error: {e}')

finally:
    # Parte del código que se ejecutara si hubieran o no errores/excepciones.
    print("Fin del programa :)")
    