tupla = []




def adcionar_nota(tupla):
    aluno = input("\nNome do aluno: ")
    nota = float(input("\nNota do aluno(0-10): "))
    disciplina = input("\nDisciplina do aluno: ")

    if 0 < nota <=10 and aluno !="" and disciplina !="":
        inf = {
            "aluno":aluno,
            "nota": nota,
            "disciplina": disciplina,

        }

        
    
    else:
        print("Digite valores dentro dos paramentros")

    tupla.append(inf)

def listar_melhor_aluno(tupla):
    pass

def listar_aluno(tupla):
    print(tupla)

def listar_notas(tupla):
    pass



def main():

    while True:
        print ("\n\n==MENU==")
        print ("\n 1 - Adcionar aluno e nota")
        print ("\n 2 - Listar melhor aluno")
        print ("\n 3 - Listar nota por aluno")
        print ("\n 3 - Listar notas por ordem  decrescente")
        print ("\n 5 - Sair")
        
        escolha = input("\n Escolha uma opcao: ")
        
        if escolha == "1":
            adcionar_nota(tupla)
            
        elif escolha == "2":
            listar_melhor_aluno(tupla)
            
        elif escolha == "3":
            listar_aluno(tupla)
        
        elif escolha == "4":
            listar_notas(tupla)

        elif escolha == "5":
            print ("obrigado")
            break
        
        else:
            print ("\n escolha opcao valida!")
            



if __name__ == "__main__":
    main()