#!/usr/bin/env bash
set -euo pipefail

PY_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

cd "${PY_DIR}"
"${PYTHON_BIN}" -m unittest -v
