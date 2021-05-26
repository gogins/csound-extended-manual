#!/bin/bash
echo "Updating WebAssemby dependencies for csound-extended-manual..."
rm -f csound-extended-wasm-2.0.0.zip*
wget https://github.com/gogins/csound-extended-wasm/releases/download/v2.0.0/csound-extended-wasm-2.0.0.zip
unzip -v csound-extended-wasm-2.0.0.zip
unzip csound-extended-wasm-2.0.0.zip -d docs/
find . -name "*.js" -ls
find . -name "*.wasm" -ls
echo "Finished updating all WebAssembly dependencies for csound-extended-manual."
