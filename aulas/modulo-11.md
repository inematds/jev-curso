# Módulo 11 — Operar e observar

Preparar logs, acompanhamento e retorno sem perder controle da operação.

## Aula 11.1 — Observar antes de automatizar

Modo de observação significa que a nova etapa calcula uma sugestão, mas o fluxo anterior continua responsável pela decisão. Assim podemos comparar o comportamento com a operação real sem aplicar automaticamente os erros do piloto.

Registre concordâncias e desacordos. Revisar somente desacordos não basta, porque humano e modelo podem concordar numa resposta errada. Inspecione também uma amostra de concordâncias. Observe o volume de cada classe e as mensagens que não cabem na taxonomia.

Defina a saída dessa fase antes de começar. Precisão, cobertura, custo, tempo de revisão e ausência de falhas de integração podem fazer parte dos critérios. Se as metas não forem demonstradas, mantenha a observação ou encerre o teste. Automatizar porque “já está há uma semana rodando” não é um critério de qualidade.

### Exemplo resolvido

A equipe recebe a fila sugerida ao lado do encaminhamento atual. Nenhuma mudança externa acontece apenas pela resposta do modelo.

### Sua vez

Um piloto teve poucos eventos da classe cobrança. É suficiente liberar todas as filas?

<details>
<summary>Conferir resposta comentada</summary>

Não necessariamente. Pode faltar evidência nessa classe. Coletar mais exemplos ou limitar a liberação às rotas efetivamente avaliadas.

</details>

## Aula 11.2 — Registrar e entender falhas

Um log útil liga o evento à versão da pergunta, à política e ao modelo usado. Também registra tempo, tokens, resultado e eventual correção. Sem essas informações, é difícil saber se uma mudança de comportamento veio do modelo, do contexto ou de uma alteração no código.

Não confunda rastreabilidade com guardar tudo para sempre. Minimize dados, limite acesso e defina retenção conforme o ambiente real. Para relatórios públicos, use exemplos fictícios ou autorizados. Credenciais nunca entram no log.

Ao corrigir um erro, procure a menor proteção suficiente. Campo ausente pode pedir validação; duplicata pode pedir idempotência; loop pode pedir um teto; decisão incorreta pode pedir critérios mais claros e novo teste. A categoria da falha ajuda: qualidade do julgamento, preparação do contexto, contrato, rede ou política operacional.

### Exemplo resolvido

Evento 42: pergunta v2, política v1, modelo fixado, resposta válida, sugestão corrigida de vendas para suporte. O texto sensível fica fora do relatório público.

### Sua vez

Um retry processa duas vezes o mesmo ticket. Reescrever a pergunta resolve?

<details>
<summary>Conferir resposta comentada</summary>

Não. A correção é de execução: identificador idempotente e controle de duplicatas, com teste que reproduza o retry.

</details>

## Aula 11.3 — Atualizar ou voltar atrás

Um alias de modelo pode apontar para uma nova versão sem mudar a sua requisição. Isso facilita atualizações, mas dificulta atribuir variação quando limiares foram ajustados para uma versão anterior. Registre o identificador resolvido e fixe versões nos experimentos que precisam ser reproduzidos.

Antes de trocar a versão em operação, rode o conjunto de avaliação e compare os erros. Uma média melhor pode esconder regressão numa classe importante. Se a política depender de confidence, verifique novamente os limiares e a cobertura.

Tenha uma forma simples de desativar a nova etapa e voltar ao fluxo anterior. O retorno não deve exigir reconstruir a aplicação. Critérios de suspensão incluem erro relevante, indisponibilidade persistente e custo inesperado. Atualizar é uma mudança controlada, não apenas substituir um nome na configuração.

### Aprofundamento da versão 1.2.0

Para triagem de código, separe comentário correto de comentário útil. O classificador pode apontar um teste enfraquecido, mas testes e análise estática continuam necessários. Amostre também o que o filtro descartou para descobrir falsos negativos. Pratique no L10.

### Exemplo resolvido

Nova versão chega: avaliar com as mesmas perguntas e dados reservados; revisar métricas por classe; liberar gradualmente ou manter a versão anterior.

### Sua vez

O que registrar para reproduzir uma decisão depois de uma atualização?

<details>
<summary>Conferir resposta comentada</summary>

Modelo resolvido, versão das perguntas e critérios, versão da política e identificação do contexto autorizado usado no evento.

</details>

[Voltar ao índice](../README.md)
