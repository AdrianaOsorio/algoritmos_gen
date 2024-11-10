import random

# Funciones de evaluación (fitness)
def suma_genes(individuo):
    """Función de aptitud que suma los valores de los genes en un individuo."""
    return sum(individuo)

def contar_unos(individuo):
    """Función de aptitud que cuenta el número de unos en el individuo."""
    return sum(1 for gen in individuo if gen == 1)


# Función de inicialización de población
def generar_poblacion_aleatoria(tamano_poblacion, longitud_individuo):
    """Genera una población de individuos aleatorios."""
    return [[random.randint(0, 1) for _ in range(longitud_individuo)] for _ in range(tamano_poblacion)]


# Funciones de selección
def seleccion_torneo(poblacion, funcion_aptitud, tamano_torneo=2):
    """Realiza selección por torneo para escoger un individuo."""
    seleccionados = random.sample(poblacion, tamano_torneo)
    seleccionados.sort(key=funcion_aptitud, reverse=True)
    return seleccionados[0]

def seleccion_ruleta(poblacion, funcion_aptitud):
    """Realiza selección por ruleta para escoger un individuo."""
    aptitud_total = sum(funcion_aptitud(ind) for ind in poblacion)
    seleccion = random.uniform(0, aptitud_total)
    actual = 0
    for individuo in poblacion:
        actual += funcion_aptitud(individuo)
        if actual > seleccion:
            return individuo


# Funciones de cruce
def cruce_punto_unico(padre1, padre2):
    """Realiza cruce de un solo punto entre dos padres."""
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def cruce_dos_puntos(padre1, padre2):
    """Realiza cruce de dos puntos entre dos padres."""
    punto1 = random.randint(1, len(padre1) - 2)
    punto2 = random.randint(punto1, len(padre1) - 1)
    hijo1 = padre1[:punto1] + padre2[punto1:punto2] + padre1[punto2:]
    hijo2 = padre2[:punto1] + padre1[punto1:punto2] + padre2[punto2:]
    return hijo1, hijo2


# Funciones de mutación
def mutacion_voltear(individuo, prob_mutacion):
    """Aplica mutación de voltear en el individuo."""
    return [1 - gen if random.random() < prob_mutacion else gen for gen in individuo]

def mutacion_intercambio(individuo, prob_mutacion):
    """Aplica mutación de intercambio en el individuo."""
    if random.random() < prob_mutacion:
        pos1 = random.randint(0, len(individuo) - 1)
        pos2 = random.randint(0, len(individuo) - 1)
        individuo[pos1], individuo[pos2] = individuo[pos2], individuo[pos1]
    return individuo
