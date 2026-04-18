# Termo (Super difícil)
# Imports
import time
import subprocess
import random
import os

# Banco de palavras
palavras = ['eclipse',         'chuva',            'praga',
            'escritorio',      'lapis-lazuli',     'amuleto',
            'sombra',          'guarda-chuva',     'roupa',
            'wasd',            'helicoptero',      'cabelo',
            'dragão',          'sabiá',            'satira',
            'arapuca',         'manifesto',        'bife a role',
            'libélula',        'esqueci',          'bergamota',
            'tonico e tinoco', 'trio parada dura', 'mamonas assasinas',
            'feijão',          'sabão',            'sousafone',
            'saquê',           'soju',             'pneumoultramicroscopicossilicovulcanoconiótico',
            'idiossincrasia',  'agnóstico',        'cornucópia',
            'loquaz',          'parabéns',         'difícil']

def limpar_tela():
    # Garante que a tela limpe tanto no Windows ('cls') quanto no Linux/Mac ('clear')
    if os.name == 'nt':
        subprocess.run('cls', shell=True) # Windows
    else:
        subprocess.run('clear') # Unix/Linux/macOS

def jogar():
    #começa a contar o tempo
    tempoIni = time.perf_counter()
    
    # Sorteia uma palavra e define as regras iniciais
    resposta = random.choice(palavras).lower()
    tentativas_restantes = 6
    letras_adivinhadas = set()
    
    # Caracteres que já começam revelados para o jogador
    caracteres_especiais = {'_', '-', ' '}
    
    print("=== Bem-vindo ao Jogo das palavras ===")
    print("Neste jogo maldito, você deve colocar os acentos, mas não precisa se preocupar com letras maiúsculas.")
    print("Boa sorte para descobri qual é a palavra oculta!\n")
    
    while tentativas_restantes > 0:
        # Modo Pythonico (List Comprehension): Monta a palavra verificando se a letra já foi adivinhada
        palavra_oculta = "".join(
            [letra if letra in letras_adivinhadas or letra in caracteres_especiais else '*' for letra in resposta]
        )
        
        print(f"Palavra: {palavra_oculta}")
        print(f"Chances restantes: {tentativas_restantes}")
        
        # Exibe as letras que o jogador já tentou, em ordem alfabética
        if letras_adivinhadas:
            print(f"Letras usadas: {', '.join(sorted(letras_adivinhadas))}")
        
        # Condição de Vitória: Se não tem mais '*', o jogador acertou tudo
        if '*' not in palavra_oculta:
            print(f"\nVitória! Você conseguiu descobrir a palavra. A palavra era: {resposta.upper()}")
            tempoFim = time.perf_counter()
            ranking(tempoIni, tempoFim, palavra_oculta)
            break
            
        letra = input("\nJogador, digite uma letra: ").lower().strip()
        limpar_tela()
        
        # --- Validações ---
        if len(letra) != 1:
            print("Errado - Digite apenas uma letra.\n")
            continue
            
        if not letra.isalpha():
            print("Errado - Digite apenas letras.\n")
            continue
            
        if letra in letras_adivinhadas:
            print(f"Você já tentou a letra '{letra}'. Tente outra!\n")
            continue
            
        # --- Lógica de Acerto ou Erro ---
        letras_adivinhadas.add(letra)
        
        if letra in resposta:
            print(f"Boa escolha! A letra '{letra}' pertence a palavra oculta.\n")
        else:
            print(f"A letra '{letra}' não pertence a palavra. Você perdeu 1 chance.\n")
            tentativas_restantes -= 1
    
    # Condição de Perca
    if tentativas_restantes == 0:
        print(f"\nSuas chances acabaram. A palavra permane oculta... A palavra era: {resposta.upper()}")
        tempoFim = time.perf_counter()

# Salva o melhor tempo e a palavra, se superar o record anterior
def ranking (tempoIni, tempoFim, palavraAtual):
    file_path = 'Ranking.txt'
    tempo = tempoIni - tempoFim
    tempo = float(abs(tempo))
    tempoRegistrado = 0
    palavra = ""
    
    # Verifica se o aerquivo existe e se tem algo
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        # Pega o conteudo do arquivo
        with open("Ranking.txt", "r", encoding='utf-8') as arquivo:
            conteudo = []
            for linha in arquivo:
                conteudo.append(linha)
            tempoRegistrado = conteudo[0]
            palavra = conteudo[1]
    else:
        # Cria/ sobscreve o arquivo
        with open("Ranking.txt", "w", encoding='utf-8') as arquivo:
            msg = f"{tempo}\n{palavraAtual}"
            arquivo.write(msg)
            print(f"Você conseguiu superar o recorde | O novo recorde e de {tempo:.2f}s com a palavra {palavraAtual} | ELSE")
            return
        
    # Verifica se o tempo foi melhor
    if tempo < float(tempoRegistrado):
        # Cria/ sobscreve o arquivo
        with open("Ranking.txt", "w", encoding='utf-8') as arquivo:
            msg = f"{tempo}\n{palavraAtual}"
            arquivo.write(msg)
        print(f"Você conseguiu superar o recorde | O novo recorde e de {tempo:.2f}s com a palavra {palavraAtual}")
    else:
        print(f"Você não conseguiu superar o recorde de {float(tempoRegistrado):.2f}s")
        
# Loop Principal do Sistema
while True:
    limpar_tela()
    jogar()
    
    # Pergunta se o jogador quer tentar de novo antes de encerrar o script
    jogar_novamente = input("\nDeseja tentar outro enigma? Digite (s) para sim: ").lower()
    if jogar_novamente != 's':
        print("Até a próxima partida!")
        break