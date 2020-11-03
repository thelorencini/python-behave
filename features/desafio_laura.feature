# language: pt

Funcionalidade: Desafio proposto por : Laura


Esquema do Cenario: Verificar CEPs
    Dado que entrei no site do "<site>"
    Quando eu realizar a busca pelo cep "<cep>"
    Então página apresentará a mensagem "<mensagem>"
    Exemplos:
    |site           |cep            |mensagem                       |
    |Correios       |14820766       |DADOS ENCONTRADOS COM SUCESSO. |
    |Correios       |14820000       |DADOS NAO ENCONTRADOS          |
