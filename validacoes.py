def validacaoTitulo(titulo):
    """
    Valida um título de eleitor.

    Verifica tamanho, UF e dígitos verificadores
    do título informado.

    Args:
        titulo (str): Número do título de eleitor.

    Returns:
        bool: True se o título for válido,
        False caso contrário.
    """
    titulo2=str(titulo)
    faltando=12-len(titulo2)

    if faltando>0:
        titulo=("0" * faltando)+titulo2
    else:
        if len(titulo2)!=12:
            return False

    inicial=titulo[:8]
    uf=titulo[8:10]
    dvtitulo=int(titulo[10])
    dvtitulo2=int(titulo[11])

    pesos1=[2,3,4,5,6,7,8,9]
    soma=0
    i=0
    while i<8:
        soma+=int(inicial[i])*pesos1[i]
        i+=1

    resto=soma%11

    if uf in("01", "02")and resto==0:
        dvreal=1
    else:
        if resto==10:
            dvreal=0
        else:
            dvreal=resto

    if dvreal!=dvtitulo:
        return False

    soma=int(uf[0])*7+int(uf[1])*8+dvreal*9
    resto=soma%11

    if uf in("01", "02")and resto==0:
        dvreal2=1
    else:
        if resto==10:
            dvreal2=0
        else:
            dvreal2=resto

    if dvreal2!=dvtitulo2:
        return False

    return True

def verificacaoCPF(cpf):
    """
    Valida um CPF.

    Verifica tamanho, repetição de dígitos
    e dígitos verificadores do CPF.

    Args:
        cpf (str): CPF a ser validado.

    Returns:
        bool: True se o CPF for válido,
        False caso contrário.
    """
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0
    digito1 = resto
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0
    digito2 = resto

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

    
