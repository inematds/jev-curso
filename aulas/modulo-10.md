# Módulo 10 — Medir qualidade de verdade

Comparar métodos sem confundir exemplos ajustados com evidência independente.

## Aula 10.1 — Construir referência humana

Uma avaliação começa com a definição do que é correto. Se os rótulos mudam de pessoa para pessoa, a métrica pode estar medindo desacordo de processo. Crie um guia de rotulagem, revise exemplos e documente os casos que não se encaixam bem.

Separe desenvolvimento, calibração e teste. Use desenvolvimento para melhorar perguntas; calibração para escolher limiares; teste para verificar a política congelada. Mensagens da mesma conversa não podem ficar em partições diferentes, pois isso facilita o reconhecimento de conteúdo já visto. Quando houver variação no tempo, avalie também dados posteriores.

Os 24 tickets fictícios do laboratório servem para aprender a executar e ler uma avaliação. Não são uma amostra representativa de uma empresa nem comprovam adequação à produção. Um dataset operacional precisa cobrir as classes, ambiguidades e mudanças do tráfego real, com revisão humana e proteção dos dados.

### Exemplo resolvido

Uma conversa com três mensagens deve ficar inteira na mesma partição. Dividir as mensagens entre treino de perguntas e teste causa vazamento de contexto.

### Sua vez

Pode ajustar a pergunta depois de olhar o erro do teste final e divulgar a nova taxa no mesmo teste como independente?

<details>
<summary>Conferir resposta comentada</summary>

Não. O teste foi usado no ajuste. É necessário reservar outro conjunto para uma nova avaliação independente.

</details>

## Aula 10.2 — Comparar alternativas

Use a mesma tarefa e os mesmos dados para comparar regras, Jev, um modelo generativo com saída estruturada e um fluxo híbrido. Registre configurações e versões. Diferenças de entrada ou de critérios tornam a comparação difícil de interpretar.

Acurácia informa a proporção total de acertos, mas pode esconder classes pequenas. A matriz de confusão mostra para onde cada classe foi encaminhada. Macro-F1 dá o mesmo peso às classes, embora também precise ser lida com as contagens. Observe especialmente o erro que tem maior custo operacional.

Meça latência ponta a ponta e custo de todas as tentativas. O resultado da baseline lexical deste projeto é reproduzível pela CLI: ele apresenta acertos e erros conhecidos no conjunto fictício. Não compare esse tempo local de regra com latência de rede como se fossem a mesma coisa. O experimento Jev real só poderá ser reportado após execução com acesso ao serviço.

### Exemplo resolvido

python3 -m jev_lab batch data/tickets-sinteticos.jsonl --out reports/baseline produz metrics.json e predictions.csv, usando regras locais.

### Sua vez

Uma classe muito comum tem 99% de acerto e outra importante tem 40%. A média global basta?

<details>
<summary>Conferir resposta comentada</summary>

Não. Reportar métricas por classe, suporte amostral, matriz de confusão e custo dos erros. A média pode esconder a classe importante.

</details>

## Aula 10.3 — Escolher e congelar limiares

Ao aumentar um limiar, normalmente menos respostas passam para a sugestão automática. Isso pode reduzir alguns erros, mas aumenta a revisão e pode deixar passar os erros mais confiantes. Precisamos medir duas coisas juntas: qualidade dos casos aceitos e cobertura, a fração de casos que a política aceita.

Escolha o limiar no conjunto de calibração e congele antes do teste. Registre se ele usa a probabilidade da classe, confidence ou ambos. Não copie o limiar de uma primitiva para outra, de um idioma para outro ou de uma versão para outra sem avaliação.

A incerteza da medição importa. Se dez exemplos passaram sem erro, ainda não temos prova de que a taxa de erro seja pequena. Quanto mais estreita a meta, maior tende a ser a necessidade de dados. Quando a amostra é insuficiente, a conclusão correta pode ser coletar mais exemplos, em vez de declarar sucesso.

### Aprofundamento da versão 1.2.0

A CLI experiment registra dataset, template, política, modelo, falhas e procedência. O modo replay permite comparar respostas externas, incluindo LLM, mas não autentica a origem declarada. Uma comparação de modelo isolado deve ter entrada equivalente; uma comparação de fluxo mede a tarefa inteira.

### Exemplo resolvido

No laboratório didático, varie confidence de 0,90 para 0,95. A resposta fictícia com confidence 0,91 passa de sugestão para revisão.

### Sua vez

Por que essa interação com valores inventados não comprova que 0,95 é o limiar certo?

<details>
<summary>Conferir resposta comentada</summary>

Porque não mede respostas reais contra rótulos independentes. Demonstra apenas como uma política reage aos números.

</details>

[Voltar ao índice](../README.md)
