# Módulo 1 — Onde Jev entra

Escolher entre uma regra, uma decisão delimitada e uma resposta generativa.

## Aula 1.1 — Decidir, gerar ou calcular

Imagine a caixa de entrada de uma equipe de cursos. Uma mensagem pede uma nova senha, outra quer saber o preço e uma terceira contesta uma cobrança. Antes de escrever uma resposta, a equipe precisa decidir quem recebe cada pedido. Essa escolha tem poucas alternativas conhecidas e pode ser estudada separadamente da redação da resposta.

Jev é apresentado pela TypeSafe como um modelo voltado a decisões estruturadas. Isso não significa que toda decisão precise dele. Somar uma fatura, verificar se um campo está vazio ou procurar um código exato são tarefas que o software convencional pode resolver. Escrever uma explicação personalizada é trabalho de geração de texto. Classificar uma intenção expressa de várias maneiras é um candidato a um modelo decisor.

A primeira pergunta de projeto é: qual parte do trabalho exige interpretação? Separe essa parte das regras exatas e das ações. O sistema pode classificar uma cobrança sem ter permissão de fazer um estorno. Essa separação permite testar o julgamento sem alterar o mundo externo.

### Exemplo resolvido

Calcular 3 × R$ 50 → código. Identificar se a mensagem pede suporte → decisão delimitada. Redigir uma explicação de recuperação de acesso → geração de texto.

### Sua vez

Separe estas tarefas: somar pedidos, escolher a equipe responsável e escrever uma resposta acolhedora. Qual saída cada etapa deve produzir?

<details>
<summary>Conferir resposta comentada</summary>

A soma produz um número por cálculo; a triagem produz uma etiqueta entre opções permitidas; a resposta produz texto. Não usar IA para a soma quando os dados já são estruturados.

</details>

## Aula 1.2 — Contexto, pergunta e opções

Uma decisão depende de três elementos. O contexto contém o material a avaliar. A pergunta declara exatamente o julgamento desejado. As opções delimitam as respostas que o sistema sabe interpretar. Se qualquer um deles estiver mal definido, a saída pode ser válida no formato e inútil para a operação.

Considere um hotel que anuncia cancelamento gratuito. A política esclarece que o valor volta como crédito para outra hospedagem. Quem precisa do dinheiro de volta não está atendido por essa condição. A pergunta “o hotel é bom?” mistura preferências; “a política prevê reembolso em dinheiro?” é mais específica. Uma classificação entre dinheiro, crédito e informação insuficiente deixa o próximo passo claro.

A ausência de uma informação não prova a alternativa negativa. Se a política disser apenas “cancelamento permitido”, ainda não sabemos como o valor retorna. É útil reservar uma opção explícita para insuficiência, além de uma política que reconheça ambiguidade. O modelo não deve completar o documento com uma condição que parece provável.

### Exemplo resolvido

Contexto: “reembolso em crédito válido por 12 meses”. Pergunta: “qual a forma de devolução?”. Opções: dinheiro / crédito / não informada. Gabarito: crédito.

### Sua vez

Reescreva a pergunta para alguém que precisa de dinheiro de volta e trate a política que não menciona reembolso.

<details>
<summary>Conferir resposta comentada</summary>

Perguntar se o trecho confirma reembolso em dinheiro. Usar opções confirma / contraria / insuficiente. A omissão vai para insuficiente, sem inventar uma condição.

</details>

## Aula 1.3 — Ler promessas com cuidado

Um anúncio pode mostrar grande diferença de velocidade entre dois sistemas. Para entender o número, precisamos saber qual tarefa foi usada, quanto contexto entrou, qual modelo foi comparado, que configuração ele tinha e o que conta como resposta correta. Um máximo observado não vira uma vantagem fixa em qualquer uso.

Também é necessário separar validade estrutural de validade semântica. Se as opções são vendas, suporte e cobrança, uma resposta “cobrança” pode obedecer perfeitamente ao contrato e ainda estar errada. Um sistema que nunca sai da lista não está automaticamente protegido contra interpretações equivocadas.

Ao ler um benchmark, procure a unidade de medida. Uma chamada pode responder várias perguntas. Acertar todas as perguntas de uma chamada é diferente de acertar a maioria das etiquetas. Procure dados reais, referência humana, distribuição por classe e custo completo. A postura útil é transformar uma promessa em uma hipótese que pode ser testada.

### Aprofundamento da versão 1.2.0

Audite uma demonstração separando entrada, julgamento, execução e evidência de efeito. Opções prontas podem resolver trabalho real; não demonstram geração arbitrária. Um jogo com estado textual não comprova visão nem autonomia física. Consulte o laboratório L12.

### Exemplo resolvido

“200 vezes mais rápido” vira: “o fornecedor relatou esse ganho em determinados workflows; ainda vamos medir nosso atendimento em português”.

### Sua vez

Corrija: “Como a saída é sempre uma opção válida, podemos confiar em toda decisão”.

<details>
<summary>Conferir resposta comentada</summary>

Uma opção válida evita certos erros de formato, mas pode representar o julgamento errado. Precisamos medir erro por classe e definir revisão.

</details>

[Voltar ao índice](../README.md)
