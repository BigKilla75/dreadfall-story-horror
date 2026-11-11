#!/usr/bin/env bash
# Install the pinned OFFICIAL Rojo binary in a Linux development container.
# Studio itself cannot run in this Linux container.
set -euo pipefail

VERSION="7.7.1"
ARCH="$(uname -m)"
case "$ARCH" in
  x86_64|aarch64) ;;
  *) echo "Unsupported Linux CPU architecture: $ARCH" >&2; exit 2 ;;
esac

URL="https://github.com/rojo-rbx/rojo/releases/download/v${VERSION}/rojo-${VERSION}-linux-${ARCH}.zip"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
curl --fail --location --retry 3 --silent --show-error "$URL" --output "$TMP_DIR/rojo.zip"
unzip -q "$TMP_DIR/rojo.zip" -d "$TMP_DIR/out"
BIN="$(find "$TMP_DIR/out" -type f -name rojo -print -quit)"
if [[ -z "$BIN" ]]; then
  echo "Rojo executable not found in downloaded release" >&2
  exit 2
fi
chmod +x "$BIN"
if command -v sudo >/dev/null 2>&1; then
  sudo install -m 0755 "$BIN" /usr/local/bin/rojo
else
  install -m 0755 "$BIN" /usr/local/bin/rojo
fi
rojo --version
python3 scripts/dev.py doctor
