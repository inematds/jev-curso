# Módulo 12 — Projeto final

Entregar uma decisão de adoção fundamentada, inclusive quando a resposta for não automatizar.

## Aula 12.1 — Especificar a triagem

Seu projeto final é uma triagem de atendimento em português. Comece descrevendo quem recebe os tickets, quais filas existem e qual problema deseja reduzir. Evite prometer automação total. A primeira entrega é uma especificação que outra pessoa consegue revisar.

Defina os critérios de cada alternativa, casos ambíguos e o tratamento de informação ausente. Acrescente cinco exemplos difíceis: negação, duas intenções, texto incompleto, sinônimo e instrução indevida dentro do ticket. Mostre como cada um deveria ser tratado e por quê.

Depois desenhe a política externa ao modelo. Ela define ações permitidas, revisão, falhas de contrato, prazo e limite de tentativas. Inclua orçamento e plano de avaliação. O projeto sem código pode usar planilha; o técnico deve acrescentar requisições, testes e relatório reproduzível. Ambos precisam separar fatos, hipóteses e resultados.

### Exemplo resolvido

Entrega: taxonomia + cinco casos difíceis + perguntas + política + diagrama + orçamento + protocolo de avaliação + plano de retorno.

### Sua vez

Escreva uma frase que descreva o sucesso do seu piloto sem usar “IA mais inteligente”.

<details>
<summary>Conferir resposta comentada</summary>

Exemplo: reduzir o tempo de triagem mantendo o erro por fila dentro do limite acordado, com custo total menor e possibilidade de correção humana.

</details>

## Aula 12.2 — Avaliar a proposta

Apresente sua avaliação de modo que outra pessoa possa repeti-la. Identifique o dataset, sua origem, as partições e as configurações. Mostre a quantidade de casos por classe, os erros importantes e as limitações. Um gráfico de acurácia sem contexto não é suficiente.

Se executou apenas a baseline de regras, diga isso. Se usou respostas simuladas, marque-as como simulação. Se fez uma chamada real, registre o modelo e o uso reportado. Essas distinções não diminuem o projeto; tornam sua conclusão confiável e mostram qual etapa ainda falta.

A rubrica considera formulação, política, evidência, economia e reprodutibilidade. Um projeto que reconhece insuficiência de dados pode ser melhor que um projeto que anuncia sucesso com números inventados. Inclua exemplos em que o sistema errou e explique a menor correção proposta, sem ajustar e medir tudo no mesmo conjunto.

### Exemplo resolvido

Relatório honesto: “baseline lexical, 24 exemplos fictícios, 20 acertos; não mede Jev nem representa tráfego de produção”.

### Sua vez

Que informação falta para transformar o relatório do exemplo em evidência de adoção do Jev?

<details>
<summary>Conferir resposta comentada</summary>

Execução real do Jev e alternativas, dados representativos revisados, política calibrada em conjunto separado, métricas finais e custo completo do fluxo.

</details>

## Aula 12.3 — Decidir adoção

A última etapa é uma decisão de projeto. Há três saídas legítimas: continuar com uma implantação limitada, coletar mais dados ou não adotar. A escolha depende de qualidade, custo, cobertura, esforço de revisão e capacidade operacional, não da popularidade do modelo.

Se decidir continuar, limite a primeira rota a uma ação reversível e acompanhe as correções. Se decidir coletar mais dados, diga exatamente qual dúvida falta resolver: uma classe rara, um idioma, um tipo de ambiguidade ou a diferença de custo. Se decidir não adotar, preserve a avaliação para evitar repetir o mesmo experimento sem aprender.

O princípio que atravessa o curso é simples: interpretação probabilística funciona melhor dentro de software que conhece seus limites. Modelos ajudam a julgar; critérios e evidências permitem avaliar; código restringe a execução; pessoas assumem as decisões que exigem responsabilidade. Uma arquitetura bem definida vale mais do que uma promessa isolada de velocidade.

### Exemplo resolvido

Decisão possível: manter regras para casos exatos, observar Jev nos demais e exigir revisão até obter evidência suficiente em português.

### Sua vez

Dê uma condição objetiva para cada saída: continuar, coletar mais dados e não adotar.

<details>
<summary>Conferir resposta comentada</summary>

Continuar: metas demonstradas com volume suficiente. Coletar: resultado inconclusivo em classes importantes. Não adotar: qualidade ou custo total não justificam a mudança após teste adequado.

</details>

[Voltar ao índice](../README.md)
