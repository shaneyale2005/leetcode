#!/usr/bin/env bash
set -euo pipefail

CPP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${CPP_DIR}/build"
BUILD_TYPE="${BUILD_TYPE:-Release}"
export CONAN_HOME="${CONAN_HOME:-${CPP_DIR}/.conan2}"

if command -v conan >/dev/null 2>&1; then
  CONAN_CMD=(conan)
else
  CONAN_CMD=(conda run -n conan conan)
fi

if ! "${CONAN_CMD[@]}" profile path default >/dev/null 2>&1; then
  "${CONAN_CMD[@]}" profile detect --force
fi

"${CONAN_CMD[@]}" install "${CPP_DIR}" \
  --output-folder="${BUILD_DIR}" \
  --build=missing \
  -s build_type="${BUILD_TYPE}"

cmake -S "${CPP_DIR}" -B "${BUILD_DIR}" \
  -DCMAKE_TOOLCHAIN_FILE="${BUILD_DIR}/conan_toolchain.cmake" \
  -DCMAKE_BUILD_TYPE="${BUILD_TYPE}"
cmake --build "${BUILD_DIR}"
"${BUILD_DIR}/test"
