# Grafo - matriz de adyacencia -
# Autor: Javier Rivera

class Grafo:
	def __init__(self):
		self.__nodos = []
		self.__matriz = []

	# Busca la posicion de un nodo en el arreglo de nodos	
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
			self.__matriz[posOrigen][valDestino] = peso
			return True
		return False
		
	# Muetra los valores (o informacion) de los nodos en el grafo 
	def mostrar_nodos(self):
		i = 0
		for nodo in self.__nodos:
			print i, nodo
			i = i + 1
			
	# Muestra peso y nodo destino de los arcos (o aristas) de un nodo, dado su valor 
	def mostrar_arcos(self, valor):
		posOrigen = self.buscaNodo(valor)
		if (posOrigen < 0):
			return False
			
		for valDestino in self.__matriz[posOrigen]:
			peso = self.__matriz[posOrigen][valDestino]
			print valDestino, peso
		return True
	
	# Indica si existen arco (o arista) de un nodo origen a un nodo destino
	def existe_arco(self,valOrigen, valDestino):
		posOrigen = self.buscaNodo(valOrigen)
		posDestino = self.buscaNodo(valDestino)
		if (posOrigen >= 0 and posDestino >= 0):
			if (valDestino in self.__matriz[posOrigen]):
				return True
		return False	
	
	# Elimina un nodo del grafo
	def elimina_nodo (self, valOrigen):
		posOrigen = self.buscaNodo(valOrigen)
		del self.__nodos[posOrigen]
		del self.__matriz[posOrigen]
		
		for arcos in self.__matriz:
			if (valOrigen in arcos):
				del arcos[valOrigen]
				
	# Indica si en un grafo hay nodos islas	
	# valida nodo isla con enlace a si mismo
	def existen_islas(self):
		pos = 0
		for arcos in self.__matriz:
			if (len(arcos) == 0):
				valDestino = self.__nodos[pos]
				
				esIsla = True
				posNodo = 0
				for valNodo in self.__nodos:
					if (valDestino in self.__matriz[posNodo]):
						esIsla = False	
					posNodo = posNodo + 1 
				
				if (esIsla == True) or (self.existe_arco(valNodo,valNodo)):
					return True
			
			pos = pos + 1
		return False
	
	# Indica si existe camino desde valOrigen a ValDestino en el grafo  
	def existe_camino(self, valOrigen, valDestino):
		
		posOrigen = self.buscaNodo(valOrigen)
		posDestino = self.buscaNodo(valDestino)
		if (posOrigen < 0 or posDestino < 0):
			return False
			
		# ingresa nodo origen a la lista camino o crea la lista si no existe con nodo inicial
		try:
			self.__camino.append(valOrigen)
		except AttributeError:
			self.__camino = [valOrigen]
		
		# Verifica si existe enlace desde nodo origen a nodo destino
		if (valDestino in self.__matriz[posOrigen]):
			return True
			
		# Recorre los arcos de nodo origen para ver si hay camino a nodo destino	
		for valNodo in self.__matriz[posOrigen]:
			# Verifica si ya paso por ese nodo
			if (valNodo in self.__camino):
				continue
			# busca camino desde nodo del arco hacia nodo destino
			if (self.existe_camino (valNodo, valDestino)):
				return True
			self.__camino.pop()
					
		return False
	
	# Convierte un grafo dirigido a un grafo no-dirigido, colocando en ambos sentidos todos los enlaces
	def no_dirigido(self):
		
		posOrigen = 0
		for valOrigen in self.__nodos:
			for valDestino in self.__matriz[posOrigen]:
				peso = self.__matriz[posOrigen][valDestino]
				self.ins_arco(valDestino, valOrigen, peso)
				
			posOrigen = posOrigen + 1
			
	# Elimina todos los bucles -enlaces a si mismo- del grafo
	def elimina_buqle(self):
		posOrigen = 0
		for valOrigen in self.__nodos:
			for valDestino in self.__matriz[posOrigen]:
				if (valOrigen == valDestino):
					del self.__matriz[posOrigen][valDestino]
					break
				
			posOrigen = posOrigen + 1
		
	
	# Muestra la matriz de adyacencia almacenada del grafo	
	def muestra_estructura_grafo(self):
		print self.__nodos
		print self.__matriz
		
		
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
g.ins_arco("B","A")
g.ins_arco("C","B")
g.ins_arco("C","D")
g.ins_arco("D","E")

g.muestra_estructura_grafo()

print "Nodos"
g.mostrar_nodos()

print "arcos de A"
g.mostrar_arcos("A")

print "Existe arco de A a B", g.existe_arco("A","B")
print "Existe arco de A a E", g.existe_arco("A","E")

print "Existe Camino de A a E", g.existe_camino("A","E")
print "Existe Camino de B a E", g.existe_camino("B","E")

print "Existen Islas", g.existen_islas()
g.elimina_nodo("D")
g.muestra_estructura_grafo()
