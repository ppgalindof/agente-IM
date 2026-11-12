# Agente de Inteligencia de Mercado XS5

Workspace de consumo interno do corpus XS5. Esta preparacao organiza documentacao e snapshots; nao implementa nem ativa o runtime congelado por R109.

## Estrutura

| Pasta | Conteudo |
| --- | --- |
| `docs/` | Guia de operacao, inventario de fontes e instrucoes de envio |
| `scripts/` | Verificacao local de integridade dos downloads |
| `data/consumer/` | Snapshots e pacotes Consumer, fora do Git |
| `data/referencias/` | WBS, diretriz e dicionario, fora do Git |
| `80_Inteligencia_Estrategica/00_Temporarios/` | Rascunhos locais |
| `80_Inteligencia_Estrategica/01_Relatorios/` | Relatorios locais |

## Comecar

1. Consultar `docs/operacao.md` e o inventario `docs/fontes/manifesto_downloads.json`.
2. Validar os arquivos com `python scripts/verificar_fontes.py` (Python 3, sem dependencias adicionais).
3. Antes de analisar dados, ler ao vivo o CURRENT e o contrato no Drive. Snapshots nao substituem essa verificacao.
4. Para envio ao repositorio, seguir `docs/repositorio.md`.

Os dados internos, dependencias locais e credenciais ficam fora do versionamento. Nao ha aplicacao executavel nem pipeline de producao neste repositorio inicial.
# agente-IM
