# Agente de Inteligência de Mercado XS5

Ambiente de trabalho para consumo interno e governado da plataforma **XS5 Mercado**, destinado a análises, estudos, diagnósticos e relatórios para profissionais autorizados da Caixa Consórcio.

O agente consumidor tem como objetivo transformar dados certificados e evidências documentadas em respostas úteis e auditáveis sobre o mercado de consórcios, seus participantes e seu contexto econômico. Cada conclusão deve permitir identificar a fonte, o período, a unidade, a cobertura e as limitações que a sustentam.

**Estado atual:** este repositório contém documentação operacional, inventário de fontes, estrutura para arquivos locais e um verificador de integridade. As capacidades analíticas descritas aqui definem o mandato do agente consumidor; ainda não existe neste repositório uma aplicação que as execute automaticamente. O runtime permanece congelado por R109, conforme a governança registrada na coleta.

## Sumário

- [Objetivo e público](#objetivo-e-público)
- [Funcionalidades e capacidades](#funcionalidades-e-capacidades)
- [Fontes e autoridade](#fontes-e-autoridade)
- [Fluxo de atendimento](#fluxo-de-atendimento)
- [Qualidade e limites](#qualidade-e-limites)
- [Entregas esperadas](#entregas-esperadas)
- [Estado da implementação](#estado-da-implementação)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Preparação e uso](#preparação-e-uso)
- [Integridade e rastreabilidade](#integridade-e-rastreabilidade)
- [Segurança e governança](#segurança-e-governança)
- [Versionamento](#versionamento)
- [Documentação complementar](#documentação-complementar)

## Objetivo e público

O projeto apoia a leitura estruturada do mercado de consórcios, combinando indicadores quantitativos, sinais qualitativos e contexto econômico dentro das regras do corpus XS5. Busca reduzir o esforço de localizar e interpretar informações, preservando a semântica dos indicadores e a rastreabilidade das respostas.

O público previsto inclui profissionais internos autorizados de inteligência, planejamento, dados e demais áreas de negócio da Caixa Consórcio. O acesso às fontes e às entregas depende das permissões corporativas aplicáveis.

Os resultados esperados são:

- Diagnósticos sobre evolução do mercado e diferenças entre participantes, segmentos e regiões, quando esses recortes existirem nas fontes certificadas.
- Comparações reproduzíveis, com critérios explícitos de período, universo, unidade e cobertura.
- Estudos que contextualizem indicadores com evidências qualitativas e informações econômicas.
- Relatórios que distingam fatos observados, associações, hipóteses, cenários e projeções externas.
- Respostas que esclareçam quando uma pergunta não pode ser atendida pela cobertura disponível.

## Funcionalidades e capacidades

As funcionalidades abaixo representam o escopo de consumo documentado. Sua execução exige acesso autorizado às fontes correntes, validação da release e ferramentas de análise adequadas. A presença dos arquivos locais não implementa automaticamente essas funções.

| Capacidade | Finalidade | Condições de uso |
| --- | --- | --- |
| Descoberta de informações | Localizar conceitos, objetos, superfícies e linhagem pelo `ai_ready` | Confirmar a origem no pacote certificado; o índice é auxiliar |
| Análise quantitativa | Examinar séries, indicadores e participação de mercado no Mart | Respeitar definições E056, grão, unidade, período e cobertura |
| Comparação competitiva | Comparar participantes e sua evolução | Explicitar universo, residual, cobertura e limitações dos rankings |
| Recortes geográficos e setoriais | Explorar diferenças nas superfícies certificadas e Research Views | Não presumir disponibilidade de todos os indicadores em todos os recortes |
| Análise financeira e de taxas | Consultar as superfícies financeiras, imobiliárias e de taxas previstas nas Research Views | Preservar a diferença entre taxa contratual e receita contábil |
| Complementação com ABAC | Consultar métricas e séries complementares com origem própria | Não substituir séries BCB nem unir entidades por semelhança de nome |
| Contexto qualitativo E072 | Organizar sinais por entidade, data, edição, página e fonte | Menções são evidência contextual; não medem desempenho |
| Contexto econômico E083 | Apoiar interpretações sobre macroeconomia, imóveis, veículos leves e pesados | Preservar provedor, dataset e vintage; explicitar premissas de cenários |
| Ofertas UOTZ | Comparar ofertas observadas nos Books | Usar a mesma coorte de painel, perfil de ticket, segmento e participante |
| Relatórios | Consolidar achados, método, fontes e limitações | Persistir saídas próprias em diretórios autorizados |
| Consulta de governança | Consultar atividades, riscos e decisões na WBS | Reler a WBS nativa; a exportação local não determina o estado atual |

### Exemplos de perguntas dentro do escopo

- Como evoluiu a participação de determinado participante nos períodos certificados?
- Quais diferenças aparecem entre segmentos ou regiões disponíveis no corpus?
- Quais sinais qualitativos foram registrados sobre uma entidade e em quais fontes?
- Como interpretar uma mudança observada à luz do contexto econômico, separando evidência de hipótese?
- Quais ofertas UOTZ são comparáveis dentro de uma mesma coorte?
- Que lacunas de cobertura impedem uma comparação solicitada?

Esses exemplos não garantem disponibilidade de todos os indicadores, entidades ou períodos. O alcance de cada resposta depende da release verificada na sessão. Recomendações comerciais devem ser produzidas somente quando solicitadas.

## Fontes e autoridade

O Google Drive oficial é a origem governada do corpus. Este workspace conserva referências e snapshots locais para apoiar o trabalho; as decisões de consumo dependem das fontes oficiais.

| Ordem | Fonte | Papel |
| --- | --- | --- |
| 1 | `XS5_CONSUMER_CURRENT.md` | Identifica release autorizada, componentes, IDs, hashes e restrições |
| 2 | Contrato de Consumo XS5 V3 | Define acesso, interpretação, comparabilidade e classificação das conclusões |
| 3 | Pacotes certificados de origem e E056 | Sustentam valores, fórmulas, unidades, universos e definições dos indicadores |
| 4 | Research Views correntes | Oferecem superfícies derivadas para facilitar leituras analíticas |
| 5 | `ai_ready` corrente | Auxilia a descoberta de conceitos e a navegação pela linhagem |
| 6 | Evidências e QA específicos | Apoiam auditoria e resolução de divergências |

A WBS nativa determina o estado de atividades, marcos, riscos e decisões. O CURRENT determina o que está distribuído e pode ser consumido. Cada documento tem uma função própria nessa governança.

### Referência da coleta local

| Campo | Valor registrado |
| --- | --- |
| Data da coleta | 12/11/2026 |
| Release Consumer | `XS5_CONSUMER_V2.10_20260925` |
| Manifesto | `2.10.1` |
| Patch | F01, de 28/09/2026 |
| Contrato | V3 |
| Inventário | 18 arquivos, incluindo documentos locais recebidos |

Esses valores descrevem a coleta documentada. **Antes de cada análise material, reler o CURRENT ao vivo e reconciliar as fontes necessárias.** A cópia local e a data deste README não comprovam que a release continua vigente.

A seleção inclui CURRENT, contrato, índice de Research Views, Mart, E052, E072, E083, ABAC, Research Views v1/v2/UOTZ, `ai_ready`, exportações E056/E047/WBS, dicionário de entidades e documentos locais recebidos. É uma coleta seletiva; não é um espelho integral do Drive. RAWs, históricos de rollback, DEV/RC e runtime não integram essa coleta.

## Fluxo de atendimento

1. **Definir a pergunta:** identificar indicador, entidade, segmento, região, período, universo e comparação pretendida.
2. **Validar a release:** ler o CURRENT ao vivo, registrar release e contrato e identificar os pacotes aplicáveis. Se não for possível confirmar a identidade corrente, interromper a análise dependente dessa confirmação.
3. **Consultar a semântica:** verificar definições, fórmulas, unidades e restrições no contrato e no catálogo canônico.
4. **Localizar a superfície:** usar índices auxiliares e seguir a linhagem até a origem certificada.
5. **Validar a comparação:** conferir chaves de entidade, grão, período, universo, coorte, vintage, disponibilidade temporal e cobertura.
6. **Consultar os dados:** selecionar observações compatíveis e registrar filtros e identificadores de origem.
7. **Analisar e contextualizar:** aplicar agregações permitidas, distinguindo resultados quantitativos, sinais contextuais e hipóteses explicativas.
8. **Revisar a qualidade:** reconciliar totais e unidades e avaliar lacunas e limitações materiais.
9. **Entregar:** apresentar achados, método, fontes, classificação das conclusões e eventuais abstenções.
10. **Persistir a saída:** salvar rascunhos ou relatórios próprios nos destinos autorizados, preservando as fontes oficiais.

Esse fluxo descreve o procedimento de consumo. Ainda não está implementado como orquestrador automático neste repositório.

## Qualidade e limites

### Regras gerais de interpretação

- **Ausência não é zero:** preservar `NULL`, supressões e lacunas; não preencher séries por interpolação ou extrapolação silenciosa.
- **Comparabilidade exige evidência:** nomes semelhantes de indicadores ou entidades não demonstram equivalência.
- **Unidades acompanham os valores:** taxas e outras grandezas não aditivas não devem ser somadas como contagens.
- **Referência e disponibilidade têm datas próprias:** respeitar vintage, revisões e `available_at`, especialmente em análises retrospectivas.
- **Associação não demonstra causalidade:** explicações econômicas devem ser identificadas como hipóteses quando não houver sustentação causal.
- **Novos indicadores são exploratórios:** proxies, scores e classificações dependem de certificação antes de serem apresentados como certificados.

### Restrições do corpus documentado

| Tema | Tratamento obrigatório |
| --- | --- |
| Market share | Na coleta, certificado até 2026T1; 2026T2 observado com cobertura incompleta. Revalidar antes de usar |
| MKT001 | `market_total_kpis` armazena mil cotas; `market_trimestre` armazena contagem física. Conversão exige reconciliação explícita e documentada |
| ABAC e BCB | Preservar métricas e universos próprios; `EXACT_CNPJ_CONFIRMED` é o único join forte autorizado |
| COSIF | Considerar a quebra de comparabilidade em 2025 |
| Cancelamentos | Cotas excluídas são estoque; não equivalem a fluxo puro de cancelamentos |
| Taxa e receita de administração | Taxa contratual média do 2080 e receita contábil COSIF em reais são grandezas distintas |
| Rankings | Considerar o viés de sobrevivência do Top 10 atual e a cobertura dos participantes observados |
| E072 | Menções não comprovam desempenho, investimento ou causalidade; contexto posterior não explica retroativamente um resultado |
| UOTZ | Comparar painel, perfil de ticket, segmento e participante compatíveis; manter taxas variáveis em mínimo/máximo/valor original |
| Lacunas UOTZ | Meses sem Book permanecem ausentes; não inferir meses nem pontos médios de intervalos |
| Previsões | Modelos não promovidos e projeções externas não podem ser apresentados como forecast validado XS5 |

Quando uma informação estiver ausente, sem certificação ou sem comparabilidade suficiente, a resposta deve declarar a limitação e evitar substituir silenciosamente a fonte ou o período.

## Entregas esperadas

Cada entrega analítica deve permitir reproduzir a seleção dos dados e compreender o alcance da conclusão.

| Informação | Conteúdo esperado |
| --- | --- |
| Pergunta e data | Solicitação atendida, identificador quando disponível e data da análise |
| Release e contrato | Identidade verificada no CURRENT e versão do contrato |
| Fontes | Superfícies, pacotes, IDs e hashes quando aplicáveis |
| Recorte | Entidade, segmento, região, período, universo, coorte e filtros |
| Método | Agregações, comparações e conversões explicitamente aplicadas |
| Temporalidade | Vintage, revisão e disponibilidade quando relevantes |
| Cobertura | Certificação, lacunas, residual e limites de comparação |
| Achados | Resultados sustentados pelas fontes, com unidades e períodos |
| Classificação | Natureza epistemológica das conclusões materiais |
| Limitações | Dados indisponíveis, ressalvas e inferências das quais o agente se absteve |

As classes previstas pelo contrato são:

- `OBSERVED_FACT`: fato observado.
- `STATISTICAL_ASSOCIATION` / `ASSOCIATION`: associação descritiva ou estatística.
- `ECONOMIC_HYPOTHESIS`: hipótese econômica explicitamente identificada.
- `CONDITIONAL_SCENARIO`: cenário condicionado a premissas.
- `EXTERNAL_PROJECTION`: projeção de fonte externa.
- `VALIDATED_FORECAST`: previsão de modelo efetivamente validado e promovido.

Um relatório pode organizar seu conteúdo em achados, evolução e diferenças, contexto, hipóteses e limitações. As saídas próprias ficam em `80_Inteligencia_Estrategica/00_Temporarios/` ou `01_Relatorios/`.

## Estado da implementação

| Componente | Situação neste repositório |
| --- | --- |
| Documentação de escopo e regras | Disponível neste README e em `docs/` |
| Inventário local | Disponível em JSON, com origem, caminhos, tamanhos e hashes |
| Verificação de integridade | Implementada em Python, sem dependências externas |
| Snapshots Consumer | Disponíveis no workspace preparado; ignorados pelo Git |
| Diretórios de rascunhos e relatórios | Preparados; conteúdo das saídas ignorado pelo Git |
| Download autenticado automático | Não implementado em script; a coleta foi realizada pelo conector do Drive |
| Consulta analítica e geração automática de relatórios | Não implementadas neste repositório |
| Interface conversacional, API ou dashboard | Não implementados neste repositório |
| Atualização agendada, ingestão e promoção de dados | Não implementadas neste repositório |
| Runtime e deploy | Congelados por R109 no estado documentado; dependem de decisão expressa de governança |

Executar o verificador valida os arquivos locais. Essa execução não inicia um agente, não consulta o Drive e não produz análises de mercado.

## Estrutura do projeto

```text
agente-IM/
├── README.md
├── .gitignore
├── .gitattributes
├── docs/
│   ├── operacao.md
│   ├── repositorio.md
│   └── fontes/
│       └── manifesto_downloads.json
├── scripts/
│   └── verificar_fontes.py
├── data/                              # Corpus local; conteúdo fora do Git
│   ├── README.md                      # Guia versionado do corpus
│   ├── consumer/
│   │   ├── XS5_CONSUMER_CURRENT.md
│   │   ├── contrato/
│   │   ├── catalogo/
│   │   ├── mart/
│   │   ├── abac/
│   │   ├── qualitativo/
│   │   ├── setorial/
│   │   ├── research_views/
│   │   └── ai_ready/
│   └── referencias/
│       ├── governanca/
│       └── dicionarios/
└── 80_Inteligencia_Estrategica/
    ├── 00_Temporarios/                # Rascunhos locais
    └── 01_Relatorios/                 # Entregas locais
```

Os caminhos exatos dos artefatos estão no [inventário](docs/fontes/manifesto_downloads.json). Diretórios ignorados aparecem no workspace após a disponibilização dos arquivos; um clone do Git não os recupera automaticamente.

## Preparação e uso

### Requisitos

- Python **3.11 ou superior**, necessário para `hashlib.file_digest`, utilizado pelo verificador.
- Git para controle de versão.
- Acesso autenticado e autorizado ao Google Drive oficial para obter e revalidar as fontes.
- Espaço para aproximadamente 364 MB da coleta, além do necessário para consultas e saídas.

O verificador utiliza apenas a biblioteca padrão do Python. A pasta `.tools/`, quando presente, contém ferramentas locais auxiliares e não é necessária para executar a validação.

### Em um novo clone

1. Ler este README, o [guia de operação](docs/operacao.md) e o inventário.
2. Obter as fontes por acesso autenticado ao Drive, usando os IDs e URLs registrados. Materiais locais sem ID de Drive precisam ser disponibilizados por seu custodiante autorizado.
3. Preservar o formato original dos arquivos armazenados; exportar planilhas nativas no formato registrado no inventário.
4. Colocar cada artefato no caminho indicado por `path`, preservando os arquivos oficiais no Drive.
5. Executar a verificação:

```powershell
python --version
python scripts/verificar_fontes.py
```

Na coleta completa registrada, a saída esperada é:

```text
OK: 18 arquivos; tamanhos, hashes registrados e CRC validos.
```

O processo retorna código `0` quando as verificações passam e `1` quando detecta os problemas tratados pelo script. Investigar arquivos ausentes ou divergentes antes de consumir os dados.

### Antes de uma análise

Abrir o [CURRENT oficial](https://drive.google.com/file/d/1uvIl9VgAqlIHyE6Z77Nt4yI4cEYxEKOO/view), verificar a release autorizada e ler o contrato indicado. Reconciliar as fontes necessárias à pergunta com essa identidade. Uma mudança de release exige revisar os arquivos aplicáveis e documentar a nova coleta.

## Integridade e rastreabilidade

O arquivo `docs/fontes/manifesto_downloads.json` relaciona os artefatos locais às suas origens.

| Campo | Significado |
| --- | --- |
| `id` e `url` | Identificação e endereço de origem no Drive, quando existentes |
| `title` e `mime_type` | Nome e tipo do artefato, quando registrados |
| `modified_time` | Data de alteração da fonte informada pelo provedor, quando disponível |
| `path` | Caminho relativo esperado no workspace |
| `expected_bytes` | Tamanho esperado do arquivo coletado |
| `sha256` | Hash dos bytes da coleta local |
| `current_sha256` | Hash publicado no CURRENT, quando explicitado para o pacote |
| `origin` | Procedência de documentos recebidos localmente, quando aplicável |

O script verifica a existência dos arquivos e a permanência dos caminhos dentro do projeto, compara tamanhos e hashes registrados e testa o CRC de ZIPs e XLSX. Preserva os pacotes, sem extrair ou executar seus conteúdos.

**Limite da verificação:** tamanho, hash e CRC confirmam integridade em relação ao inventário. Não comprovam currentness no Drive, validade semântica de indicadores, integridade de bancos internos, completude da cobertura ou aprovação de uma análise. Esses controles dependem das fontes e dos procedimentos de governança.

Uma nova exportação de planilha nativa pode produzir bytes diferentes. Revisar a divergência e documentar uma nova coleta quando apropriado. Para pacotes com hash publicado no CURRENT, a correspondência física precisa ser exata; não alterar o hash esperado apenas para fazer a verificação passar.

## Segurança e governança

O corpus é de **uso interno restrito**. Manter fontes, metadados e entregas no perímetro autorizado. O inventário contém informações internas e deve receber proteção compatível.

- Tratar a estrutura oficial XS5 no Drive como somente leitura, incluindo WBS, CURRENT, contratos, dados certificados, manifests e evidências.
- Consumir exclusivamente componentes autorizados pelo CURRENT; data e nome de artefato não tornam DEV/RC ou históricos correntes.
- Preservar origem, licença, temporalidade e linhagem das observações.
- Não criar links públicos nem permissões anônimas para o corpus.
- Gravar saídas próprias somente em temporários e relatórios autorizados.
- Encaminhar novos indicadores e mudanças de semântica ou promoção ao PMO XS5.
- Respeitar R109 para desenvolvimento e deploy e o tratamento governado da continuidade e custódia associado a R120.

A preparação do workspace não altera as fontes oficiais nem representa aprovação para reativar o runtime.

## Versionamento

O Git acompanha documentação, estrutura, script e inventário. Os pacotes em `data/`, os relatórios e temporários, as dependências locais e as credenciais permanecem ignorados conforme `.gitignore`.

Para uma alteração exclusiva do README:

```powershell
git status --short
git diff -- README.md
git diff --check
git add README.md
git diff --cached --check
git diff --cached --stat
git commit -m "Detalha objetivos e capacidades do agente XS5"
```

Quando houver alteração da coleta ou do inventário, executar também `python scripts/verificar_fontes.py`. Não forçar a inclusão de dados ou segredos ignorados. Utilizar repositório privado com acesso aprovado.

Commit local e envio ao remoto são operações distintas. Conferir remoto e branch antes de publicar alterações; o [guia de repositório](docs/repositorio.md) descreve o procedimento de envio e as condições da preparação inicial.

## Documentação complementar

| Documento | Utilidade |
| --- | --- |
| [Guia de operação](docs/operacao.md) | Contexto da coleta, autoridade das fontes e regras de consumo |
| [Guia de repositório](docs/repositorio.md) | Preparação e envio ao Git |
| [Inventário de fontes](docs/fontes/manifesto_downloads.json) | IDs, caminhos, tamanhos e hashes dos arquivos |
| [Guia do corpus local](data/README.md) | Organização e preservação dos snapshots |
| [Verificador de fontes](scripts/verificar_fontes.py) | Implementação da validação física |
| [Pasta oficial no Drive](https://drive.google.com/drive/folders/1rNnn8we1FIDUv7NgtIWrjcSUVwUO0lEG) | Localização das fontes governadas, mediante autorização |

Este README descreve o escopo e a preparação local a partir dos documentos da coleta. CURRENT, contrato, catálogo canônico e WBS oficial continuam sendo as referências para decisões de consumo e operação.
