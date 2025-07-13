#!/bin/bash
set -e
mkdir -p dist
cp -r site/* dist/
# Copy markdown sources so pages can load them
cp *.md dist/
