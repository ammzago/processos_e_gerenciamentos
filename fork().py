 
import os

# Função que cria processos filhos para calcular somas 
# parciais de subconjuntos de uma lista de números e retorna a soma das somas parciais
def criar_processos_filhos(lista, num_filhos):
    #primeiro é criado um array onde serão armazenados os resultados parciais
    resultados = []
    
    #Então se criam filhos de acordo com a quantidade solicitada pelo usuário
    for filho in range(num_filhos):
     
      #a função fork() é aplicada gerando um processo filho a partir do pai
      pid = os.fork()

      #verifica se o processo filho foi criado para então:
      # 1) converter os valores de intervalo de soma propostos
      # 2) definir a função de soma parcial passando os valores iniciais e finais como parametro
      # 3) declarar na função .exit() a função a qual deverá ser chamada e após concluida, finalizar o filho e retornar o valor
      
      if pid == 0:
        inicio,fim = retornar_intervalo(filho,lista)
        soma_parcial = efetuar_soma(inicio,fim)
        os._exit(soma_parcial)
        
    # para cada filho criado, a função os.wait() é passada como parâmetro para a função WEXITSTATUS() onde seu valor de retorno se
    # dará pelo retorno da função chamada em _exit(). O resultado é armazenado no array "resultados"
    for filho in range(num_filhos):
        pid_filho, status = os.wait()
        soma_parcial = os.WEXITSTATUS(status)
        resultados.append(soma_parcial)
        
    return resultados

# Função para retornar o intervalo de números a serem somados pelo processo filho
def retornar_intervalo(indice, lista):
  inicial =  int(lista[indice][0])
  final = int(lista[indice][1])
  return inicial,final

# Loop para somar os números no intervalo
def efetuar_soma(inicial,final):
  soma = 0
  i = inicial
  
  while i != final+1:
    soma += i
    i+=1
  return soma


if __name__ == "__main__":
    # é solicitado o numero de processos filhos que se deseja criar
    num_filhos = int(input("Digite o número de processos filhos desejado: "))
    
    lista = []

    # Loop para solicitar e armazenar os intervalos de soma fornecidos pelo usuário
    for filho in range(num_filhos):
      lista.append(input(f'Insira o intervalo de soma do filho {filho+1} (ex: 1,2): ').split(','))

    # os valores obtidos são submetidos a função que criará os processos filhos e executará as somas, retornando
    # uma lista com os resultados parciais
    resultados = criar_processos_filhos(lista, num_filhos)
    
    # Os valores parciais são somados e o resultado final é impresso no terminal
    soma_total = sum(resultados)
    print("A soma total é:", soma_total)
    
    
# OBS: em ambiente Windows a função fork() não é suportada, devendo-se executar em um ambiente virtual MAC ou Linux, ou baixar / executar
# pelo terminal Cygwin64


