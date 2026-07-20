from time import sleep
# Definindo as cores usando códigos ANSI
C_RESET = '\033[0m'
C_VERDE = '\033[32m'
C_AZUL = '\033[34m'
C_AMARELO = '\033[33m'
C_ROXO = '\033[35m'
C_CIANO = '\033[36m'

print(f'{C_AZUL}-={C_RESET}' * 25)
print(f"{C_AMARELO}{'Contador de Treinos'.center(50)}{C_RESET}")
print(f'{C_AZUL}-={C_RESET}' * 25)

res = int(input(f"{C_CIANO}Quantos treinos você quer contar? {C_RESET}"))

for i in range(res):
    print(f'{C_VERDE}Treino {i+1} registrado!{C_RESET}')
    sleep(0.5)

print(f'{C_AZUL}-={C_RESET}' * 25)
print(f"{C_ROXO}{'PARABÉNS! Você registrou todos os treinos!'.center(50)}{C_RESET}")
print(f'{C_AZUL}-={C_RESET}' * 25)


# exemplos e usar cores no terminal
# Reset para voltar ao normal no final de cada print
RESET = '\033[0m'

print("=== CORES NORMAIS (Sem Negrito, Sem Fundo) ===")
print(f"\033[31mTexto em Vermelho normal{RESET}")
print(f"\033[32mTexto em Verde normal{RESET}")
print(f"\033[34mTexto em Azul normal{RESET}")
print()

print("=== CORES EM NEGRITO (Com o número 1) ===")
print(f"\033[1;31mTexto em Vermelho NEGRITO{RESET}")
print(f"\033[1;33mTexto em Amarelo NEGRITO{RESET}")
print(f"\033[1;35mTexto em Roxo NEGRITO{RESET}")
print()

print("=== CORES COM MARCA TEXTO (Fundo - casa dos 40) ===")
print(f"\033[41mFundo Vermelho (Letra normal){RESET}")
print(f"\033[42mFundo Verde (Letra normal){RESET}")
print(f"\033[47mFundo Branco (Letra normal){RESET}")
print()

print("=== COMBINAÇÕES LOUCAS (Letra + Fundo + Negrito) ===")
# 1 (Negrito); 37 (Letra Branca); 41 (Fundo Vermelho)
print(f"\033[1;37;41m ALERTA: Letra Branca, Fundo Vermelho e Negrito {RESET}")

# 1 (Negrito); 33 (Letra Amarela); 44 (Fundo Azul)
print(f"\033[1;33;44m AVISO: Letra Amarela, Fundo Azul e Negrito {RESET}")

# 30 (Letra Preta); 42 (Fundo Verde) - Sem negrito
print(f"\033[30;42m SUCESSO: Letra Preta com Fundo Verde {RESET}")

# 1 (Negrito); 35 (Letra Roxa); 43 (Fundo Amarelo)
print(f"\033[1;35;43m ESTILOSO: Letra Roxa em Negrito no Fundo Amarelo {RESET}")
print()
