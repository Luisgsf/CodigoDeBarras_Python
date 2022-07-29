def InformarPais(cod):
    pais_loc = "";

    if(cod == "789" or cod == "790"):
        pais_loc = "Brasil";        

    elif(cod == "779"):
        pais_loc = "Argentina";
        
    elif(cod == "773"):
        pais_loc = "Uruguai";
        
    elif(cod == "780"):
        pais_loc = "Chile";       

    elif(cod == "784"):
        pais_loc = "Paraguai";
                
    elif(cod == "786"):
        pais_loc = "Equador";
        
    elif(cod == "770"):
        pais_loc = "Colômbia";
        
    elif(cod == "743"):
        pais_loc = "Nicarágua";
        
    elif(cod == "600" or cod == "601"):
        pais_loc = "África do Sul";
        
    else:
        pais_loc = "VAREJOS S/A não vende para este país: ";        
            
    return pais_loc;

def Titulo():
    print("-------------------------------");
    print("         VAREJOS S/A           ");
    print("   Código GTIN-13/UPC/EAN-13   ");
    print("-------------------------------");

import os
continuar = True;

os.system('cls');

while(continuar):
    soma = 0;
    aux1 = 0;
    aux2 = 0;

    Titulo();
    print("1)Validar código GTIN-13       ");
    print("2)Identificar País             ");
    print("3)Sair                         ");
    print("-------------------------------");
    
    op = int(input("Digite a opção: "));
    os.system('cls');

    Titulo();
    
# Código da opção 1
    if(op == 1):
        print("VALIDAR CÓDIGO");
        codigo13 = str(input("Digite o código de 13 digitos: "));
        
        if(len(codigo13) != 13):
            print("Número GTIN-13 não possui 13 digitos!");
            input("Pressione ENTER para continuar...");
            os.system('cls');
        
        else:
            for i in range(0, 12, 2):
                aux1 += (int(codigo13[i]) * 1);
                aux2 += (int(codigo13[i+1]) * 3);
                
            soma += aux1 + aux2;
            print(soma);
            divisao = soma // 10;
            print(divisao);
            divisao += 1;
            print(divisao);
            divisao *= 10;
            print(divisao);
            digVerificador = divisao - soma;

            if(digVerificador % 10 == 0):
                digVerificador = 0;
            
            print("DIGITO VERIFICADOR: ", digVerificador);

            if(digVerificador == int(codigo13[12])):
                print("NÚMERO GTIN-13 VÁLIDO!");
            else:
                print("NÚMERO GTIN-13 INVÁLIDO!");

            print("-----------------------------");
            input("Pressione ENTER para continuar...");
            os.system('cls');

# Código da opção 2
    elif(op == 2):
        print("IDENTIFICAR PAÍS");
        codigo13 = input("Digite o código de 13 digitos: ");
        
        if(len(codigo13) != 13):
            print("Número GTIN-13 não possui 13 digitos!");
            input("Pressione ENTER para continuar...");
            os.system('cls');

        else:
            codPais = codigo13[:3];
            pais = InformarPais(codPais);

            if "VAREJOS S/A não" not in pais:
                print("GTIN-13 origem %s: %s" %(pais, codPais));
                input("Pressione ENTER para continuar...");
            else:
                print(pais, codPais);
                input("Pressione ENTER para continuar...");
            os.system('cls')
    
# Código da opção 3
    elif(op == 3):
        continuar = False;
        print("PROGRAMA ENCERRADO!");

    else:
        print("OPÇÃO INVÁLIDA!");
        input("Pressione ENTER para continuar...");
        os.system('cls');