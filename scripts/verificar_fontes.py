"""Verifica bytes locais, SHA-256 e CRC de ZIPs sem extrair ou executar fontes."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / 'docs/fontes/manifesto_downloads.json').read_text(encoding='utf-8'))
    errors = []
    for item in manifest['files']:
        path = (ROOT / item['path']).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append(f"Ausente ou fora do projeto: {item['path']}")
            continue
        expected_size = item.get('expected_bytes')
        if expected_size is not None and path.stat().st_size != int(expected_size):
            errors.append(f"Tamanho divergente: {item['path']}")
        with path.open('rb') as stream:
            actual = hashlib.file_digest(stream, 'sha256').hexdigest()
        for field in ('sha256', 'current_sha256'):
            if item.get(field) and actual != item[field]:
                errors.append(f"{field} divergente: {item['path']}")
        if path.suffix.lower() in ('.zip', '.xlsx'):
            try:
                with zipfile.ZipFile(path) as archive:
                    if archive.testzip() is not None:
                        errors.append(f"CRC invalido: {item['path']}")
            except zipfile.BadZipFile:
                errors.append(f"ZIP invalido: {item['path']}")
    if errors:
        print('\n'.join(errors))
        return 1
    print(f"OK: {len(manifest['files'])} arquivos; tamanhos, hashes registrados e CRC validos.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
