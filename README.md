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
| 01 | Listas | [PDF](01_listas/material/resumo_listas.pdf) | [PDF](01_listas/material/enunciados_listas.pdf) | [Código](01_listas/exercicios/) | ✅ 10/10 |
| 02 | Matrizes | [PDF](02_matrizes/material/resumo_matrizes.pdf) | [PDF](02_matrizes/material/enunciados_matrizes.pdf) | [Pasta](02_matrizes/exercicios/) | ⏳ Pendente |
| 03 | Dicionários | [PDF](03_dicionarios/material/resumo_dicionarios.pdf) | [PDF](03_dicionarios/material/enunciados_dicionarios.pdf) | [Pasta](03_dicionarios/exercicios/) | ⏳ Pendente |
| 04 | Arquivos | [PDF](04_arquivos/material/resumo_arquivos.pdf) | [PDF](04_arquivos/material/enunciados_arquivos.pdf) | [Pasta](04_arquivos/exercicios/) | ⏳ Pendente |
| 05 | Recursividade | [PDF](05_recursividade/material/resumo_recursividade.pdf) | [PDF](05_recursividade/material/enunciados_recursividade.pdf) | [Pasta](05_recursividade/exercicios/) | ⏳ Pendente |
| 06 | Orientação a Objetos: Introdução | [PDF](06_oo_introducao/material/resumo_oo_introducao.pdf) | [PDF](06_oo_introducao/material/enunciados_oo_introducao.pdf) | [Pasta](06_oo_introducao/exercicios/) | ⏳ Pendente |
| 07 | Orientação a Objetos: Relacionamento | [PDF](07_oo_relacionamento/material/resumo_oo_relacionamento.pdf) | [PDF](07_oo_relacionamento/material/enunciados_oo_relacionamento.pdf) | [Pasta](07_oo_relacionamento/exercicios/) | ⏳ Pendente |
| 08 | Exceções | [PDF](08_excecoes/material/resumo_excecoes.pdf) | [PDF](08_excecoes/material/enunciados_excecoes.pdf) | [Pasta](08_excecoes/exercicios/) | ⏳ Pendente |

---

## Exercícios resolvidos

### Lista 01 — Listas

| Nº | Arquivo | Descrição | Entrada |
|:--:|---------|-----------|:-------:|
| 1 | [`ex01_ordem_inversa.py`](01_listas/exercicios/ex01_ordem_inversa.py) | Lê *N* números, exibe-os em ordem inversa e soma os valores das posições pares e ímpares | Usuário |
| 2 | [`ex02_filtrar_palavras.py`](01_listas/exercicios/ex02_filtrar_palavras.py) | Filtra as palavras com mais caracteres do que um tamanho informado | Usuário |
| 3 | [`ex03_alterna_paridade.py`](01_listas/exercicios/ex03_alterna_paridade.py) | Verifica se os elementos alternam entre par e ímpar | Fixa |
| 4 | [`ex04_sem_repeticao.py`](01_listas/exercicios/ex04_sem_repeticao.py) | Remove valores repetidos, mantendo a ordem da primeira ocorrência | Fixa |
| 5 | [`ex05_segundo_maior.py`](01_listas/exercicios/ex05_segundo_maior.py) | Encontra o segundo maior valor distinto da lista | Fixa |
| 6 | [`ex06_maior_diferenca.py`](01_listas/exercicios/ex06_maior_diferenca.py) | Calcula a maior diferença entre elementos consecutivos | Fixa |
| 7 | [`ex07_media_notas.py`](01_listas/exercicios/ex07_media_notas.py) | Lê notas, calcula a média e separa as notas acima e abaixo dela | Usuário |
| 8 | [`ex08_eh_espelhada.py`](01_listas/exercicios/ex08_eh_espelhada.py) | Verifica se a lista é espelhada (palíndromo) | Fixa |
| 9 | [`ex09_mesclar.py`](01_listas/exercicios/ex09_mesclar.py) | Mescla duas listas ordenadas em uma nova lista ordenada | Fixa |
| 10 | [`ex10_desempenho_corrida.py`](01_listas/exercicios/ex10_desempenho_corrida.py) | Lê nomes e tempos de atletas, calcula a média, lista quem ficou abaixo dela e monta o pódio | Usuário |

