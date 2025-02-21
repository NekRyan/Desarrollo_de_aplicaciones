class AlgoritmosSecuenciales:

    def __init__(self, numero):
        self.numero = numero

    def suma_n_numeros(self):
        return sum(range(1, self.numero +1))
    
    def factorial(self):
        resultado = 1
        for i in range(1, self.numero +1)
            resultado *= i
        return resultado
    
    def fibonacci(self):
        secuencia = [0,1]
        for _ in range(2, self.numero):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:self.numero]
        