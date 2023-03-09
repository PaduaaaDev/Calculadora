# While infinito para a calculadora sempre funcionar:
while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    operacoes = input('Qual operação deseja usar ? (+, -, /, *, ^ ): ')
# Váriaveis iniciais: 
    conversao_n1 = 0
    conversao_n2 = 0
    numeros_validos = None
    # Exceções para os números recebidos pelo usuário:
    try:
        conversao_n1 = float(n1)
        conversao_n2 = float(n2)
        numeros_validos = True
    except ValueError:
        print(f'Os números digitados são invalidos, por favor, digite apenas números válidos.')
        continue
    # Verificação dos operadores recebidos pelo usuário:
    if operacoes == ('+') or ('-') or ('/') or ('*') or  ('^') :
    # Contas matemáticas:   
        if operacoes == '+':
            soma = conversao_n1 + conversao_n2
            print(f'{conversao_n1} + {conversao_n2} = {soma:.2f}')
        elif operacoes == '-':
            subtracao = conversao_n1 - conversao_n2
            print(f'{conversao_n1} - {conversao_n2} = {subtracao:.2f}')
        elif operacoes == '/':
            divisao = conversao_n1 / conversao_n2
            print(f'{conversao_n1} / {conversao_n2} = {divisao:.2f}')
        elif operacoes == '*':
            multiplicacao = conversao_n1 * conversao_n2
            print(f'{conversao_n1} * {conversao_n2} = {multiplicacao:.2f}')
        elif operacoes == '^':
            elevado = conversao_n1 ** conversao_n2
            print(f'{conversao_n1} ^ {conversao_n2} = {elevado:.2f}')    
        else:
            print('Digite um operador valido.')
            continue
    # Váriavel para sair do Programa:
    sair = input('Deseja sair ? Se sim digite [s]: ').lower().startswith('s')
    # Verificação se a váriavel é True:
    if sair is True:
        print('Obrigado, até a proxima :) ')
        break
