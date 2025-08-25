assentos = [false] * 10

def reservar():
    pass
    
    numero  = int(input("\nDigite o numero do assento"))
    
    if 0 < numero < 11:
        if assentos [numero - 1] == False:
            assentos [numero - 1] =True
            print (f"Assento: {numero}; reservado\n")
        else:
            print(f"Assento: {numero}. Oculpado\n")
                 
    else:
        print ("\nNumero de assento invalido")

def liberar():

    pass

    pass
    numero  = int(input("\nDigite o numero do assento"))
    
    if 1 <= numero <= 10:
        if assentos [numero - 1] == True:
            assentos [numero - 1] = False
            print (f"Assento: {numero}; reservado\n")
        else:
            print(f"Assento: {numero}. Oculpado\n")
                 
    else:
        print ("\nNumero de assento invalido")

def mostar():
    
    pass

    print("\n\n =MAPA DE OCULPACAO==\n\n")
    for in range (10):
        if assentos[i] == True:
            status = "Oculpado"
        else:
            status = "livre"
        
        print(f"assento: {assentos +1}: {status}")




def main():

    while True:
        print("\n==MENU==")
        print("\n\n1 - Reserva um assento")
        print("2 - Liberar um assento")
        print("3 - mostar mapa de ocupaçao")
        print("4 - Sair")

        opcao= input("\n\nDigite uma opcao de 1 - 4")

        if opcao == "1":
            def reservar()

        elif opcao == "2":
            def liberar()
                
        elif opcao == "3":
            def mostar()
        
        elif opcao == "4":
            print("obrigado")
            break

        else:
            print("opcao nao valida")



#if __name__ == "__main__":


main()