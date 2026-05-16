# 🎮 Jogo das Palavras (Termo Super Difícil)

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Um jogo de adivinhação de palavras baseado em texto, desenvolvido em Python. O objetivo é descobrir a palavra oculta antes que suas chances se esgotem, no menor tempo possível. 

O jogo conta com um banco de palavras variado e desafiador, incluindo termos complexos, expressões com espaços e hifens, exigência de acentuação gráfica correta e um sistema integrado de recordes (*ranking*) baseado no tempo de conclusão.

---

## 🚀 Como Jogar (Passo a Passo)

### Pré-requisitos
Antes de começar, certifique-se de ter o **Python 3** instalado em sua máquina.

### Passos para Execução
1. **Baixe o arquivo:** Salve o código fonte em um arquivo chamado `main.py`.
2. **Abra o terminal:** Acesse o Prompt de Comando (Windows) ou o Terminal (Linux/macOS) na pasta onde o arquivo foi salvo.
3. **Execute o comando:** Digite o comando abaixo e pressione `Enter`:

```bash
python main.py

```

---

## 📜 Regras do Jogo

* **O Enigma:** Uma palavra aleatória será sorteada e exibida na tela com os caracteres ocultos por asteriscos (`*`).
* **Caracteres Especiais:** Espaços (` `), hifens (`-`) e sublinhados (`_`) já começam revelados automaticamente.
* **Chances:** Você tem **6 chances** para errar. Chutes corretos não consomem suas chances.
* **Acentuação Importa:** O jogo diferencia letras com acento de letras sem acento.
> **Exemplo:** Se a palavra for `dragão`, digitar apenas `a` não revelará o `ã`. Você deve digitar a letra exatamente com o acento correspondente.


* **Histórico:** O terminal limpa a tela a cada rodada e mostra uma lista em ordem alfabética das letras que você já utilizou.
* **Tempo e Recorde:** O jogo cronometra o tempo levado para descobrir a palavra. Se você vencer e for mais rápido que o recorde anterior, seu novo tempo e a palavra serão salvos no arquivo de ranking.

---

## 🛠️ Estrutura e Explicação do Código

O código foi estruturado de forma procedural, utilizando funções para modularizar o comportamento do sistema e o ecossistema nativo do Python.

### 1. Bibliotecas Utilizadas (Imports)

```python
import time
import subprocess
import random
import os

```

* `time`: Utilizada para capturar o tempo no início e no fim da partida (`time.perf_counter()`), permitindo calcular a duração exata do jogo.
* `subprocess`: Utilizada para executar comandos do sistema operacional (como limpar o terminal) de forma segura.
* `random`: Responsável por selecionar uma palavra aleatória da lista através do método `random.choice()`.
* `os`: Utilizada para detectar o sistema operacional do usuário (`os.name`) e manipular o arquivo de recordes (`os.path`).

### 2. Banco de Palavras (`palavras`)

Uma lista em Python (`list`) contendo strings de diversos tamanhos e dificuldades. Há desde palavras simples até termos extremamente longos (como *pneumoultramicroscopicossilicovulcanoconiótico*), expressões compostas e gírias.

### 3. Função `limpar_tela()`

```python
def limpar_tela():
    if os.name == 'nt':
        subprocess.run('cls', shell=True) # Windows
    else:
        subprocess.run('clear') # Unix/Linux/macOS

```

Esta função verifica se o sistema é Windows (`'nt'`) para rodar o comando `cls`, ou baseado em Unix (Linux/Mac) para rodar o `clear`, mantendo a interface do terminal limpa e organizada a cada jogada.

### 4. Função Principal `jogar()`

Aqui reside a máquina de estados do jogo. Ela inicializa as variáveis de controle da partida:

* `tempoIni`: Captura o exato momento em que o jogo começa.
* `resposta`: A palavra escolhida convertida para minúsculas.
* `tentativas_restantes`: Um contador inteiro definido em 6.
* `letras_adivinhadas`: Um conjunto (`set()`). A escolha por um *set* em vez de uma lista melhora a performance de busca e garante que não haja letras duplicadas no histórico.

#### Mecânicas Internas de `jogar()`

* **Montagem da Palavra Oculta (Pythonic Way):**
```python
palavra_oculta = "".join(
    [letra if letra in letras_adivinhadas or letra in caracteres_especiais else '*' for letra in resposta]
)


```

  Utiliza *List Comprehension* para iterar por cada caractere da resposta. Se a letra já foi adivinhada ou for um caractere especial, ela é mantida; caso contrário, é substituída por `*`.

* **Tratamento de Inputs e Validações:** O código faz três checagens cruciais antes de processar a jogada:
  1. Verifica se o usuário digitou mais de um caractere.
  2. Verifica se o caractere digitado é uma letra (`letra.isalpha()`).
  3. Verifica se a letra já foi jogada anteriormente.

* **Condições de Fim de Jogo:**
  * **Vitória:** Ocorre quando o caractere `*` não está mais presente na string `palavra_oculta`. O tempo final é capturado (`tempoFim`) e a função `ranking()` é chamada.
  * **Derrota:** Ocorre quando o contador `tentativas_restantes` chega a 0. A palavra original é revelada em letras maiúsculas.

### 5. Função de Gerenciamento de Recordes `ranking()`
`ranking(tempoIni, tempoFim, palavraAtual)`

Esta função é responsável por calcular o tempo total e gerenciar o arquivo de salvamento:
1. Calcula a diferença entre o tempo final e inicial para obter o tempo total gasto.
2. Verifica se o arquivo `Ranking.txt` existe e possui conteúdo usando `os.path.exists()` e `os.path.getsize()`.
3. Lê o recorde atual (se houver) e compara com o novo tempo do jogador.
4. Sobrescreve o arquivo gravando o novo tempo e a palavra caso o jogador não tenha um recorde anterior ou tenha superado a marca registrada.

### 6. Loop Principal do Sistema
```python
while True:
    limpar_tela()
    jogar()
    
    jogar_novamente = input("\nDeseja tentar outro enigma? Digite (s) para sim: ").lower()
    if jogar_novamente != 's':
        print("Até a próxima partida!")
        break

```

Um loop infinito (`while True`) garante que, após o término de uma partida (ganhando ou perdendo), o jogador possa escolher se deseja iniciar um novo jogo digitando `s` ou encerrar o programa digitando qualquer outra tecla.

## Autores:
Enzo Costa Gomes - Enzo838
wallyson johnny da Silva Siqueira - wallysonjoh
Felipe da Silva - 
Bruno da Silva Salazar Pardo - brunosalazarse-lgtm
kauan -
Paulo Thomaz Filho - Paulo-Thomaz-Filho



```
