import matplotlib.pyplot as plt


class Preguntas:
    def __init__(self):
        self.preguntas = {}
    
    def añadir_enunciado(self, enun):
        if isinstance(enun, str):
            return enun
        else:
            return None
    
    def añadir_respuestas(self, respuestas):
        # Ensure respuestas is a tuple of 4 elements, each a tuple with (text, is_correct)
        if isinstance(respuestas, tuple) and len(respuestas) == 4:
            all_valid = all(isinstance(r, tuple) and len(r) == 2 for r in respuestas)
            if all_valid:
                return respuestas
        return None
    
    def añadir_pregunta(self, enunciado, respuestas):
        enun_valido = self.añadir_enunciado(enunciado)
        respuestas_validas = self.añadir_respuestas(respuestas)
        
        if enun_valido is None or respuestas_validas is None:
            print("No se ha guardado la pregunta. Formato no válido.")
            return None
        
        # Añadir la pregunta y las respuestas al diccionario
        self.preguntas[enun_valido] = respuestas_validas
        print(f"Pregunta añadida: {enun_valido}")
        return self.preguntas


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aciertos = 0
        self.fallos = 0


class Trivial(Preguntas):
    def __init__(self):
        super().__init__()  # Initialize Preguntas
        self.jugadores = []
        
    def crear_jugadores(self):
        n_jugadores = int(input("Especifica el número de jugadores: "))
        for i in range(n_jugadores):
            nombre = input(f"Introduce el nombre del jugador {i + 1}: ")
            jugador = Jugador(nombre)  # Crear una instancia de Jugador
            self.jugadores.append(jugador)  # Añadir a la lista de jugadores
            
    def base_del_juego(self, par):
        match par:
            case 0:
                # Modo en el que se añaden preguntas manualmente (pedir input)
                for _ in range(2):  # Asumimos que quieres añadir 2 preguntas
                    enunciado = input("Enunciado de la pregunta: ")
                    
                    # Simulamos que se añaden 4 respuestas, cada una con un booleano que indica si es correcta
                    respuestas = []
                    for i in range(4):
                        respuesta = input(f"Respuesta {i + 1}: ")
                        es_correcta = input(f"¿Es la respuesta {i + 1} correcta? (s/n): ").lower() == 's'
                        respuestas.append((respuesta, es_correcta))
                    
                    self.añadir_pregunta(enunciado, tuple(respuestas))  # Convertir respuestas a tupla
                
                self.crear_jugadores()
                
                print("Preguntas registradas:")
                for enunciado, respuestas in self.preguntas.items():
                    print(f"{enunciado}: {respuestas}")
            
            case 1:
                # Modo con preguntas predefinidas
                self.preguntas = {
                    "¿Cuál es el planeta más cercano al Sol?": (
                        ("Venus", False),
                        ("Tierra", False),
                        ("Mercurio", True),
                        ("Marte", False)
                    ),
                    "¿Cuál es el océano más grande del mundo?": (
                        ("Océano Atlántico", False),
                        ("Océano Índico", False),
                        ("Océano Ártico", False),
                        ("Océano Pacífico", True)
                    ),
                    "¿Quién pintó la Mona Lisa?": (
                        ("Vincent van Gogh", False),
                        ("Leonardo da Vinci", True),
                        ("Pablo Picasso", False),
                        ("Claude Monet", False)
                    ),
                    "¿En qué año llegó el hombre a la Luna?": (
                        ("1965", False),
                        ("1969", True),
                        ("1972", False),
                        ("1963", False)
                    ),
                }
                
                # Omitir creación de jugadores aquí si no es necesario, pero puedes habilitar si es parte del flujo
                self.crear_jugadores()
                
                print("Preguntas predefinidas registradas:")
                for enunciado, respuestas in self.preguntas.items():
                    print(f"{enunciado}: {respuestas}")

    
    def mostrar_resultados(self):
        # Extraer nombres, aciertos y fallos de los jugadores
        nombres = [jugador.nombre for jugador in self.jugadores]
        aciertos = [jugador.aciertos for jugador in self.jugadores]
        fallos = [jugador.fallos for jugador in self.jugadores]
        
        # Crear el gráfico de barras
        fig, ax = plt.subplots()
        
        # Indices de las posiciones de las barras
        index = range(len(self.jugadores))
        
        # Crear las barras para aciertos y fallos
        bar_width = 0.35  # Ancho de las barras
        bar1 = ax.bar(index, aciertos, bar_width, label='Aciertos', color='green')
        bar2 = ax.bar([i + bar_width for i in index], fallos, bar_width, label='Fallos', color='red')
        
        # Etiquetas y título
        ax.set_xlabel('Jugadores')
        ax.set_ylabel('Cantidad')
        ax.set_title('Aciertos y Fallos por Jugador')
        ax.set_xticks([i + bar_width / 2 for i in index])  # Ajustar la posición de los ticks
        ax.set_xticklabels(nombres)  # Etiquetar las barras con los nombres de los jugadores
        ax.legend()
        
        # Mostrar el gráfico
        plt.tight_layout()
        plt.show()
    
    
    def jugar(self):
        print("\n--- Comienza el juego ---\n")
        
        # Recorrer las preguntas
        for enunciado, respuestas in self.preguntas.items():
            print(f"Pregunta: {enunciado}")
            for idx, (respuesta, _) in enumerate(respuestas):
                print(f"{idx + 1}. {respuesta}")
            
            # Turno para cada jugador
            for jugador in self.jugadores:
                eleccion = int(input(f"{jugador.nombre}, elige tu respuesta (1-4): ")) - 1
                if respuestas[eleccion][1]:  # El segundo elemento de la tupla indica si es correcta
                    # print("¡Correcto!")
                    jugador.aciertos += 1
                else:
                    # print("Incorrecto.")
                    jugador.fallos += 1
        
        # Final del juego: Mostrar los resultados
        print("\n--- Fin del juego ---\n")
        for jugador in self.jugadores:
            print(f"{jugador.nombre} - Aciertos: {jugador.aciertos}, Fallos: {jugador.fallos}")
            
        self.mostrar_resultados()


# Example of usage
juego = Trivial()

# To start the game, uncomment the lines below:
juego.base_del_juego(1)
juego.jugar()
