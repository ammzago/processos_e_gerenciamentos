#Estrutura do processo
class Processo:
    def __init__(self, id, duracao):
        self.id = id
        self.tempo_chegada = 0
        self.duracao = duracao
        self.tempo_espera = 0
        self.tempo_resposta = -1
        self.tempo_processamento = 0
        self.tempo_turnaround = 0

#Algoritmo de escalonamento de processo:First-come First-Served
def fcfs(processos):
    tempo_atual = 0
    
    #nesse laço, o processo que vier primeiro é processado, atualizando o tempo de chegada com o atual
    for processo in processos:
        processo.tempo_chegada = tempo_atual
        processo.tempo_espera = tempo_atual
        tempo_atual += processo.duracao
        processo.tempo_turnaround = tempo_atual
        processo.tempo_processamento = tempo_atual
        processo.tempo_resposta = tempo_atual
        
#Algoritmo de escalonamento de processo: Round Robin
def round_robin(processos, quantum):
    #é feita uma copia da lista de processos
    fila = processos.copy()
    tempo_atual = 0
    
    #Nesse laço, enquanto houver processos na fila, ele irá executar
    while fila: 
        #remove o item inicial da lista
        processo = fila.pop(0)
        
        #Verifica se é a primeira vez que o processo é executado, caso for, atualiza o tempo de resposta e chegada
        if processo.tempo_resposta == -1:
            processo.tempo_chegada = tempo_atual
            processo.tempo_resposta = 0
            
        # Verifica se o tempo restante de duração é maior que o quantum, caso for, computa o quantum e retorna
        #o processo ao final da fila, se não, computa o restante do processo
        if processo.duracao - processo.tempo_resposta > quantum:
            tempo_atual += quantum
            processo.tempo_resposta += quantum
            
            fila.append(processo)
        else:
            tempo_atual += (processo.duracao - processo.tempo_resposta)
            processo.tempo_resposta = processo.duracao
            processo.tempo_turnaround = tempo_atual
        
        # atualiza o tempo de espera e a duração final
        processo.tempo_espera = tempo_atual - processo.tempo_chegada - processo.duracao
        processo.tempo_processamento = processo.duracao
               
      
#Algoritmo de escalonamento de processo: Shortest Job First

def sjf(processos):
    fila = processos.copy()
    
    #reordena a lista passando o pico como parâmetro
    fila.sort(key=lambda x: x.duracao)
    
    tempo_atual = 0
    
    #nesse laço, o processo com menor valor de pico é processado, atualizando o tempo de chegada com o atual 
    for processo in fila:
        processo.tempo_chegada = tempo_atual
        processo.tempo_espera = tempo_atual
        tempo_atual += processo.duracao
        processo.tempo_turnaround = tempo_atual
        processo.tempo_processamento = tempo_atual
        processo.tempo_resposta = tempo_atual

def main():
    fcfs_array = []
    round_array = []
    sjf_array = []

    #solicita o numero de processos desejados
    n_de_processos = int(input('Insira o numero de processos: '))

    # para cada numero de procesoss, solicita o pico
    for i in range(n_de_processos):
        pico = int(input(f'Pico do processo {i+1}: '))
        fcfs_array.append(Processo(i+1,pico))
        round_array.append(Processo(i+1,pico))
        sjf_array.append(Processo(i+1,pico))

    #solicita o quantum para o processo RR
    quantum = int(input('insira o quantum: '))

    #Executa o escalonamento para cada processo e retorna os resultados
    fcfs(fcfs_array)
    print("FCFS:")
    for processo in fcfs_array:
        print(f"Processo {processo.id}: Espera = {processo.tempo_espera}, Resposta = {processo.tempo_resposta}, Processamento = {processo.tempo_processamento}, Turnaround = {processo.tempo_turnaround}")

    round_robin(round_array, quantum)
    print("\nRound Robin:")
    for processo in round_array:
        print(f"Processo {processo.id}: Espera = {processo.tempo_espera}, Resposta = {processo.tempo_resposta}, Processamento = {processo.tempo_processamento}, Turnaround = {processo.tempo_turnaround}")

    sjf(sjf_array)
    print("\nSJF:")
    for processo in sjf_array:
        print(f"Processo {processo.id}: Espera = {processo.tempo_espera}, Resposta = {processo.tempo_resposta}, Processamento = {processo.tempo_processamento}, Turnaround = {processo.tempo_turnaround}")



if __name__ == "__main__":
    main()