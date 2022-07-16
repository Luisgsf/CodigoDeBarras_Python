continuar = True;
soma = 0;

while(continuar):
    print("-----------------------------");
    print("        VAREJOS S/A          ");
    print("   Código GTIN-13/UPC/EAN-13 ");
    print("-----------------------------");
    print("1)Validar código GTIN-13     ");
    print("2)Identificar País           ");
    print("3)Sair                       ");
    print("-----------------------------");
    
    op = int(input('Digite a opção: '));
    print("-----------------------------");
    print("        VAREJOS S/A          ");
    print("   Código GTIN-13/UPC/EAN-13 ");
    print("-----------------------------");
    
    if(op == 1):
        print("VALIDAR CÓDIGO");
        codigo13 = input('Digite o código de 13 digitos: ');
        if(codigo13.__len__ != 13):
            print("Número GTIN-13 não possui 13 digitos!");
        else:
            for dig in range(codigo13[11], codigo13[1], -2):                
                soma += (codigo13[dig] * 3);
            for dig in range(codigo13[10], codigo13[0], -2):
                soma += (codigo13[dig] * 1);
            resto = soma % 10;
            resto += 1;
            resto *= 10;
            digVerificador = resto - soma;
            if(digVerificador % 10 == 0):
                digVerificador = 0;
            
            print("-----------------------------");