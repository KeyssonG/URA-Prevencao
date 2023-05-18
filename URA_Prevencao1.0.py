
recepcao = 'Olá, prazer em recebe-lo em nosso chat. Estamos aqui para te ajudar. O que você precisa?'
senha = 123456 #senha padrão
CVV_int = ''
erro = 0
nome = ''



nome = input('Como podemos lhe chamar? ')

print(f'Seja bem vindo {nome} ao atendimento digital do Business Bank')

print('-'*60)

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
        print(f'Você errou {erro}x, você possui 2 tentativas!')    
        continue
    break

print('-'*50)

print(recepcao)
