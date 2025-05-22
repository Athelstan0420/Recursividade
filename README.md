# Recursividade

---------------------------------------------

- Conceito de programação onde uma função chama a si mesma;
- Utitlizando casos bases = condição que encerra a recursão;
- A função chama a si mesma com uma valor menor ou maior;
- Mecanismo básico para repetições nas linguagens funcionais;
- Há um ou mais casos bases;
- Há um ou mais casos recursivos;

- Estratégia recursiva:
  
  	- Dividir o problema em problemas menores;
  	- Dividir problemas menores em menores ainda;
  	- Combinar as soluções para formar a solução final;


---------------------------------------------
# Exemplo de fatorial recursivo em python:

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

# Exemplo de soma de valor n até 0 recursivo em python:

	def soma_n_ate_0(n):
			
		if n == 0: # Caso base;
			return 0
		elif n == 1: # Caso base;
			return 1	
		return n + soma_n_ate_0(n-1)
	
	num = int(input("Dig num: "))
	print(soma_n_ate_0(num))

---------------------------------------------
