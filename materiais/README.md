# Laboratórios — material fictício e autoral

Cada arquivo inclui gabaritos para autocorreção. Tente resolver antes de consultar a resposta. Nenhum dataset representa tráfego operacional real.

| Laboratório | Arquivo | Atividade e critério |
|---|---|---|
| L1 — formular | [12 tarefas](l1-formulacao.csv) | Escolher regra, Choice, Noul, Score ou geração e justificar. |
| L2 — hotel | [6 políticas](l2-hoteis.json) | Distinguir dinheiro, crédito, falta de devolução, conflito e insuficiência. |
| L3 — atendimento | [30 tickets](l3-tickets.json) | Classificar filas; comparar com label e explicar divergências. |
| L4 — evidências | [8 pares e 4 cláusulas](l4-evidencias.json) | Identificar apoio e omissão somente no material fornecido. |
| L5 — rotas | [12 tarefas](l5-rotas.json) | Escolher capacidade; definir permissão e limite de tentativa separadamente. |
| L6 — DOM | [5 listas](l6-dom.json) | Selecionar candidato, abster-se ou pedir revisão por permissão. |
| L7 — economia | [Planilha CSV](l7-custos.csv) | Refazer custos e acrescentar fallback, trabalho humano e implantação. |
| L8 — limiares | [10 predições simuladas](l8-predicoes-simuladas.json) | Comparar cobertura e erro ao aceitar confidence ≥0,90 ou ≥0,95. |

## Gabarito comentado do L8

Em ≥0,90: seis aceitos, quatro corretos; cobertura 60%, acurácia entre aceitos 66,67%.
Em ≥0,95: quatro aceitos, três corretos; cobertura 40%, acurácia entre aceitos 75%.
O erro com confidence 0,97 permanece aceito nos dois. Aumentar o limiar não elimina todos os erros. Esses números são inventados para o exercício, não resultados Jev.

## Integração com a aplicação

[Dez casos completos](dez-casos.json) contêm estado, perguntas, critérios, resposta simulada e comentário. O [laboratório web](https://inematds.github.io/jev/app/) permite explorar os mesmos casos.

## Entrega final

Preencha o [modelo de projeto](projeto-final.md). Aprovação sugerida: 75/100 na rubrica, sem apresentar simulação como medição nem atribuir permissões ao modelo. A nota é uma autoavaliação educacional, não uma certificação de segurança operacional.

## Aprofundamento — L9 a L12

Todos incluem situações fictícias e gabaritos.

| Laboratório | Material | Entrega |
|---|---|---|
| L9 — Skills | [Oito pedidos](l9-skills.json) | Selecionar uma skill ou nenhuma; justificar pela intenção. |
| L10 — Código | [Seis situações](l10-comentarios-diff.json) | Separar correção, utilidade e evidência de teste. |
| L11 — Evidências | [Seis passagens](l11-evidencias.json) | Preservar contradições, negações e IDs. |
| L12 — Demos | [Oito alegações](l12-auditoria-demos.json) | Dar veredito e listar a evidência ainda necessária. |

[Vinte casos da aplicação](vinte-casos.json) incluem as três primitivas e perguntas combinadas. O arquivo anterior com dez casos permanece como material inicial. Para prática técnica, use o [guia de experimentos](https://github.com/inematds/jev/blob/main/docs/08-experimentos.md).
