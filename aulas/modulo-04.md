# Módulo 4 — Custo e escolha do primeiro caso

Calcular a viabilidade incluindo o trabalho que acontece depois do modelo.

## Aula 4.1 — A conta de dez mil tokens

Uma tarifa por milhão de tokens precisa ser convertida antes de multiplicar pelo volume de chamadas. Na referência de preço consultada em 18/09/2026, a entrada do Jev custa US$ 0,042 por milhão. Para 10.000 tokens totais de entrada, dividimos 10.000 por um milhão e multiplicamos por 0,042. O resultado é US$ 0,00042.

Mil chamadas iguais custariam US$ 0,42 de entrada; dez mil, US$ 4,20; cem mil, US$ 42. Observe as casas decimais. Um erro de zero muda toda a comparação. Trabalhe em uma única moeda e mantenha separadas estimativa e cobrança real.

Tokens não são palavras, caracteres ou documentos. Um contexto longo e critérios detalhados podem consumir mais entrada. Para o orçamento definitivo, use a contagem retornada pelo serviço e verifique a tarifa da rota utilizada. O laboratório permite editar o preço para atualizar a conta sem reescrever o curso.

### Exemplo resolvido

Custo = chamadas × tokens totais médios ÷ 1.000.000 × preço por milhão. Em 10.000 × 10.000 tokens, a estimativa é US$ 4,20.

### Sua vez

Calcule 100.000 chamadas de 2.000 tokens na tarifa de referência.

<details>
<summary>Conferir resposta comentada</summary>

100.000 × 2.000 ÷ 1.000.000 × 0,042 = US$ 8,40. É apenas a entrada do modelo, sem outros custos.

</details>

## Aula 4.2 — Custo do processo inteiro

Uma chamada barata não garante um processo barato. Depois da triagem pode haver modelo generativo, revisão humana, extração de texto, armazenamento e retrabalho. Se o erro direcionar um pedido para a equipe errada, o custo real inclui o tempo de corrigir o encaminhamento.

Compare duas operações completas. Na referência, todos os eventos seguem o fluxo atual. No híbrido, todos passam pela triagem e uma parte segue ao modelo maior ou à revisão. As chamadas residuais podem ser justamente as mais difíceis e caras; não presuma que custam a mesma média das anteriores.

Inclua ainda o esforço de implantação amortizado pelo período de uso. Um processo de pequeno volume pode não justificar uma integração complexa, mesmo com grande economia percentual de tokens. Faça uma análise de sensibilidade: o resultado continua positivo se a taxa de fallback dobrar ou a revisão humana levar o dobro do tempo?

### Exemplo resolvido

Cenário fictício: baseline US$ 1.000; Jev US$ 8,40; LLM residual US$ 200. Economia bruta US$ 791,60, antes de revisão, infraestrutura e implantação.

### Sua vez

Adicione US$ 500 de revisão e US$ 400 de implantação amortizada ao cenário. Ainda economiza?

<details>
<summary>Conferir resposta comentada</summary>

Não. O híbrido soma US$ 1.108,40 e supera a baseline de US$ 1.000. A economia de tokens foi consumida pelos outros custos.

</details>

## Aula 4.3 — Escolher um piloto

Um primeiro piloto deve responder a uma pergunta de negócio pequena e verificável. “Automatizar toda a empresa” não oferece um critério de conclusão. “Sugerir a fila de tickets em português sem aumentar o retrabalho” permite reunir exemplos, revisar os resultados e decidir se vale avançar.

Prefira um caso com alternativas claras, dados disponíveis, frequência suficiente e consequência reversível. Também é necessário alguém que saiba dizer o que é correto. Se nem as pessoas concordam sobre as categorias, a primeira tarefa é ajustar o processo e a rotulagem, não escolher o modelo.

A matriz de prioridade pode combinar volume, tempo humano por caso, facilidade de obter referência e impacto do erro. Não use a matriz como matemática exata: ela torna o debate visível. Um caso chamativo de navegador ou agentes pode vir depois de uma triagem simples que prove o valor e revele as limitações do domínio.

### Exemplo resolvido

Piloto recomendado: sugerir suporte, cobrança ou vendas em tickets. Fase inicial: apenas observar a sugestão e comparar com o encaminhamento humano.

### Sua vez

Compare triagem de tickets com execução automática de reembolsos. Qual começa primeiro e por quê?

<details>
<summary>Conferir resposta comentada</summary>

Triagem: consequência reversível, revisão mais simples e menor necessidade de permissões. Reembolso exige um projeto separado de regras, autorização e controle.

</details>

[Voltar ao índice](../README.md)
