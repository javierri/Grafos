# Grafo - nodos enlazados -
# Autor: Javier Rivera

class Grafo:
	def __init__(self):
		self.__nodos = []
		self.__matriz = []
		
	def buscaNodo(self,valor):
		if (valor in self.__nodos):
			return self.__nodos.index(valor)
		return -1
		
	def ins_nodo(self, valor):
		if (self.buscaNodo(valor) < 0):
			self.__nodos.append(valor)
			self.__matriz.append({})
			return True
		return False
		
	def ins_arco(self, valOrigen, valDestino, peso = 1):
		posOrigen = self.buscaNodo(valOrigen)
		posDestino = self.buscaNodo(valDestino)
		if (posOrigen >= 0 and posDestino >= 0):
			self.__matriz[posOrigen][posDestino] = peso
			return True
			
		return False
		
	def mostrar_nodos(self):
		i = 0
		for nodo in self.__nodos:
			print i, nodo
			i = i + 1
			
	def mostrar_arcos(self, valor):
		posOrigen = self.buscaNodo(valor)
		if (posOrigen < 0):
			return False
			
		for posDestino in self.__matriz[posOrigen]:
			peso = self.__matriz[posOrigen][posDestino]
			print self.__nodos[posDestino], peso
			
	def existe_arco(self,valOrigen, valDestino):
		posOrigen = self.buscaNodo(valOrigen)
		posDestino = self.buscaNodo(valDestino)
		if (posOrigen >= 0 and posDestino >= 0):
			if (posDestino in self.__matriz[posOrigen]):
				return True

		return False
    
# PRINCIPAL

g = Grafo()
g.ins_nodo("A")
g.ins_nodo("B")
g.ins_nodo("C")
g.ins_nodo("D")
g.ins_nodo("E")

g.ins_arco("A","B")
g.ins_arco("A","C",3)
g.ins_arco("A","A",1)
g.ins_arco("A","D",1)
g.ins_arco("C","B")
g.ins_arco("C","D")
g.ins_arco("D","E")

print "Nodos"
g.mostrar_nodos()

print "arcos de A"
g.mostrar_arcos("A")

print "Eciste arco de A a B", g.existe_arco("A","B")
print "Eciste arco de A a E", g.existe_arco("A","E")

