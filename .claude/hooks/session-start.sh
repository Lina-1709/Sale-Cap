#!/bin/bash
set -euo pipefail

# Only run in Claude Code cloud sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Python libs for Sales data analysis (Excel/CSV). Idempotent.
pip install --quiet -r requirements.txt
