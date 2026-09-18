# Laboratórios e avaliação

Todos os datasets e gabaritos abaixo são **entregas planejadas**. Usar dados fictícios nos materiais públicos; os dados operacionais ficam no projeto de aplicação com controles próprios.

| Laboratório | Material a produzir | Exercício | Evidência de conclusão |
|---|---|---|---|
| L1 — formular | 12 situações cotidianas | Escolher regra, Choice, Noul, Score ou geração | Resposta justificada e gabarito comentado |
| L2 — hotel | 6 políticas fictícias de cancelamento | Separar dinheiro, crédito, conflito e omissão | Nenhuma ausência tratada automaticamente como “não” |
| L3 — atendimento | 30 tickets fictícios em português | Rotular fila e suficiência | Matriz manual com divergências explicadas |
| L4 — evidências | 8 pares de afirmação/passagem e 4 cláusulas fictícias | Marcar apoio e pendência de revisão | Trecho de evidência e limite da conclusão |
| L5 — rotas | 12 tarefas com catálogo de modelos/agentes abstratos | Escolher caminho e teto de tentativas | Diagrama sem loops ilimitados nem permissões implícitas |
| L6 — DOM | 5 listas textuais de elementos | Escolher candidato ou abster-se | Distinguir seleção semântica de execução do clique |
| L7 — economia | Planilha editável e cenários | Calcular API, fallback e revisão | Conta corrigida e análise de sensibilidade |
| L8 — avaliação | Predições simuladas com erro de alta confiança | Medir erro e cobertura ao variar limiar | Relatório rotulado como simulação, sem alegação de benchmark |

## Projeto final

Problema: uma equipe recebe tickets e precisa sugerir filas. Entregar taxonomia; cinco exemplos difíceis; perguntas atômicas; política de revisão; diagrama do fluxo; plano de dados e avaliação; orçamento; critérios de operação e retorno.

Percurso sem código entrega planilha e especificação. Percurso técnico adiciona execução no laboratório do repositório de aplicação quando implementado, logs anonimizados e relatório reproduzível. Se não houver acesso real, a execução usa fixture rotulada; não inventar chamadas bem-sucedidas.

## Rubrica de 100 pontos

| Critério | Pontos | Evidência |
|---|---:|---|
| Formulação e opções | 20 | Questões específicas, sem sobreposição indevida, dados insuficientes tratados |
| Política de decisão | 20 | Consequências, revisão, ações permitidas e limites de repetição |
| Evidência e qualidade | 25 | Referência revisada, separação de dados e erros por classe |
| Economia e latência | 15 | Cálculo correto e custos do fluxo completo |
| Reprodutibilidade e comunicação | 20 | Versões, fontes, procedimento e distinção entre simulação e resultado real |

Aprovação proposta: 75 pontos e correção das falhas essenciais. Alegar que confiança garante verdade, apresentar simulação como benchmark ou permitir ação fora da política exige revisão do projeto, independentemente da soma.

## Questões de saída e resposta esperada

1. “Se só há duas opções, o modelo não pode errar?” Pode escolher a alternativa errada.
2. “Noul 0,05 significa pouca confiança?” Significa baixa probabilidade de sim, não um campo confidence.
3. “Falta de confirmação significa não houve agendamento?” Não necessariamente; preservar insuficiência.
4. “10 mil tokens custam US$ 0,0042 nessa tarifa?” Não; US$ 0,00042.
5. “O benchmark externo valida atendimento em português?” Não; precisamos de avaliação no domínio.
6. “Posso enviar screenshot diretamente?” A modalidade documentada é texto; requer etapa anterior.
7. “Escolheu o agente financeiro: pode pagar?” Escolha de rota não concede permissão.
8. “Se o piloto não economizar, o projeto fracassou?” Uma decisão fundamentada de não adotar é resultado útil.
