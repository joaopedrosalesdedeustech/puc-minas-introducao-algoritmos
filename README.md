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
| 01 | Listas | [PDF](01_listas/material/Resumo_01_Listas.pdf) | [PDF](01_listas/material/Lista_01_Listas.pdf) | [Código](01_listas/exercicios/) | ✅ 10/10 |
| 02 | Matrizes | [PDF](02_matrizes/material/Resumo_02_Matrizes.pdf) | [PDF](02_matrizes/material/Lista_02_Matrizes.pdf) | — | ⏳ Pendente |
| 03 | Dicionários | [PDF](03_dicionarios/material/Resumo_03_Dicionarios.pdf) | [PDF](03_dicionarios/material/Lista_03_Dicionarios.pdf) | — | ⏳ Pendente |
| 04 | Arquivos | [PDF](04_arquivos/material/Resumo_04_Arquivos.pdf) | [PDF](04_arquivos/material/Lista_04_Arquivos.pdf) | — | ⏳ Pendente |
| 05 | Recursividade | [PDF](05_recursividade/material/Resumo_05_Recursividade.pdf) | [PDF](05_recursividade/material/Lista_05_Recursividade.pdf) | — | ⏳ Pendente |
| 06 | Orientação a Objetos: Introdução | [PDF](06_oo_introducao/material/Resumo_06_OO_Introducao.pdf) | [PDF](06_oo_introducao/material/Lista_06_OO_Introducao.pdf) | — | ⏳ Pendente |
| 07 | Orientação a Objetos: Relacionamento | [PDF](07_oo_relacionamento/material/Resumo_07_OO_Relacionamento.pdf) | [PDF](07_oo_relacionamento/material/Lista_07_OO_Relacionamento.pdf) | — | ⏳ Pendente |
| 08 | Exceções | [PDF](08_excecoes/material/Resumo_08_Excecoes.pdf) | [PDF](08_excecoes/material/Lista_08_Excecoes.pdf) | — | ⏳ Pendente |

---

## Exercícios resolvidos

### Lista 01 — Listas

| Nº | Arquivo | Descrição | Entrada |
|:--:|---------|-----------|:-------:|
| 1 | [`ex01.py`](01_listas/exercicios/ex01.py) | Lê *N* números, exibe-os em ordem inversa e soma os valores das posições pares e ímpares | Usuário |
| 2 | [`ex02.py`](01_listas/exercicios/ex02.py) | Filtra as palavras com mais caracteres do que um tamanho informado | Usuário |
| 3 | [`ex03.py`](01_listas/exercicios/ex03.py) | Verifica se os elementos alternam entre par e ímpar | Fixa |
| 4 | [`ex04.py`](01_listas/exercicios/ex04.py) | Remove valores repetidos, mantendo a ordem da primeira ocorrência | Fixa |
| 5 | [`ex05.py`](01_listas/exercicios/ex05.py) | Encontra o segundo maior valor distinto da lista | Fixa |
| 6 | [`ex06.py`](01_listas/exercicios/ex06.py) | Calcula a maior diferença entre elementos consecutivos | Fixa |
| 7 | [`ex07.py`](01_listas/exercicios/ex07.py) | Lê notas, calcula a média e separa as notas acima e abaixo dela | Usuário |
| 8 | [`ex08.py`](01_listas/exercicios/ex08.py) | Verifica se a lista é espelhada (palíndromo) | Fixa |
| 9 | [`ex09.py`](01_listas/exercicios/ex09.py) | Mescla duas listas ordenadas em uma nova lista ordenada | Fixa |
| 10 | [`ex10.py`](01_listas/exercicios/ex10.py) | Lê nomes e tempos de atletas, calcula a média, lista quem ficou abaixo dela e monta o pódio | Usuário |

> **Entrada:** *Usuário* indica que o programa lê dados pelo teclado; *Fixa* indica que os dados de teste estão definidos no próprio código.

---

## Estrutura do repositório

```
PUC-Minas/
├── 01_listas/
│   ├── material/
│   │   ├── Resumo_01_Listas.pdf
│   │   └── Lista_01_Listas.pdf
│   └── exercicios/
│       ├── ex01.py
│       ├── ...
│       └── ex10.py
├── 02_matrizes/
├── 03_dicionarios/
├── 04_arquivos/
├── 05_recursividade/
├── 06_oo_introducao/
├── 07_oo_relacionamento/
├── 08_excecoes/
├── .gitignore
└── README.md
```

**Convenções adotadas:**

- As pastas de tópico são numeradas (`NN_topico`) na ordem em que os assuntos são vistos na disciplina.
- `material/` guarda o resumo teórico (`Resumo_NN_*.pdf`) e a lista de exercícios (`Lista_NN_*.pdf`) do tópico.
- `exercicios/` guarda as soluções, uma por arquivo, numeradas com dois dígitos (`ex01.py`, `ex02.py`, …) para manter a ordem certa na listagem.

---

## Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado. Nenhuma biblioteca externa é necessária.

```bash
# Clonar o repositório
git clone https://github.com/joaopedrosalesdedeustech/PUC-Minas.git
cd PUC-Minas

# Executar um exercício
python 01_listas/exercicios/ex01.py
```

---

## Autor

**João Pedro Sales de Deus**, estudante da PUC Minas.

[![GitHub](https://img.shields.io/badge/GitHub-joaopedrosalesdedeustech-181717?style=flat-square&logo=github)](https://github.com/joaopedrosalesdedeustech)
