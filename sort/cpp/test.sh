#!/usr/bin/env bash
set -euo pipefail

CPP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${CPP_DIR}/build"
BUILD_TYPE="${BUILD_TYPE:-Release}"
CONAN_ENV_NAME="${CONAN_ENV_NAME:-conan}"
export CONAN_HOME="${CONAN_HOME:-${CPP_DIR}/.conan2}"

find_conda() {
  local candidates=()

  if [[ -n "${CONDA_EXE:-}" ]]; then
    candidates+=("${CONDA_EXE}")
  fi

  if command -v conda >/dev/null 2>&1; then
    candidates+=("$(command -v conda)")
  fi

  candidates+=(
    "${HOME}/miniconda3/bin/conda"
    "${HOME}/anaconda3/bin/conda"
    "${HOME}/miniforge3/bin/conda"
    "${HOME}/mambaforge/bin/conda"
    "/opt/homebrew/Caskroom/miniconda/base/bin/conda"
    "/usr/local/Caskroom/miniconda/base/bin/conda"
  )

  local candidate
  for candidate in "${candidates[@]}"; do
    if [[ -x "${candidate}" ]]; then
      echo "${candidate}"
      return 0
    fi
  done

  return 1
}

detect_conan() {
  if command -v conan >/dev/null 2>&1; then
    CONAN_CMD=(conan)
    return 0
  fi

  if [[ -n "${CONDA_PREFIX:-}" && -x "${CONDA_PREFIX}/bin/conan" ]]; then
    CONAN_CMD=("${CONDA_PREFIX}/bin/conan")
    return 0
  fi

  local conda_bin
  if ! conda_bin="$(find_conda)"; then
    return 1
  fi

  local env_name
  for env_name in "${CONAN_ENV_NAME}" "${CONDA_DEFAULT_ENV:-}"; do
    if [[ -n "${env_name}" ]] && "${conda_bin}" run -n "${env_name}" conan --version >/dev/null 2>&1; then
      CONAN_CMD=("${conda_bin}" run -n "${env_name}" conan)
      return 0
    fi
  done

  return 1
}

if ! detect_conan; then
  echo "Unable to find Conan. Install it directly or create a conda env named '${CONAN_ENV_NAME}'." >&2
  exit 1
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
