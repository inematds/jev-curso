from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
modules=json.loads((root/'conteudo/curso.json').read_text())
out=root/'aulas';out.mkdir(exist_ok=True)
for m in modules:
 text=[f'# Módulo {m["number"]} — {m["title"]}',m['goal']]
 for l in m['lessons']:
  text.extend([f'## Aula {l["id"]} — {l["title"]}',*l['body'],'### Exemplo resolvido',l['example'],'### Sua vez',l['exercise'],'<details>\n<summary>Conferir resposta comentada</summary>\n\n'+l['answer']+'\n\n</details>'])
 text.append('[Voltar ao índice](../README.md)')
 (out/f'modulo-{m["number"]:02}.md').write_text('\n\n'.join(text)+'\n')
index=['# Jev na prática','**v1.1.0** · Curso autoral em português: **3 trilhas, 12 módulos, 36 aulas e oito laboratórios**.','As aulas e materiais estão disponíveis abaixo em Markdown. A publicação em HTML aguarda a escolha do formato visual v5 ou v2. Nenhum dado recebido para análise é publicado.','[Aplicação e guia](https://inematds.github.io/jev/guia/) · [Laboratório de dez casos](https://inematds.github.io/jev/app/)','## Comece por aqui','Percurso conceitual: módulos 1–8, sem exigir código. Percurso técnico: módulos 9–12, com noções de JSON, terminal e Python. Estimativa de 18 horas incluindo exercícios e projeto; a leitura isolada é mais curta.']
for t,start in [('Entender',0),('Aplicar',4),('Construir e avaliar',8)]:
 index.append('## Trilha — '+t)
 for m in modules[start:start+4]:index.append(f'- [Módulo {m["number"]} — {m["title"]}](aulas/modulo-{m["number"]:02}.md)')
index.extend(['## Laboratórios','[Materiais, atividades e gabaritos](materiais/README.md) · [Projeto final](materiais/projeto-final.md)','## Como estudar','Leia a situação, resolva o exercício antes de abrir a resposta e anote onde faltou informação. Nos laboratórios, diferencie dado fictício, resposta simulada e inferência real. Nenhuma simulação comprova desempenho do Jev.','## Limites e referências','Curso educacional independente. Casos clínicos, jurídicos e financeiros são fictícios e supervisionados. Não há diagnóstico, aprovação contratual ou transação automática. A tarifa usada nos exercícios foi consultada em 18/09/2026; confira atualizações na [documentação TypeSafe](https://docs.typesafe.ai/models).','## Manutenção','A fonte autoral das aulas fica em `conteudo/curso.json`. Para regenerar Markdown: `python3 scripts/export_markdown.py`. O plano pedagógico original permanece em `planejamento/`.'])
(root/'README.md').write_text('\n\n'.join(index)+'\n')
print('12 módulos Markdown exportados a partir das 36 aulas autorais.')
