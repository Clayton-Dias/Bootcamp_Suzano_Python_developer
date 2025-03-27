
# Desafio: Simulação de Sistema Bancário em Python

## Descrição

Este projeto implementa uma simulação simplificada de um sistema bancário em Python, utilizando os princípios da Programação Orientada a Objetos (POO). O sistema permite a criação de clientes, contas correntes, depósitos, saques e a visualização de extratos. Além disso, implementa um sistema de logging para registrar as transações.

## Funcionalidades

*   **Gerenciamento de Clientes:**
    *   Criação de clientes (apenas pessoa física).
    *   Armazenamento de informações como nome, CPF, data de nascimento e endereço.
*   **Gerenciamento de Contas Correntes:**
    *   Criação de contas correntes associadas a clientes.
    *   Atribuição de número de conta, agência e titular.
    *   Definição de limite de crédito e limite de saques.
*   **Operações Bancárias:**
    *   Depósitos: Adição de valor ao saldo da conta.
    *   Saques: Retirada de valor do saldo da conta (sujeito a limites e saldo disponível).
    *   Extrato: Exibição das transações realizadas na conta e o saldo atual.
*   **Histórico de Transações:**
    *   Registro de todas as transações realizadas em cada conta.
    *   Armazenamento do tipo de transação, valor e data/hora.
*   **Iterador de Contas:**
    *   Implementação de um iterador personalizado para percorrer a lista de contas, formatando as informações para exibição.
*   **Limitação de Transações:**
    *   Restrição do número máximo de transações por dia por conta.
*   **Logging:**
    *   Registro de todas as chamadas de função (transações) em um arquivo de log (`log.txt`).
    *   Informações registradas: data e hora, nome da função, argumentos e valor de retorno (ou exceção).

## Arquitetura do Código

O código é organizado em classes e funções, seguindo os princípios da POO:

*   **Classes:**
    *   `Cliente`: Classe base para clientes.
    *   `PessoaFisica`: Subclasse de `Cliente` para pessoas físicas.
    *   `Conta`: Classe base para contas bancárias.
    *   `ContaCorrente`: Subclasse de `Conta` para contas correntes.
    *   `Historico`: Classe para o histórico de transações.
    *   `Transacao`: Classe abstrata para transações.
    *   `Saque`: Subclasse de `Transacao` para saques.
    *   `Deposito`: Subclasse de `Transacao` para depósitos.
    *   `ContasIterador`: Iterador para a lista de contas.

*   **Funções:**
    *   `log_transacao(func)`: Decorador para registrar transações.
    *   `menu()`: Exibe o menu de opções.
    *   `filtrar_cliente(cpf, clientes)`: Busca cliente por CPF.
    *   `recuperar_conta_cliente(cliente)`: Recupera a conta do cliente.
    *   `depositar(clientes)`: Realiza um depósito.
    *   `sacar(clientes)`: Realiza um saque.
    *   `exibir_extrato(clientes)`: Exibe o extrato.
    *   `criar_cliente(clientes)`: Cria um novo cliente.
    *   `criar_conta(numero_conta, clientes, contas)`: Cria uma nova conta.
    *   `listar_contas(contas)`: Lista as contas.
    *   `main()`: Função principal que executa o sistema.

## Implementação

1.  **Estrutura de Classes:** As classes foram criadas para representar as entidades do sistema, com atributos e métodos relevantes. A herança foi utilizada para especializar classes (ex: `PessoaFisica` herda de `Cliente`, `ContaCorrente` herda de `Conta`).

2.  **Iterador:** A classe `ContasIterador` implementa os métodos `__iter__` e `__next__` para permitir a iteração sobre a lista de contas, formatando cada conta para exibição.

3.  **Decorador de Logging:**
    *   A função `log_transacao(func)` é um decorador que recebe uma função como argumento e retorna uma nova função (o `envelope`).
    *   O `envelope` executa a função original, registra informações sobre a execução em um arquivo de log (`log.txt`) e retorna o resultado da função original.
    *   O decorador registra:
        *   Data e hora atuais (UTC)
        *   Nome da função
        *   Argumentos da função
        *   Valor retornado pela função (ou exceção, se ocorrer)
    *   A anotação `@log_transacao` é usada para aplicar o decorador a cada função que precisa ser logada.
    *   É adicionado um tratamento de exceções.

4.  **Arquivo de Log:**
    *   As informações de log são armazenadas no arquivo `log.txt`, localizado na raiz do projeto.
    *   O arquivo é aberto em modo "append" (`"a"`), para que as novas entradas sejam adicionadas ao final do arquivo, sem sobrescrever o conteúdo existente.
    *   Cada entrada de log é escrita em uma nova linha.

5.  **Função Main:**
    *   A função `main()` orquestra a execução do sistema.
    *   Ela inicializa as listas de clientes e contas, exibe o menu de opções para o usuário e chama as funções apropriadas com base na opção selecionada.


## Como Executar

1.  Clone o repositório.
2.  Navegue até o diretório do projeto.
3.  Execute o arquivo `main.py`: `python main.py`
4.  Siga as instruções do menu para interagir com o sistema.


## Conclusão 

Em conclusão, este desafio prático de simulação de sistema bancário exemplifica os conceitos fundamentais da programação em Python e da Programação Orientada a Objetos (POO), e foi desenvolvido com o objetivo de consolidar e aplicar os conhecimentos adquiridos ao longo da trilha **Python Developer** da **DIO (Digital Innovation One)**. Ao completar este projeto, o participante demonstra proficiência em:

*   **Design e Implementação de Classes:** Criação de classes para modelar entidades do mundo real e organização do código.
*   **Herança e Polimorfismo:** Reutilização de código e especialização de classes.
*   **Iteradores:** Criação de iteradores personalizados para percorrer coleções de objetos.
*   **Decoradores:** Aplicação de decoradores para adicionar funcionalidades transversais.
*   **Tratamento de Exceções:** Implementação de mecanismos para lidar com erros e garantir a robustez do sistema.
*   **Modularização:** Organização do código em funções e módulos para facilitar a manutenção e reutilização.
*   **Logging:** Implementação de um sistema de logging para registrar informações sobre a execução do sistema.



