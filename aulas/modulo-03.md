# Módulo 3 — Confiança e erro

Usar incerteza sem transformá-la em autorização automática.

## Aula 3.1 — Probabilidade e confidence

Em Choice, a distribuição informa um valor para cada alternativa. O campo confidence resume uma propriedade dessa distribuição segundo a implementação do fornecedor. Não presumimos que seja igual à maior probabilidade. Ao registrar um resultado, guardamos os dois campos com nomes distintos.

Uma terceira ideia é o intervalo estatístico de uma taxa medida. Se revisarmos um conjunto de previsões e contarmos acertos, podemos estimar a taxa e sua incerteza amostral. Esse intervalo depende do experimento e não é o campo confidence recebido de uma chamada. Misturar os conceitos dá uma impressão de precisão que os dados não sustentam.

Calibração é uma propriedade observada em grupos de previsões: valores de probabilidade precisam ser comparados com frequências de resultados corretos. Uma única resposta não comprova que o sistema esteja calibrado. O domínio e o idioma também importam. A política do nosso atendimento deve ser avaliada nos nossos exemplos, não apenas num gráfico genérico.

### Exemplo resolvido

Distribuição fictícia: suporte 0,94; cobrança 0,04; vendas 0,02. Confidence fictícia: 0,91. Nenhum desses valores é um intervalo de confiança da acurácia do sistema.

### Sua vez

Uma tela chama confidence=0,91 de “91% de garantia”. Qual correção deve ser feita?

<details>
<summary>Conferir resposta comentada</summary>

Trocar por uma descrição do campo do modelo e explicar que a decisão pode estar errada. Garantia individual não decorre dessa estatística.

</details>

## Aula 3.2 — Alta confiança, resposta errada

Crie um caso fictício: a pessoa escreve “não quero cancelar; só preciso trocar a data”. O modelo escolhe cancelamento com probabilidade alta. A saída é estruturalmente válida, mas a interpretação falhou na negação. Esse exemplo não precisa ser um benchmark real para revelar uma falha de arquitetura: executar uma ação irreversível apenas porque o número é alto.

Quando um erro acontece, registre o contexto necessário, a pergunta, os critérios e a versão do modelo. Verifique primeiro se a pergunta era ambígua ou se opções importantes estavam ausentes. Corrigir uma instrução pode ser suficiente, mas é necessário retestar um conjunto independente; acertar o caso usado no ajuste não comprova melhoria geral.

Nem todo erro pede uma pergunta mais longa. Às vezes falta uma regra: cancelar exige confirmação explícita, qualquer que seja a classificação. Essa proteção deve existir fora do modelo. A melhor correção costuma preservar o sistema e reduzir a consequência do erro, em vez de adicionar outra sequência ilimitada de julgamentos.

### Exemplo resolvido

Erro fictício: “não quero cancelar” foi classificado como cancelamento. Proteção: a triagem só sugere a fila; cancelamento nunca é executado por ela.

### Sua vez

Proponha uma correção no texto da pergunta e outra no fluxo operacional.

<details>
<summary>Conferir resposta comentada</summary>

Pergunta: distinguir pedido explícito de cancelamento de menção ou negação. Fluxo: exigir confirmação e permissão fora do modelo antes de cancelar.

</details>

## Aula 3.3 — Quando pedir revisão

O próximo passo depende tanto da incerteza quanto do custo de errar. Mostrar uma fila sugerida e apagar uma conta têm consequências diferentes. Não há um limiar universal que torne as duas ações equivalentes. O projeto deve definir quais ações são reversíveis, quais precisam de confirmação e quais ficam somente com pessoas autorizadas.

Uma política inicial pode produzir três resultados: sugerir, pedir mais informação ou encaminhar à revisão. Essa política precisa funcionar também quando o serviço falha, quando a resposta não obedece ao contrato e quando chega uma categoria desconhecida. Nesses casos não devemos inventar uma classificação para manter o fluxo andando.

A revisão humana tem custo e capacidade limitada. Meça quantos eventos ela recebe e quanto tempo leva. Se quase tudo vai para revisão, o ganho pode desaparecer. Se quase nada vai, investigue se os critérios ficaram permissivos. O equilíbrio se escolhe com evidência e com quem responde pela operação.

### Exemplo resolvido

Sugerir suporte é reversível. Confirmar uma data pode exigir validação. Excluir uma conta exige um fluxo próprio de autorização, mesmo com confiança alta.

### Sua vez

Defina o destino de resposta inválida, dado incompleto e pedido de exclusão.

<details>
<summary>Conferir resposta comentada</summary>

Resposta inválida: erro operacional e revisão. Dado incompleto: pedir informação ou revisar. Exclusão: fluxo autorizado e confirmação, sem execução pela triagem.

</details>

[Voltar ao índice](../README.md)
