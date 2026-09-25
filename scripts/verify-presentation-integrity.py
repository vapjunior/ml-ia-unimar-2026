#!/usr/bin/env python3
"""Verifica os arquivos protegidos das apresentações das Unidades 1 e 2."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

IMMUTABLE_FILES = {
    "Unidade 1": {
        "css/custom.css": "20607ecc28571aee1dbdf335e88a6f061a98b843578d6d454317d3701418b904",
        "js/slides.js": "cd001b0523072e3411d8a81192a2ee1901e86300b2d94012727891c0f266c062",
        "README.md": "aeb785de67bb3a9f669a024b03135581c00b85117802f9fc4a2625b045cd6bb6",
        "REFERENCIAS.md": "6474d050ca014ed2512509271ad0d56e68e18fc1868c59b0ca8256e49c605c03",
    },
    "Unidade 2": {
        "css/custom.css": "0d7e269135ba3c87bc73fc0136d115f1f69659e16bac5042de2759dd53e2e303",
        "js/slides.js": "d7996e6ba26a045ea8694e440f73e73256ecb007f3849e2424a42e44f8b265c1",
        "README.md": "b259dd9d84822878f3972ddeb17629807219217d725003809f8fab188f52233e",
        "REFERENCIAS.md": "86425599ff6ef61b897a2ce4ceb91a534079342557fd1cac7190d7b676b4cf78",
    },
}

PRESENTATIONS = {
    "Unidade 1": {
        "directory": "unidade-1",
        "sections": 53,
        "slides_sha256": "e938e752fbbf1d17a836f21e00aec3ca3539c7f937f447d782a969af7892a15b",
    },
    "Unidade 2": {
        "directory": "unidade-2",
        "sections": 67,
        "slides_sha256": "7e39c98217d44fe4a564dc2ad919d009a753614fa4a177dd0ff7891dd55ab4f2",
    },
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(unit: str, path: Path, detail: str) -> None:
    relative_path = path.relative_to(ROOT)
    print(f"ERRO: {unit} — {relative_path}: {detail}", file=sys.stderr)


def verify_immutable_files() -> int:
    errors = 0
    for unit, files in IMMUTABLE_FILES.items():
        directory = PRESENTATIONS[unit]["directory"]
        for relative_path, expected_hash in files.items():
            path = ROOT / str(directory) / relative_path
            if not path.is_file():
                fail(unit, path, "arquivo ausente")
                errors += 1
                continue

            actual_hash = sha256(path.read_bytes())
            if actual_hash != expected_hash:
                fail(
                    unit,
                    path,
                    f"SHA-256 divergente; esperado {expected_hash}, obtido {actual_hash}",
                )
                errors += 1
    return errors


def verify_presentations() -> int:
    errors = 0
    for unit, expected in PRESENTATIONS.items():
        path = ROOT / str(expected["directory"]) / "index.html"
        if not path.is_file():
            fail(unit, path, "arquivo ausente")
            errors += 1
            continue

        html = path.read_bytes()
        first_section = html.find(b"<section")
        last_section_end = html.rfind(b"</section>")
        if first_section == -1 or last_section_end == -1 or last_section_end < first_section:
            fail(unit, path, "região de slides não encontrada")
            errors += 1
            continue

        last_section_end += len(b"</section>")
        slide_region = html[first_section:last_section_end]
        actual_hash = sha256(slide_region)
        expected_hash = str(expected["slides_sha256"])
        if actual_hash != expected_hash:
            fail(
                unit,
                path,
                f"SHA-256 da região de slides divergente; esperado {expected_hash}, obtido {actual_hash}",
            )
            errors += 1

        actual_sections = len(re.findall(br"<section(?:\s|>)", html))
        expected_sections = int(expected["sections"])
        if actual_sections != expected_sections:
            fail(
                unit,
                path,
                f"contagem de <section> divergente; esperado {expected_sections}, obtido {actual_sections}",
            )
            errors += 1
    return errors


def main() -> int:
    errors = verify_immutable_files() + verify_presentations()
    if errors:
        print(f"Verificação de integridade falhou com {errors} divergência(s).", file=sys.stderr)
        return 1

    print("Integridade preservada: 8 arquivos imutáveis conferidos.")
    print("Unidade 1: região de slides preservada; 53 seções.")
    print("Unidade 2: região de slides preservada; 67 seções.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
