# Guia completo de Expressões regulares

Usando Ctrl + H para abrir a barra de pesquisa
selecione a opção "Use Regular Expression"
através dela voce consegue achar os caracteres pelos quais procura em seu 
código/texto
- caso queira achar todos os número contidos no texto use: \d 
- caso não saiba o primeiro digito de um número, mas sabe o que se segue use: \d23
- do mesmo jeito voce pode utilizar: 1\d3

* Ponto - ele é como um coringa
- utilize ... para achar toda sequencia de três caracteres
- utilize \. para escapar o ponto, ou melhor, para pesquisar apenas o ponto
- ..\... voce também pode usar este método para achar caracteres junto dos pontos

* [] - podemos usar colchetes para específicar o que estamos procurando Ex: [oa]
* [^w] - encontrar todos os caracteres menos o caractere w
use o - para indicar uma faixa. Ex: [5-9]
isso pode ser utilizado para letrar também [t-z]

------------------------------------------------------------------------------------------------------------------------------------
### SITE: casa do desenvolvedor
link: https://blog.casadodesenvolvedor.com.br/expressoes-regulares-regex/?gad_source=1&gclid=Cj0KCQjwyL24BhCtARIsALo0fSAbd34eFmdb5gbGK_Mst3O1nU5iK4oVoP5fco_dd-9xAtH1uUxiZqQaAt-wEALw_wcB

## Classes
São definidas entre colchetes [], isso indica que estamos buscando especificamente o caractere informado dentro dos colchetes

por exemplo, dado determinado texto quero que encontre a letra "a" então escrevemos o seguinte padrão [a]

existem várias classe de caracteres prontas que podemos utilizá-las para facilitar nossas operações

estas são algumas classes comumente utilizadas

[A-Z] - significa de A até Z, sempre maiúscula.

[a-z] - significa de a até z, sempre minúscula,

[A-Za-z] - significa A-Z ou a-z.

\d - significa todos os dígitos e é atalho para [0-9]

\w - significa word char e é um atalho para [A-Za-z0-9_].

\s significa whitespace normalmente é um atalho para [ \t\r\n\f] onde:

O primeiro caractere é um espaço branco.

\t é um tab.

\r é carriage return.

\n é newline.

\f é form feed.

## Quantificadores
São identificadores para dizer quantas vezes determinada expressão deve aparecer em sequência

? - zero ou uma vez.

* - zero ou mais vezes.

+ - uma ou mais vezes.

. - o "ponto" que significa qualquer caractere

{ e } - as chaves servem para definir uma quantidade de caracteres específicas que é desejado encontrar

 Por exemplo:

  a{3} - letra a 3 vezes.

{n} - exatamente n vezes.

{n,} - no mínimo n vezes.

{n,m} - no mínimo n vezes, no máximo m vezes.

Com \ (barra) podemos escapar metacaracteres, se quisermos procurar pelo * ou . literalmente (sem significado especial), devemos utilizar o caractere \

Por exemplo: \..

Podemos combinar classes com quantificadores o que nos dá ainda mais poder pesquisar informações, alguns exemplos:

\d*- um dígito, zero ou mais vezes

[.-]*   - ponto ou hífen zero, uma ou mais vezes.

[.-]{1} - ponto ou hífen uma vez.

[.-]?   - ponto ou hífen zero ou uma vez.

## Agrupamentos
São representados pelos metacaracteres ( ), utilizamos para agrupar regras ou extrair informações 

() - Declaramos um grupo 

?: - Non-Capturing group

exemplo (?:de\s+)  não deve devolver o grupo formado pela preposição de e por um \s

## Âncoras
Quando precisamos encontrar determinada informação delimitando uma parte da informação podemos usar as âncoras:

\b - (minúsculo) é uma âncora que seleciona um word boundary, isso é o início ou fim da palavra. 

^  - Garantir que nada vem antes.

$ - Garantir que nada vem depois.

\B - (B maiúsculo) non-word-boundary comportamento inverso a sílaba alvo deve aparecer dentro de uma palavra, nunca no início ou fim.


## Negação

Às vezes é mais vantajoso selecionarmos a informação que não queremos e para isso podemos utilizar

\W  - (maiúsculo) é a non-word char, ou seja, tudo que não é um word char. \W é um atalho para [^\w].

\D  - (maiúsculo) é um non-digit, sendo \D um atalho para [^\d] 

Repare também que não usamos a metacaractere ^ como âncora, pois aparece dentro de uma classe [^>]

Com esses conceitos estabelecidos já é possível criar um regex para uma finalidade específica ou então compreender um padrão já existente que precise ser modificado

Vamos analisar um exemplo do cotidiano que utilizamos regex

regex para validação de formatação de CPF:

(\d{3})[.]?(\d{3})[.]?(\d{3})[-]?(\d{2})

Separando em cores podemos perceber que existem um conjunto de regras sendo aplicadas com o objetivo de validar se a informação está no formato correto de um CPF

Vamos descrever a regras e exibir a parte correspondente desta regra

CPF é composto  por

3 dígitos e após os dígitos pode ou não estar separados por um ponto
(\d{3})[.]?

Seguido de mais 3 dígitos e após os dígitos pode ou não estar separados por um ponto
(\d{3})[.]?

Seguido de mais 3 dígitos e após os dígitos pode ou não estar separado por um traço
(\d{3})[-]?

Seguido de mais 2 dígitos
(\d{2})