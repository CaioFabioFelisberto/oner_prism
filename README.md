# OneR e PRISM

Implementação didática de algoritmos de classificação baseados em regras para o conjunto de dados **Play Tennis**. O projeto treina e exibe regras geradas pelos algoritmos OneR e PRISM e inclui uma comparação adicional com uma árvore de decisão.

## Requisitos

- Python 3.10 ou superior
- `pip`

As dependências estão listadas em [`requirements.txt`](requirements.txt).

## Instalação

No Windows PowerShell, a partir da raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Caso a política de execução do PowerShell impeça a ativação do ambiente virtual, execute o Python diretamente:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Execução

Execute o programa principal na raiz do projeto:

```powershell
python main.py
```

Ou, usando o interpretador do ambiente virtual:

```powershell
.\.venv\Scripts\python.exe main.py
```

O programa lê [`data/play_tennis.csv`](data/play_tennis.csv), usa `Jogar` como variável-alvo e imprime:

- a melhor característica e o relatório de erros do modelo OneR;
- a quantidade de regras geradas pelo PRISM.

Para executar a comparação com uma árvore de decisão:

```powershell
python src/comparison.py
```

Esse script imprime a estrutura da árvore no terminal e gera o arquivo `decision_tree.png` na raiz do projeto.

## Estrutura do projeto

```text
.
├── data/
│   └── play_tennis.csv       # Dados de treinamento
├── outputs/                  # Diretório reservado para resultados
├── src/
│   ├── comparison.py         # Árvore de decisão e visualização
│   ├── oner.py               # Implementação do OneR
│   └── prism.py              # Implementação do PRISM
├── main.py                   # Ponto de entrada principal
├── requirements.txt          # Dependências Python
└── .gitignore
```

## Dados

O dataset contém atributos categóricos sobre condições climáticas:

- `Aparencia`
- `Temperatura`
- `Umidade`
- `Vento`

O alvo `Jogar` indica se é recomendado jogar tênis (`Sim` ou `Nao`).

## Observações

Os scripts usam caminhos relativos, como `data/play_tennis.csv`. Por isso, execute-os a partir da raiz do projeto. O diretório `.venv/` é ignorado pelo Git.