# Módulo 8 — Navegador e aplicações sensíveis

Distinguir seleção de candidatos de execução e supervisão profissional.

## Aula 8.1 — Escolher elemento pelo texto

A modalidade documentada do Jev consultada para este curso é texto. Portanto, um fluxo de navegador precisa preparar uma representação textual: elementos do DOM, nomes acessíveis ou uma lista de candidatos. Enviar uma captura de tela diretamente não corresponde a esse contrato.

Uma Choice pode selecionar o identificador de um candidato. O código consulta o DOM novamente antes de agir, pois a página pode ter mudado desde a extração. Se o elemento não existe ou sua função é diferente, o fluxo deve parar ou atualizar os candidatos, sem clicar numa posição antiga por aproximação.

Inclua uma opção nenhum e trate ambiguidade entre elementos parecidos. Medir só a rapidez do classificador omite extração, navegação e execução. O desempenho relevante é completar a tarefa corretamente, com limites de ação. Neste curso, o exemplo apenas escolhe um ID textual e não controla um navegador externo.

### Exemplo resolvido

Lista: nav-home = Início; download-pdf = Baixar relatório; remove-account = Excluir conta. Para baixar o relatório, o candidato é download-pdf.

### Sua vez

O botão mudou depois da classificação. Reutilizar a coordenada antiga é aceitável?

<details>
<summary>Conferir resposta comentada</summary>

Não. Validar o elemento atual pelo identificador e sua função, ou extrair novamente. A decisão não é autorização para clicar em qualquer posição.

</details>

## Aula 8.2 — Organizar revisão clínica fictícia

Este caso é um exercício administrativo com dados inventados. A tarefa é reconhecer se um campo obrigatório está preenchido e organizar uma fila para revisão humana. Não estamos classificando doenças, recomendando tratamento ou priorizando pacientes reais.

Uma ficha com campo de alergias vazio não demonstra que a pessoa não tem alergias. Mostra ausência de informação. A política do exercício determina que esse caso seja encaminhado ao profissional responsável para completar a ficha. Mesmo uma resposta muito confiante não elimina a necessidade dessa revisão.

Em um domínio sensível, é especialmente importante declarar o limite da atividade. O mesmo software usado para um exercício não se torna adequado a uso clínico real por ganhar uma interface bonita. Uma implantação real exigiria projeto específico, profissionais responsáveis e validação no contexto apropriado. Aqui aprendemos a manter o escopo administrativo e a opção de insuficiência.

### Exemplo resolvido

Campo obrigatório vazio → revisar. Nunca traduzir o vazio em “sem alergias”. O laboratório mantém revisão obrigatória neste caso.

### Sua vez

Por que um limiar mais alto de confidence não transforma esse exercício em um sistema de diagnóstico?

<details>
<summary>Conferir resposta comentada</summary>

Porque o tipo de tarefa, dados, validação e responsabilidade são diferentes. Um número alto não cria capacidade clínica nem autorização para usá-la.

</details>

## Aula 8.3 — Organizar alertas fictícios

Considere um fluxo inventado de acompanhamento de documentos financeiros. A política do exercício manda revisar uma retificação, acompanhar uma atualização pertinente e arquivar notícias sem relação com o tema. O objetivo é organizar informação, não decidir investimentos.

Uma classificação deve apoiar-se na política e no documento fornecidos. “O preço caiu” não define sozinho qual ação tomar; o sistema precisa conhecer a regra que está aplicando. Para um protótipo educacional, mantemos o encaminhamento supervisionado e não conectamos execução de transações.

O erro mais importante pode ser o descarte indevido de algo relevante. Por isso, a avaliação deve observar falsos negativos e não apenas a proporção total de acertos. Uma fila que parece muito eficiente por arquivar quase tudo pode estar escondendo informação. A revisão deve incluir amostras dos itens arquivados, além dos alertas destacados.

### Exemplo resolvido

“O emissor retificou o demonstrativo” + política “retificações vão para revisão” → revisar. Sem ordem de compra ou venda.

### Sua vez

Uma avaliação revisa apenas os alertas selecionados. Qual problema ela deixa de observar?

<details>
<summary>Conferir resposta comentada</summary>

Os alertas relevantes descartados. É necessário auditar também os arquivados para medir falsos negativos.

</details>

[Voltar ao índice](../README.md)
