# Preparacao para envio

O repositorio local estava sem commits e sem remoto na inspecao inicial. O destino ainda precisa ser informado. Usar repositorio privado com acesso autorizado, considerando a classificacao interna das fontes.

O Git inclui estrutura, documentacao, script e inventario. Os binarios internos em `data/`, relatorios, temporarios, `.tools/` e segredos estao ignorados. O inventario contem metadados internos e deve permanecer no mesmo perimetro autorizado.

Executar na raiz:

```powershell
python scripts/verificar_fontes.py
git status --short
git add .gitignore .gitattributes README.md docs scripts data/README.md 80_Inteligencia_Estrategica
git diff --cached --check
git diff --cached --stat
git commit -m "Organiza workspace XS5 e inventario de fontes"
git remote add origin <URL_DO_REPOSITORIO_PRIVADO>
git push -u origin HEAD
```

Nao forcar a inclusao de `data/`. Em outro ambiente, baixar novamente as fontes pelo conector autenticado do Drive usando os IDs e formatos do inventario. Exports de Sheets podem produzir bytes diferentes em uma nova exportacao; nesse caso registrar uma nova coleta apos revisar a origem. Hashes de pacotes explicitados pelo CURRENT devem coincidir exatamente.
