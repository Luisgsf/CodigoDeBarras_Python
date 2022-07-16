import os

continuar = True;
soma = 0;

os.system('cls');

while(continuar):
    print("-------------------------------");
    print("         VAREJOS S/A           ");
    print("   Código GTIN-13/UPC/EAN-13   ");
    print("-------------------------------");
    print("1)Validar código GTIN-13       ");
    print("2)Identificar País             ");
    print("3)Sair                         ");
    print("-------------------------------");
    
    op = int(input('Digite a opção: '));
    os.system('cls');

    print("-------------------------------");
    print("         VAREJOS S/A           ");
    print("   Código GTIN-13/UPC/EAN-13   ");
    print("-------------------------------");
    
# Código da opção 1
    if(op == 1):
        print("VALIDAR CÓDIGO");
        codigo13 = str(input('Digite o código de 13 digitos: '));
        
        if(len(codigo13) != 13):
            print("Número GTIN-13 não possui 13 digitos!");
            input("Pressione ENTER para continuar...");
            os.system('cls');

        else:
            codigo13 = int(codigo13);

            # Repetição para multiplicar os números por 3(três)
            for dig in range(codigo13[1], codigo13[11], 2):
                soma += (codigo13[dig] * 3);

            # Repetição para multiplicar os números por 1(um)
            for dig in range(codigo13[0], codigo13[10], 2):
                soma += (codigo13[dig] * 1);

            divisao = soma // 10;
            divisao += 1; #divisao = divisao + 1
            divisao *= 10; #divisao = divisao * 10
            digVerificador = divisao - soma;

            if(digVerificador % 10 == 0):
                digVerificador = 0;

            print("DIGITO VERIFICADOR: ", digVerificador);
            print("NÚMERO GTIN-13 VÁLIDO!");
            print("-----------------------------");
            input("Pressione ENTER para continuar...");
            os.system('cls');

# Código da opção 2
    elif(op == 2):
        print("IDENTIFICAR PAÍS");
        codigo13 = input('Digite o código de 13 digitos: ');
        codPais = codigo13[:3];

        if(codPais == 789 or codPais == 790):
            pais = "Brasil";

        elif(codPais == 779):
            pais = "Argentina";

        elif(codPais == 773):
            pais = "Uruguai";

        elif(codPais == 780):
            pais = "Chile";

        elif(codPais == 784):
            pais = "Paraguai";
        
        elif(codPais == 786):
            pais = "Equador";
        
        elif(codPais == 770):
            pais = "Colômbia";
        
        elif(codPais == 743):
            pais = "Nicarágua";
        
        elif(codPais == 600 or 601):
            pais = "África do Sul";

        else:
            print("VAREJOS S/A não vende para este país: ", codPais);
            input("Pressione ENTER para continuar...");
        
        print("GTIN-13 origem %s: %s" %(pais, codPais));
        input("Pressione ENTER para continuar...");
    
# Código da opção 3
    elif(op == 3):
        continuar = False;
        print("PROGRAMA ENCERRADO!");

    else:
        print("OPÇÃO INVÁLIDA!");
        input("Pressione ENTER para continuar...");
        os.system('cls');