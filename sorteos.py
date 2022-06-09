from abc import ABC, abstractmethod
from random import randint

class Loteria(ABC):
    L_COMBINACION = 6
    MAX_COMBINACION = 49
    
    def __init__(self):
        self.combinación = []
        
    def _generar_números(self):
        self.combinación = []
        cont_numeros = 0
        while cont_numeros < self.L_COMBINACION:
            numero = randint(1, self.MAX_COMBINACION)
            if numero not in self.combinación:
                self.combinación.append(numero)
                cont_numeros += 1
            
        self.combinación.sort()
    
    @abstractmethod
    def get_boleto(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
class Euromillon(Loteria):
    L_COMBINACION = 5
    L_ESTRELLAS = 2
    MAX_COMBINACION = 50
    MAX_ESTRELLAS = 12
    
    def __init__(self):
        super().__init__()
        self.estrellas = []
        self._generar_números()
        
    def _generar_números(self):
        super()._generar_números()
        
        cont_numeros = 0
        while cont_numeros < self.L_ESTRELLAS:
            numero = randint(1, self.MAX_ESTRELLAS)
            if numero not in self.estrellas:
                self.estrellas.append(numero)
                cont_numeros += 1
        self.estrellas.sort()
        
    def get_boleto(self):
        boleto = []
        boleto[0] = self.combinacion
        boleto[1] = self.estrellas
        return boleto
        
    
    def __str__(self):
        return f"{self.combinación} - {self.estrellas}"    
    
class Primitiva(Loteria):
    
    
    def __init__(self):
        super().__init__()
        self._generar_números()
        
    def _generar_números(self):
        super()._generar_números()
        
    def get_boleto(self):
        return self.combinación
        
    def __str__(self):
        return self.combinación
    
class Registro:
    def __init__(self):
        self.euromillones = []
        self.primitivas = []
        
    def add_euromillon(self, euromillon):
        self.euromillones.append(euromillon)
        
    def add_primitiva(self, primitiva):
        self.primitivas.append(primitiva)
        
class Sorteo:
    def __init__(self, registro):
        self.registro = registro
        self.__sortear()
        
    def __sortear(self):
        self.euromillon = Euromillon()
        self.primitiva = Primitiva()
        
    def mostrar_resultados(self):
        print(self.euromillon)
        print(self.primitiva)
        
    def __n_aciertos_primitiva(self, primitiva):
        n_aciertos = 0
        resultado_sorteo = self.primitiva.get_boleto()
        boleto = primitiva.get_boleto()
        for numero in boleto:
            if numero in resultado_sorteo:
                n_aciertos += 1
        return n_aciertos
    def mostrar_aciertos_primitivas(self):
        print(f"Combinacion ganadora de la primitiva: {self.primitiva.get_boleto()}")
        for primitiva in self.registro.primitivas:
            print(f"{primitiva.get_boleto()} - {self.__n_aciertos_primitiva(primitiva)}")
    

            
    def mostrar_estadisticas_primitivas(self):
        print(f"Combinacion ganadora de la primitiva: {self.primitiva.get_boleto()}")
        aciertos = []
        for i in range(Primitiva.L_COMBINACION):
            aciertos.append(0)
        for primitiva in self.registro.primitivas:
            n_aciertos_boleto = self.__n_aciertos_primitiva(primitiva)
            aciertos[n_aciertos_boleto] += 1
        for i in range(Primitiva.L_COMBINACION):
            print(f"{i} aciertos: {aciertos[i]}")
            
if __name__ == "__main__":
    # Generamos 10 primitivas y las registramos
    registro = Registro()
    for i in range(10):
        primitiva = Primitiva()
        registro.add_primitiva(primitiva)
        
    # Realizamos un sorteo
    sorteo = Sorteo(registro)
    
    # Mostramos los resultados de la primitiva
    sorteo.mostrar_aciertos_primitivas()
    sorteo.mostrar_estadisticas_primitivas()
    
        
        
        
