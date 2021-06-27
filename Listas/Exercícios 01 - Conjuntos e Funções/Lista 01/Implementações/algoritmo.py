class Conjunto:
    def __init__(self):
        self.elementos = []

    def gerar_conjunto_partes(self):
        lista_elementos = self.elementos.copy()
        tamanho = len(lista_elementos)
        subconjunto = []

        for i in range(2**tamanho):
            for k in range(tamanho):
                if i&1<<k:
                    subconjunto.append(lista_elementos[k])
            lista_elementos.append(subconjunto)
            subconjunto = []

        print(lista_elementos)

    def adicionar_elemento(self, item):
        if item not in self.elementos:
            self.elementos.append(item)

    def remover_elemento(self,item):
        if item in self.elementos:
             self.elementos.pop(item)


c = Conjunto()
c.adicionar_elemento('a')
c.adicionar_elemento('b')
c.adicionar_elemento('c')
c.adicionar_elemento(1)
c.gerar_conjunto_partes();
