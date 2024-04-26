# 👨‍💻 Sistema Bancário 2.0
## Desafio proposto no Bootcamp Python AI Backend Developer da DIO.

## 🧾 Requisitos do programa:
- Separar as funções existentes de saque, depósito e extrato em
funções. Criar duas novas funções: Cadastrar usuário(cliente) e 
cadastrar conta bancária.

- Criar funções para as operações já existentes.
- Criar usuário (Cliente do banco)
- Criar conta corrente (Vincular com o usuário)

- Cada função vai ter uma regra na passagem de argumentos.
O retorno e a forma como serão chamadas, pode ser definida
do meu modo.

- SAQUE: A função saque deve receber os argumentos apenas por
nome (Keyword only). Sugestão de argumentos: saldo, valor,
extrato, limite, numero_saques, limite_saques. Sugestão de
retorno: saldo e extrato.


- DEPÓSITO: A função depósito deve receber os argumentos apenas
por posição (positional only). Sugestão de argumentos: saldo,
valor, extrato. Sugestão de retorno: saldo e extrato.

- EXTRATO: A função extrato deve receber os argumentos por
posição e nome (positional only e keyword only). Argumentos
posicionais: saldo, argumentos nomeados: extrato.

- CRIAR USUÁRIO: O programa deve armazenar os usuários em
uma lista, um usuário é composto por: nome, data de nascimento,
cpf e endereço. O endereço é uma string com o formato:
logradouro, n° - bairro - cidade/ UF. Deve ser armazenado
somente os números do CPF. Não podemos cadastrar 2 usuários
com o mesmo CPF.

- CRIAR CONTA CORRENTE: O programa deve armazenar contas em
uma lista, uma conta é composta por: agência, número da conta
e usuário. O número da conta é sequencial, iniciando em 1. O
número da agência é fixo: "0001". O usuário pode ter mais de
uma conta, mas uma conta pertence a somente um usuário.
