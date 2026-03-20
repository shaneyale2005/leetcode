#!/usr/bin/env bash
set -euo pipefail

CPP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${CPP_DIR}/build"
TOOLCHAIN_FILE="${VCPKG_TOOLCHAIN_FILE:-/Users/shaneyale/Workspace/vcpkg/scripts/buildsystems/vcpkg.cmake}"

cmake -S "${CPP_DIR}" -B "${BUILD_DIR}" -DCMAKE_TOOLCHAIN_FILE="${TOOLCHAIN_FILE}"
cmake --build "${BUILD_DIR}"
"${BUILD_DIR}/test"
