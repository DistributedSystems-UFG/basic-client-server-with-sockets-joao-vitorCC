[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar um servidor com outras funcionalidades (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.

# 🚀 Python TCP Operations Server

Um servidor de eco multitarefa robusto, desenvolvido em Python utilizando a biblioteca `socket`. Este servidor é capaz de processar operações matemáticas e manipular strings, tratando erros de entrada de forma resiliente.

## 📋 Funcionalidades

- **Cálculos Matemáticos**: Realiza somas e cálculos de raiz quadrada.
- **Validação de Dados**: Proteção contra entradas não numéricas usando blocos `try/except`.
- **Tratamento de Strings**: Normalização de comandos (ignora maiúsculas/minúsculas e espaços extras).
- **Log de Conexão**: Exibe o endereço IP e a porta de cada cliente conectado no terminal do servidor.

---

## 🛠️ Como Executar

### 1. Pré-requisitos
* Python 3.x instalado.

### 2. Iniciando o Servidor
Clone o repositório e execute o script principal:
```bash
python server.py
```
---

## 🛠️ Como Executar no lado cliente

| Comando    | Descrição | Exemplo de Entrada | Saída Esperada |
| ---------- | ----- | ------ | ------ |
| SOMA    | Soma dois números reais  | SOMA 15 25.5 |Resultado da soma: 40.5|
| RAIZ   | Calcula a raiz quadrada  | RAIZ 64 | A raiz de 64.0 é 8.0|
| INVERTE   | Inverte as letras de uma string  | INVERTE 123456 abc |Texto invertido: cba 654321|
