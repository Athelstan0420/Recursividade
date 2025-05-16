
"""

- O que é RECURSÃO? Função que dentro da própria função você chama ela mesma; (Tipo uma boneca russa)

- Comentários dentro de um comentário;

- Utiliza uma lógica parecida com uma árvore;

- Arquivos utilizados: https://drive.google.com/drive/folders/1fnWf44Wcnq4pOmg7-lRr9ki-IFpbBwdE?usp=drive_link

"""
#

meses_sistema = ['mai2022', 'jan2022', 'set2022', 'dez2022', 'ago2022', 'nov2022', 'jun2022', 'mar2022', 'jul2022', 'abr2022', 'out2022', 'mai2020', 'jun2020', 'jan2020', 'nov2020', 'fev2020', 'abr2020', 'mar2020', 'dez2020', 'out2020', 'set2020', 'jul2020', 'dez2021', 'out2021', 'nov2021', 'ago2021', 'jun2021', 'jan2021', 'set2021', 'fev2021']
# print(len(meses_sistema))

#

import os #Permite entrar em pastas denro do nosso PC;

arquivos_estraidos = [] #Variável global;

def pegar_arq_pasta(pasta):

    lista_arquivos = os.listdir(pasta) # Add arq na var arq_estrai; Essa função lista todos os arquivos de uma pasta;
    
    # Percorre cada arquivo dentro da pasta;
    for arq in lista_arquivos:

        # Se tiver txt e vendas no nome do arq então eu vou pegar o nome do mês; 
        if '.txt' in arq and 'Vendas' in arq:
            nome_mes = (arq.split()[-1].replace('.txt', '')) # Separa o valor que você quer e remove o .txt por um texto vazio;
            arquivos_estraidos.append(nome_mes)

        # Caso contrário: não vou fazer nada;
        # Agora começa a recursão!!!

        elif '.txt' not in arq: # Se é uma pasta;
            pegar_arq_pasta(f"{pasta}/{arq}")

    # print(lista_arquivos)
    pass 
pegar_arq_pasta("/home/adriel/Documentos/Develop/Recursividade/09-22 - Recursão em Python/Arquivos") # Coloca o caminho deste diretório e ele irá listar todos os arq dentro da pasta;


# print(arquivos_estraidos)
# for i in arquivos_estraidos:
#     print(i)

# verifica quais arquivos estão faltando dentro da varial meses_sistema;
for mes in arquivos_estraidos:
    if mes not in meses_sistema:
        print(mes)
