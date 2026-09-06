# Decisões do programa "Chamados Helpdesk"

## Tema escolhido

O tema que eu escolhi foi um sistema de chamados para suporte de TI inspirado no GLPI. A escolha se deu ao fato de eu possuir experiência prévia com esse tipo de programa e já ter ideias para implementações adicionais no programa. Além disso, o meu sistema foi feito para ser um "template" a ser adotado por qualquer empresa que queira adotar o sistema. O design é básico, o título é genérico, e ainda deixei espaços para a logo da empresa e campos para divulgar sua marca, assim como no GLPI.

## Stack escolhida

### Python + Django

Escolhi Python por já ter experiências anteriores com a linguagem, e pelo fato de ser melhor para o meu currículo ter mais experiência com essa linguagem. Sobre o framework, eu nunca tive experiência com nenhum framework em Python, então qualquer um que eu escolhesse seria coisa nova para mim, então fiz minha pesquisa. Fiquei entre Flask, Express e Django. Django já traz pronto o que este teste pede: autenticação, proteção de rotas, criação do usuário admin por um comando e criação das tabelas do banco. Também é possível fazer isso com Flask e Express, mas toda a implementação deveria ser feita manualmente. Como eu tinha 7 dias para fazer o projeto, decidi ir pelo mais prático, o que daria mais tempo para focar nas outras áreas do projeto.

**Desvantagens:** Django é grande para um sistema de sete requisitos e faz muita coisa sem que eu veja. Precisei estudar sessão de login e proteção de rotas para não entregar código que não soubesse explicar. Também aceitei a organização de pastas que o framework impõe em vez de definir a minha.

### SQLite

Optei pelo SQLite por ele ser mais fácil de manusear, tanto por mim, quanto pelo usuário que vai testar o programa na máquina, já que ele é simplesmente um arquivo na pasta do projeto.

**Desvantagens:** Por o banco de dados ser apenas um arquivo dentro do projeto, ele não lida bem com muitas escrituras simultâneas, além de não ser ideal para colocar em uma produção real. Mas como o escopo desse projeto é menor, eu decidi usar ele.

### HTML e CSS (Tailwind)

Eu já havia experiência com HTML e CSS anteriormente, além de HTML e CSS serem o básico do frontend.

**Disclaimer:** O frontend foi 100% pela IA, foi feito apenas o básico da interface para não ficar muito feio ou amador, me dando mais tempo para focar no código do projeto.

## Comentários e decisões sobre o projeto

### Status do chamado

A especificação do trabalho restringe o estado do chamado em "pendente, confirmado e cancelado", o que não corresponde com a realidade de um chamado de suporte, então fiz uma adição/adaptação. Usei o `choices` do Django, que guarda dois valores por opção, um para entrar no banco de dados (pendente, confirmado e cancelado) e outro a ser mostrado ao usuário: "Chamado aberto, aguardando triagem | Triado e aceito, na fila do técnico | Recusado — duplicado, fora de escopo ou resolvido pelo próprio usuário". Além disso adicionei a opção do usuário logado conseguir alterar o status dos chamados, para melhor gerenciamento de trabalho.

### Categorias

Eu queria separar o chamados em 3 categorias: "Hardware, Software e Redes". Mas o usuário na maioria das vezes não sabe o que é isso, então eu fiz da mesma forma que fiz com os status, usando `choices`: Deixei "Hardware, Software e Redes" no banco, mas adicionei outro texto para o usuário: "Computador não liga / Computador lento | Programa não funciona | Problemas com internet / sistema". Além de adicionar uma quarta categoria chamada "Não sei identificar", para não confundir o técnico caso o cliente seja leigo.

### Descrição

Foi adicionado um campo novo ao formulário, chamado "Descrição", que permite o usuário descrever o seu problema com detalhes. Além disso implementei uma opção no painel para visualizar os detalhes de cada formulário, para não contaminar visualmente o painel.

### Adicionais

Os adicionais foram voltados para interface de usuário, deixando o programa usável em um ambiente de trabalho(na medida do possível).

## Uso de IA

Como mencionado anteriormente, eu nunca havia trabalhado com um framework de Python, então foi a primeira vez. A IA fez o crud e me guiou pela estrutura dos projetos do django, me explicando o que cada coisa fazia e como. A IA escreveu praticamente todo o código, mas mais da metade desses 7 dias foram usados estudando o que cada linha do código fazia, principalmente as partes feitas diretamente pelo Django, como autenticação e proteção do painel por login. Sobre a parte das decisões: Tirando as decisões voltadas 100% ao código, eu tomei todas. 

Sobre erros que a IA cometeu, nenhum foi dela propiamente dita, foram erros de implementação da minha parte. Sobre sugestões tomadas contra a IA, teve a decisão sobre a marca. A IA queria que eu desenvolvesse uma marca do zero, já eu optei por fazer um sistema genérico com o intuito de ser personalizado pelo cliente que adotá-lo. 
