# Recursividade

---------------------------------------------

#Exemplo de fatorial recursivo em python:

	def fatorial(n):
			
		if n == 0: # Caso base;
			return 0
		elif n == 1: # Caso base;
			return 1	
		return n * fatorial(n-1)
	
	num = int(input("Dig num: "))
	print(fatorial(num))

---------------------------------------------

---------------------------------------------

#Exemplo de soma de valor n até 0, recursivo em python:

	def fatorial(n):
			
		if n == 0: # Caso base;
			return 0
		elif n == 1: # Caso base;
			return 1	
		return n + fatorial(n-1)
	
	num = int(input("Dig num: "))
	print(fatorial(num))

---------------------------------------------
