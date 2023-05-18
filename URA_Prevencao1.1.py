recepcao = 'Olá, prazer em recebe-lo em nosso chat. Estamos aqui para te ajudar. O que você precisa?'
senha = 123456 #senha padrão
CVV_int = ''
erro = 0
nome = ''
#cnpj ficticio 68361350000117



while True:
    identificacao = input('Olá, seja bem vindo ao atendimento eletronico do Business Bank'
                             '\nPara iniciarmos, digite o seu CPF ou CNPJ sem caracteres especiais:')
    nome = input('Como podemos lhe chamar: ')
    if len(identificacao) == 11:
        print(f'Olá {nome}')   
    elif len(identificacao) == 14:
        print(f'Olá empreendedor {nome}')
    else:
        print('Não conseguimos lhe identificar, tenta novamente digitando apenas números sem carecteres especiais.')    
        continue
    break

print('-'*50)          

while True:
    
    senha = input('Digite a sua senha: ')
    CVV = input('Digite o CVV do seu cartão: ')

    senha_int = int(senha)
    CVV_int = int(CVV)

    if senha_int == 123456 and CVV_int == CVV_int:
        print('Login efetuado com sucesso!')
    else:
        print('Erro ao efetuar o login, tente novamente!')
        erro = erro + 1
        print(f'Você errou {erro}x')    
        continue
    break

print('-'*50)

print(recepcao)