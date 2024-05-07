class Process:
    def __init__(self, id, pico):
        self.id = id
        self.pico = pico
        self.recurso = None

# Função para criar processos e atribuir dependências a eles
def create_processes(num_processos):
    processos = []
    for id in range(num_processos):
        pico = int(input(f"Insira o pico do processo {id}: "))
        processos.append(Process(id, pico))
    
    for processo in processos:
        processo.recurso = encontrar_processo(int(input(f'insira o id da dependência de {processo.id}: ')), processos)
        
    return processos

#função para encontrar um processo a partir do seu ID
def encontrar_processo(chave, processos):
    for processo in processos:
        if processo.id == chave: return processo
        
    return None

# O algoritmo de espera circular verifica se existe uma dependência n1 -> ... -> nx -> n1
# funcionamento: para cada item do processo é verificado se o caminho entre as dependencias faz um looping em algum ponto.
# retorno: lista com a dependencia n1 -> ... -> nx -> n1, caso exista dependencia, ou None, caso não exista dependência

def espera_circular(processos):
    circular = []
    
    for processo in processos:
        if(retorna_dependencia(processo,circular) != None):
            return caminho_circular(circular)
        else: 
            circular = [] 
            
# função recursiva que percorre as dependencias a partir de um processo e verifica se existe um looping entre eles.
#       - a função recebe um processo base através da função espera_circular(), e a partir disso, verifica se possui dependencia de algum 
#       processo já computado

#       - caso possua, ela insere o processo dependente e finaliza a recursão

#       - caso não tenha processo dependente, então ela retorna nulo

#       - caso possua um processo dependente, mas que ainda não foi computado, então ela adiciona o processo na fila circular e realiza a 
#       próxima pesquisa com o seu dependente.
def retorna_dependencia(processo,circular):
    if encontrar_processo(processo.id,circular):
        circular.append(processo)
        return circular
    
    if(processo.recurso == None): 
        return None
    
    else:
        circular.append(processo)
        return retorna_dependencia(processo.recurso,circular)

def caminho_circular(lista_circular):
    while lista_circular[0] != lista_circular[len(lista_circular)-1]:
        del lista_circular[0]
    
    return lista_circular

# Função principal
def main():
    looping = []
    num_processos = int(input("Insira o número de processos: "))
    processos = create_processes(num_processos)
    looping = espera_circular(processos)
    
    print('Espera circular em:', end=' ')
    for item in looping:
        print(item.id, end = ' ')
    

if __name__ == "__main__":
    main()
