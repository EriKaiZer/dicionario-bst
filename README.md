# Dicionário Técnico com Árvore Binária de Busca

**Aluno:** Erik Kaiser  
**Linguagem:** Python  
**Atividade:** Estruturas de Dados

## Objetivo

Criar um glossário de termos técnicos usando uma Árvore Binária de Busca (BST). O programa permite cadastrar uma palavra, buscar sua definição e listar os termos em ordem alfabética.

## Como executar

1. Tenha o Python 3 instalado.
2. Extraia o ZIP e abra a pasta `dicionario-bst`.
3. Abra o terminal nessa pasta e execute:

```bash
python main.py
```

No Windows, também pode usar `py main.py`. No Linux ou macOS, pode usar `python3 main.py`.

Não precisa instalar nenhuma biblioteca.

## Menu

| Opção | O que faz |
| --- | --- |
| 1 | Cadastra um termo ou atualiza sua definição |
| 2 | Busca a definição de um termo |
| 3 | Lista os termos em ordem alfabética |
| 4 | Encerra o programa |

O programa também aceita `0` para sair, como no código inicial do PDF.

## Exemplo para testar

Use a opção 1 para cadastrar estes termos, nesta ordem:

| Palavra | Definição |
| --- | --- |
| Python | Linguagem de programação. |
| Algoritmo | Sequência de passos para resolver um problema. |
| Variável | Nome usado para guardar um valor no programa. |
| Banco de dados | Conjunto organizado de dados. |

Depois, use a opção 3. A saída será:

```text
algoritmo: Sequência de passos para resolver um problema.
banco de dados: Conjunto organizado de dados.
python: Linguagem de programação.
variável: Nome usado para guardar um valor no programa.
```

Para buscar, escolha a opção 2 e digite `Python`. Para atualizar, cadastre `Python` de novo com outra definição. Para testar uma busca sem resultado, procure `Java`, que não foi cadastrado nesse exemplo.

## Respostas sobre os requisitos da atividade

O PDF apresenta requisitos de implementação, sem uma lista separada de perguntas. Abaixo estão as explicações de como cada parte foi resolvida.

### 1. O que fica guardado em cada nó?

A classe `NoTermo` guarda a palavra, a definição e dois filhos: esquerda e direita. Quando não existe filho, o valor é `None`.

### 2. Como funciona a inserção?

O primeiro termo vira a raiz. Os próximos são comparados com a palavra do nó atual. Se a palavra for menor, o programa segue para a esquerda. Se for maior, segue para a direita. Quando encontra um espaço vazio, coloca o novo nó ali.

### 3. O que acontece se a palavra já existir?

O programa atualiza a definição do termo existente. Não cria outro nó para a mesma palavra.

### 4. Como funciona a busca?

A busca começa na raiz. Se encontrar a palavra, retorna sua definição. Se a palavra for menor, segue para a esquerda. Se for maior, segue para a direita. Se chegar em `None`, retorna "Termo não encontrado."

### 5. Como a listagem fica em ordem alfabética?

Ela usa o caminhamento Em-Ordem: visita a esquerda, mostra o nó atual e visita a direita. Como as palavras menores estão à esquerda e as maiores à direita, os termos aparecem ordenados.

### 6. Como funciona o menu?

Um `while True` repete o menu. O usuário escolhe uma opção e o programa executa a função correspondente. Ao escolher sair, o `break` encerra o laço.

### 7. Por que usar uma árvore em vez de uma lista?

Na árvore, a comparação indica para qual lado continuar. Isso pode evitar olhar todos os termos. Em uma árvore equilibrada, a busca tem custo O(log n). Se a árvore ficar muito inclinada para um lado, a busca pode chegar a O(n), como em uma busca sequencial na lista.

## Arquivos do projeto

- `main.py`: classes da árvore e menu interativo, com comentários simples.
- `README.md`: instruções, exemplo de uso e explicações da atividade.

## Observações

- Os termos começam vazios. Os exemplos acima precisam ser cadastrados pelo menu.
- Os dados ficam apenas na memória e são perdidos ao fechar o programa.
- As palavras são convertidas para minúsculas e os espaços nas pontas são removidos. Assim, `Python` e `python` são o mesmo termo.
- A comparação usa a ordem de caracteres do Python. Acentos são preservados; a ordem de palavras acentuadas pode diferir da ordem de um dicionário em português.
- A árvore não faz balanceamento automático.
- A remoção é um desafio opcional do PDF e não foi incluída nesta versão.
