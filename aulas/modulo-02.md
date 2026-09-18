# Módulo 2 — Os três tipos de pergunta

Distinguir Choice, Noul e Score a partir do tipo de resposta necessário.

## Aula 2.1 — Choice: escolher uma alternativa

Choice serve para escolher entre alternativas descritas previamente. Em uma triagem, as opções podem representar equipes. Os nomes devem ser estáveis para o código e os critérios devem ser compreensíveis para quem rotula exemplos. Não basta escrever uma lista de palavras vagas: “financeiro” e “administrativo” podem se sobrepor se as fronteiras não forem explicadas.

Uma boa opção inclui o que a caracteriza. Cobrança pode abranger fatura, pagamento duplicado e solicitação de estorno. Suporte pode abranger acesso, erro de login e falha de uso. Se a pessoa falar de dois problemas independentes, o produto precisa decidir se escolhe uma fila principal, abre duas tarefas ou pede revisão. Uma Choice isolada seleciona uma opção; ela não resolve por si só essa decisão de produto.

A resposta documentada inclui a alternativa e uma distribuição de probabilidades. Leia essa distribuição como saída do modelo, não como a quantidade real de pessoas de cada equipe. Antes de executar qualquer ação, valide que a opção existe e que a política permite o encaminhamento.

### Exemplo resolvido

“Paguei duas vezes” → cobrança. “A senha não funciona” → suporte. “Preciso de senha nova e estorno” → regra de múltiplas intenções ou revisão.

### Sua vez

Defina critérios para vendas e suporte que não se confundam quando alguém pergunta como contratar.

<details>
<summary>Conferir resposta comentada</summary>

Vendas trata de interesse em planos ou contratação; suporte trata de dificuldade técnica no serviço. Uma pergunta comercial sobre contratação não é automaticamente um problema técnico.

</details>

## Aula 2.2 — Noul: probabilidade de sim

Noul responde a uma pergunta binária com um número entre zero e um. O valor representa a probabilidade de “sim” segundo o modelo. Próximo de um aponta para sim; próximo de zero aponta para não. O valor intermediário não representa uma intensidade intermediária do assunto: ele indica que as alternativas não estão bem separadas.

Se a pergunta é “há um pedido de estorno?”, 0,05 não significa baixa confiança na resposta negativa. Significa pouca probabilidade de sim. Não copie uma política de Choice que lê o campo confidence: a primitiva Noul não devolve esse campo separado. Se precisar de três estados operacionais, seu código pode aplicar dois limiares e deixar uma faixa de revisão no meio.

Escreva a pergunta de maneira afirmativa e literal. Evite a dupla negação “não é verdade que não pediu estorno?”. Se a falta de contexto precisa ser uma categoria explícita, considere Choice ou uma pergunta separada de suficiência. Não assuma que um número perto de zero prova que a informação necessária estava presente.

### Exemplo resolvido

Política didática, ainda não calibrada: p ≥ 0,90 sugere sim; p ≤ 0,10 sugere não; demais valores pedem revisão. Esses limites são exemplos, não garantias.

### Sua vez

Interprete Noul=0,50 para “a pessoa tem experiência em Python?”. É experiência média?

<details>
<summary>Conferir resposta comentada</summary>

Não. É uma resposta binária sem forte preferência por sim ou não. Para medir nível de experiência, definir níveis em Score.

</details>

## Aula 2.3 — Score: níveis ordenados

Score é adequado quando existe uma escala com descrições. “Como está a prioridade?” só funciona bem se cada nível tiver um significado operacional. Baixa pode significar dúvida sem bloqueio; média, dificuldade com alternativa de contorno; alta, bloqueio do trabalho sem alternativa. O objetivo é tornar a rubrica revisável por pessoas.

A saída pode cair entre níveis porque resulta de uma distribuição sobre eles. Um valor 1,6 em níveis 0, 1 e 2 não é necessariamente um erro. Também não é uma medida física precisa. Score não é um substituto de cálculo de valores monetários, contagem de itens ou comparação exata de datas.

Separe dimensões independentes. Urgência, impacto e tom emocional são coisas diferentes. Uma pessoa pode escrever com calma sobre um problema grave. Pergunte por dimensão e combine os resultados em uma regra explícita. Quando a empresa alterar a prioridade de cada fator, será possível mudar a regra sem esconder a mudança numa pergunta ampla.

### Exemplo resolvido

Níveis: 0 = sem bloqueio; 1 = bloqueio com alternativa; 2 = bloqueio sem alternativa. Um tom cordial não impede nível 2.

### Sua vez

Crie uma rubrica de três níveis para dificuldade de acesso. Evite usar “bom”, “médio” e “ruim” sem explicar.

<details>
<summary>Conferir resposta comentada</summary>

0: acessa normalmente e tem dúvida de uso. 1: parte do conteúdo falha, mas há alternativa funcional. 2: não consegue acessar o conteúdo necessário e não tem alternativa.

</details>

[Voltar ao índice](../README.md)
