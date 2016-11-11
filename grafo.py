# Grafo - nodos enlazados -
# Autor: Javier Rivera

class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.arcos = []
		
	def enlace (self, destino, peso = 1):
		if (type(nodo) == type(self)):
			arco = Arco(destino, peso)
			self.arcos.append(arco)
			return True
			
		return False
		
	def muestra_enlaces (self):
		for arco in self.arcos: 
			print arco.nodo.info,
			print arco.peso
		
class Arco:
	def __init__ (self, ndestino, peso=0):
		self.nodo = ndestino
		self.peso = peso

class Grafo:
	def __init__(self):
		self.__nodos = []
		
	def buscaNodo (self, valor):
		for nodo in self.__nodos:
			if (nodo.info == valor):
				return nodo
		return False
	
	def enlace(self, origen, destino, peso = 1):
		
		norigen = self.buscaNodo(origen)
		if (not(norigen)):
			return False
			
		ndestino = self.buscaNodo(destino)
		if (not(ndestino)):
			return False
		
		norigen.enlace(ndestino,peso)
		return True
		
	def ins_nodo (self, valor):
		if (self.buscaNodo(valor) == False):
			nodo = Nodo(valor)
			self.__nodos.append(nodo)
			return nodo
			
		return False
				
# Principal

g = Grafo()
nodo1 = g.ins_nodo("A")
nodo2 = g.ins_nodo("B")
nodo3 = g.ins_nodo("C")
nodo4 = g.ins_nodo("D")

nodo1.enlace(nodo2,2)
nodo1.enlace(nodo3,1)
nodo2.enlace(nodo4,1)

print " GRAFO "
print "Enlaces de A"
nodo1.muestra_enlaces()
print "Enlaces de B"
nodo2.muestra_enlaces()

#######

g2 = Grafo()
				
g2.ins_nodo("A")
g2.ins_nodo("B")
g2.ins_nodo("C")
g2.ins_nodo("D")

g2.enlace("A","B",2)
g2.enlace("A","C",1)
g2.enlace("B","D",1)
		
print		
print " GRAFO 2"		
print "Enlaces de A"
nodoA = g2.buscaNodo("A")
nodoA.muestra_enlaces()

print "Enlaces de B"
nodoB = g2.buscaNodo("B")
nodoB.muestra_enlaces()
		
	
	
