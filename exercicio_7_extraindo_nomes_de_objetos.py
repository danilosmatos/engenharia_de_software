class Estoque:
    def __init__(self, produto):
        self.produto = produto

def extrair_nomes(lista):
    return [i.produto for i in lista]

p1 = Estoque("Gabinete")
p2 = Estoque("CPU")
p3 = Estoque("Placa de video")

l_estoque = [p1,p2,p3]

print(extrair_nomes(l_estoque))