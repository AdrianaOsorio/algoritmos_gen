#Funciones.py
# algoritmos_geneticos/genetico.py
import random

class AlgoritmoGenetico:
    def __init__(self, poblacion, funcion_aptitud, prob_cruce=0.8, prob_mutacion=0.01,
                 tipo_cruce="punto_unico", tipo_mutacion="voltear", tipo_seleccion="torneo", elitismo=False):
        self.poblacion = poblacion
        self.funcion_aptitud = funcion_aptitud
        self.prob_cruce = prob_cruce
        self.prob_mutacion = prob_mutacion
        self.tipo_cruce = tipo_cruce
        self.tipo_mutacion = tipo_mutacion
        self.tipo_seleccion = tipo_seleccion
        self.elitismo = elitismo

    def seleccionar(self):
        if self.tipo_seleccion == "torneo":
            seleccionados = random.sample(self.poblacion, 2)
            seleccionados.sort(key=self.funcion_aptitud, reverse=True)
            return seleccionados[0]
        elif self.tipo_seleccion == "ruleta":
            aptitud_total = sum(self.funcion_aptitud(ind) for ind in self.poblacion)
            seleccion = random.uniform(0, aptitud_total)
            actual = 0
            for individuo in self.poblacion:
                actual += self.funcion_aptitud(individuo)
                if actual > seleccion:
                    return individuo

    def cruzar(self, padre1, padre2):
        if random.random() < self.prob_cruce:
            if self.tipo_cruce == "punto_unico":
                punto_cruce = random.randint(1, len(padre1) - 1)
                hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
                hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
            elif self.tipo_cruce == "dos_puntos":
                punto1 = random.randint(1, len(padre1) - 2)
                punto2 = random.randint(punto1, len(padre1) - 1)
                hijo1 = padre1[:punto1] + padre2[punto1:punto2] + padre1[punto2:]
                hijo2 = padre2[:punto1] + padre1[punto1:punto2] + padre2[punto2:]
            return hijo1, hijo2
        else:
            return padre1, padre2

    def mutar(self, individuo):
        if self.tipo_mutacion == "voltear":
            mutado = []
            for gen in individuo:
                if random.random() < self.prob_mutacion:
                    mutado.append(1 - gen)
                else:
                    mutado.append(gen)
            return mutado
        elif self.tipo_mutacion == "intercambiar":
            if random.random() < self.prob_mutacion:
                pos1 = random.randint(0, len(individuo) - 1)
                pos2 = random.randint(0, len(individuo) - 1)
                individuo[pos1], individuo[pos2] = individuo[pos2], individuo[pos1]
            return individuo

    def ejecutar(self, generaciones):
        for _ in range(generaciones):
            nueva_poblacion = []
            if self.elitismo:
                mejor = max(self.poblacion, key=self.funcion_aptitud)
                nueva_poblacion.append(mejor)

            while len(nueva_poblacion) < len(self.poblacion):
                padre1 = self.seleccionar()
                padre2 = self.seleccionar()
                hijo1, hijo2 = self.cruzar(padre1, padre2)
                hijo1 = self.mutar(hijo1)
                hijo2 = self.mutar(hijo2)
                nueva_poblacion.extend([hijo1, hijo2])

            self.poblacion = nueva_poblacion[:len(self.poblacion)]
            mejor = max(self.poblacion, key=self.funcion_aptitud)
            print(f"Mejor solución: {mejor} con aptitud: {self.funcion_aptitud(mejor)}")
