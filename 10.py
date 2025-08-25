def adcionar(tarefa):
    x = input("\nadcionar tarefa: \n")
    
    if x != "":

        tarefa.append (x)
        print ("\ntarefa adcionada")
    else:
        print("\ntarefa vazia")
    
def listar(tarefa):
    if len(tarefa) == 0:
        print ("\n\nnenhuma tarefa listada")
        return
        
    print ("\n==TAREFAS==")

    print (tarefa)

def remover(tarefa):
    x = input ("\ntarefa a ser deletada: ")
    
    if x in tarefa:
        tarefa.remove(x)
        print (f"\ntarefa: {x}, removida")

    elif x =="":
        print("\nNenhuma tarefa digitada.")

    else:
        print ("tarefa nao existente")

    



def main():
    tarefa = []
    
    while True:
        print ("\n\n==menu==")
        print ("\n 1 - Adcionar tarefa")
        print ("\n 2 - Lista tarefa")
        print ("\n 3 - Remover tarefa")
        print ("\n 4 - Sair da tarefa")
        
        opcao = input ("\nEscolha a opcao: ")
        
        
        if opcao == "1":
            adcionar(tarefa)
        
        elif opcao =="2":
            listar(tarefa)
        
        elif opcao =="3":
            remover(tarefa)
        
        elif opcao =="4":
            print ("obrigado")
            break
    
            
        else:
            print ("Escolha opcao valida")



#if __name__ == "__main__:
main ()