> **Entrada:** *Usuário* indica que o programa lê dados pelo teclado; *Fixa* indica que os dados de teste estão definidos no próprio código.

---

## Estrutura do repositório

```
PUC-Minas/
├── 01_listas/
│   ├── material/
│   │   ├── resumo_listas.pdf
│   │   └── enunciados_listas.pdf
│   └── exercicios/
│       ├── ex01_ordem_inversa.py
│       ├── ex02_filtrar_palavras.py
│       ├── ex03_alterna_paridade.py
│       ├── ex04_sem_repeticao.py
│       ├── ex05_segundo_maior.py
│       ├── ex06_maior_diferenca.py
│       ├── ex07_media_notas.py
│       ├── ex08_eh_espelhada.py
│       ├── ex09_mesclar.py
│       └── ex10_desempenho_corrida.py
├── 02_matrizes/
│   ├── material/
│   │   ├── resumo_matrizes.pdf
│   │   └── enunciados_matrizes.pdf
│   └── exercicios/
│       └── .gitkeep
├── 03_dicionarios/
│   ├── material/
│   │   ├── resumo_dicionarios.pdf
│   │   └── enunciados_dicionarios.pdf
│   └── exercicios/
│       └── .gitkeep
├── 04_arquivos/
│   ├── material/
│   │   ├── resumo_arquivos.pdf
│   │   └── enunciados_arquivos.pdf
│   └── exercicios/
│       └── .gitkeep
├── 05_recursividade/
│   ├── material/
│   │   ├── resumo_recursividade.pdf
│   │   └── enunciados_recursividade.pdf
│   └── exercicios/
│       └── .gitkeep
├── 06_oo_introducao/
│   ├── material/
│   │   ├── resumo_oo_introducao.pdf
│   │   └── enunciados_oo_introducao.pdf
│   └── exercicios/
│       └── .gitkeep
├── 07_oo_relacionamento/
│   ├── material/
│   │   ├── resumo_oo_relacionamento.pdf
│   │   └── enunciados_oo_relacionamento.pdf
│   └── exercicios/
│       └── .gitkeep
├── 08_excecoes/
│   ├── material/
│   │   ├── resumo_excecoes.pdf
│   │   └── enunciados_excecoes.pdf
│   └── exercicios/
│       └── .gitkeep
├── .gitignore
└── README.md
```

**Convenções adotadas:**

- As pastas de tópico são numeradas (`NN_topico`) na ordem em que os assuntos são vistos na disciplina.
- Todos os nomes de pastas e arquivos usam letras minúsculas, `snake_case` e nenhum acento ou espaço.
- `material/` guarda o resumo teórico (`resumo_<topico>.pdf`) e a lista de exercícios (`enunciados_<topico>.pdf`) do tópico.
- `exercicios/` guarda as soluções, uma por arquivo, no formato `exNN_<descricao>.py`. O número com dois dígitos mantém a ordem certa na listagem, e a descrição usa o nome da função pedida no enunciado, quando houver (por exemplo, `ex09_mesclar.py`).
- Pastas de exercícios ainda vazias contêm um arquivo `.gitkeep`, necessário para que o Git as mantenha no repositório.

---

## Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado. Nenhuma biblioteca externa é necessária.

```bash
# Clonar o repositório
git clone https://github.com/joaopedrosalesdedeustech/PUC-Minas.git
cd PUC-Minas

# Executar um exercício
python 01_listas/exercicios/ex01_ordem_inversa.py
```

---

## Autor

**João Pedro Sales de Deus**, estudante da PUC Minas.

[![GitHub](https://img.shields.io/badge/GitHub-joaopedrosalesdedeustech-181717?style=flat-square&logo=github)](https://github.com/joaopedrosalesdedeustech)
