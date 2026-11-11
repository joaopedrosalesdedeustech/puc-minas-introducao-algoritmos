<div align="center">

# Introdução a Algoritmos — PUC Minas

Resumos teóricos, listas de exercícios e soluções em Python da disciplina de **Introdução a Algoritmos**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20andamento-yellow?style=flat-square)
![Progresso](https://img.shields.io/badge/listas%20concluídas-1%20de%208-blue?style=flat-square)
![Instituição](https://img.shields.io/badge/PUC-Minas-003366?style=flat-square)

</div>

---

## Sumário

- [Sobre](#sobre)
- [Conteúdo da disciplina](#conteúdo-da-disciplina)
- [Exercícios resolvidos](#exercícios-resolvidos)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Como executar](#como-executar)
- [Autor](#autor)

---

## Sobre

Este repositório reúne o material de estudo da disciplina de **Introdução a Algoritmos** da **PUC Minas**. Cada tópico tem um resumo teórico, uma lista de exercícios e, conforme o andamento do curso, as minhas soluções em Python.

As soluções seguem as restrições propostas nas listas. Por exemplo, várias questões proíbem funções prontas como `sorted()`, `sort()` e `min()`, para praticar a lógica dos algoritmos.

---

## Conteúdo da disciplina

| # | Tópico | Resumo | Lista | Soluções | Status |
|:-:|--------|:------:|:-----:|:--------:|:------:|
| 01 | Listas | [PDF](lista/Resumo_01_Listas.pdf) | [PDF](lista/Lista_01_Listas.pdf) | [Código](lista/exercicios/) | ✅ 10/10 |
| 02 | Matrizes | [PDF](matrizes/Resumo_02_Matrizes.pdf) | [PDF](matrizes/Lista_02_Matrizes.pdf) | — | ⏳ Pendente |
| 03 | Dicionários | [PDF](dicionario/Resumo_03_Dicionarios.pdf) | [PDF](dicionario/Lista_03_Dicionarios.pdf) | — | ⏳ Pendente |
| 04 | Arquivos | [PDF](arquivos/Resumo_04_Arquivos.pdf) | [PDF](arquivos/Lista_04_Arquivos.pdf) | — | ⏳ Pendente |
| 05 | Recursividade | [PDF](recursao/Resumo_05_Recursividade.pdf) | [PDF](recursao/Lista_05_Recursividade.pdf) | — | ⏳ Pendente |
| 06 | Orientação a Objetos: Introdução | [PDF](orientacao_a_objetos/Resumo_06_OO_Introducao.pdf) | [PDF](orientacao_a_objetos/Lista_06_OO_Introducao.pdf) | — | ⏳ Pendente |
| 07 | Orientação a Objetos: Relacionamento | [PDF](orientacao_a_objetos/Resumo_07_OO_Relacionamento.pdf) | [PDF](orientacao_a_objetos/Lista_07_OO_Relacionamento.pdf) | — | ⏳ Pendente |
| 08 | Exceções | [PDF](excecoes/Resumo_08_Excecoes.pdf) | [PDF](excecoes/Lista_08_Excecoes.pdf) | — | ⏳ Pendente |

---

## Exercícios resolvidos

### Lista 01 — Listas

| Nº | Arquivo | Descrição | Entrada |
|:--:|---------|-----------|:-------:|
| 1 | [`ex1.py`](lista/exercicios/ex1.py) | Lê *N* números, exibe-os em ordem inversa e soma os valores das posições pares e ímpares | Usuário |
| 2 | [`ex2.py`](lista/exercicios/ex2.py) | Filtra as palavras com mais caracteres do que um tamanho informado | Usuário |
| 3 | [`ex3.py`](lista/exercicios/ex3.py) | Verifica se os elementos alternam entre par e ímpar | Fixa |
| 4 | [`ex4.py`](lista/exercicios/ex4.py) | Remove valores repetidos, mantendo a ordem da primeira ocorrência | Fixa |
| 5 | [`ex5.py`](lista/exercicios/ex5.py) | Encontra o segundo maior valor distinto da lista | Fixa |
| 6 | [`ex6.py`](lista/exercicios/ex6.py) | Calcula a maior diferença entre elementos consecutivos | Fixa |
| 7 | [`ex7.py`](lista/exercicios/ex7.py) | Lê notas, calcula a média e separa as notas acima e abaixo dela | Usuário |
| 8 | [`ex8.py`](lista/exercicios/ex8.py) | Verifica se a lista é espelhada (palíndromo) | Fixa |
| 9 | [`ex9.py`](lista/exercicios/ex9.py) | Mescla duas listas ordenadas em uma nova lista ordenada | Fixa |
| 10 | [`ex10.py`](lista/exercicios/ex10.py) | Lê nomes e tempos de atletas, calcula a média, lista quem ficou abaixo dela e monta o pódio | Usuário |

> **Entrada:** *Usuário* indica que o programa lê dados pelo teclado; *Fixa* indica que os dados de teste estão definidos no próprio código.

---

## Estrutura do repositório

```
PUC-Minas/
├── lista/                    # 01 — Listas
│   ├── Resumo_01_Listas.pdf
│   ├── Lista_01_Listas.pdf
│   └── exercicios/           # ex1.py … ex10.py
├── matrizes/                 # 02 — Matrizes
├── dicionario/               # 03 — Dicionários
├── arquivos/                 # 04 — Arquivos
├── recursao/                 # 05 — Recursividade
├── orientacao_a_objetos/     # 06 e 07 — Orientação a Objetos
├── excecoes/                 # 08 — Exceções
└── README.md
```

Cada pasta de tópico contém o resumo (`Resumo_XX_*.pdf`) e a lista (`Lista_XX_*.pdf`). As soluções ficam na subpasta `exercicios/`.

---

## Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado. Nenhuma biblioteca externa é necessária.

```bash
# Clonar o repositório
git clone https://github.com/joaopedrosalesdedeustech/PUC-Minas.git
cd PUC-Minas

# Executar um exercício
python lista/exercicios/ex1.py
```

---

## Autor

**João Pedro Sales de Deus**, estudante da PUC Minas.

[![GitHub](https://img.shields.io/badge/GitHub-joaopedrosalesdedeustech-181717?style=flat-square&logo=github)](https://github.com/joaopedrosalesdedeustech)
