## 🛠️ Glossário de Comandos Utilizados

Abaixo estão as explicações dos principais conceitos Python aplicados neste projeto:

### 1. `def` (Definição de Função)
> Define um bloco de código reutilizável.
*   **Para que serve:** Permite organizar o programa em pequenas tarefas específicas. Em vez de escrever o mesmo código várias vezes, você o define uma vez e o "chama" quando precisar.

### 2. `append` (Adicionar à Lista)
> Método de listas para inserção de dados.
*   **Para que serve:** Adiciona um novo elemento ao final de uma lista existente. No projeto, é usado para ir guardando cada nota digitada pelo usuário dentro da lista de notas.

### 3. `len` (Comprimento/Length)
> Retorna a quantidade de itens.
*   **Para que serve:** Conta quantos elementos existem dentro de uma lista ou string. É fundamental para calcular a média (soma total dividida pelo `len` da lista).

### 4. `enumerate` (Contador Automático)
> Facilita a iteração com índices.
*   **Para que serve:** Em um laço `for`, ele fornece simultaneamente o **índice** (posição) e o **valor** do item. Isso elimina a necessidade de criar e somar variáveis de contagem manualmente (ex: `i = i + 1`).

### 5. `.2f` (Formatação de Decimais)
> Formata números flutuantes (float).
*   **Para que serve:** Limita a exibição de casas decimais. O `.2f` indica que o número deve ser mostrado com apenas 2 casas após o ponto, evitando números como `7.6666666`.

---

## 🚀 Como o código funciona

1.  **Entrada:** O usuário define a quantidade de alunos.
2.  **Processamento:** O sistema pede a nota de cada aluno e armazena usando `append`.
3.  **Cálculo:** O sistema utiliza `len` e `sum` para gerar a média.
4.  **Saída:** O sistema exibe as notas e avisa quais alunos estão com nota inferior a 6.0 usando `enumerate`.