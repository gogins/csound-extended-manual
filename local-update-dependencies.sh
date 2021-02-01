#!/bin/bash
echo "Updating WebAssemby dependencies for csound-examples from my home directory..."

cp -rf ~/csound-extended/WebAssembly/dist-wasm/*.js ./docs/
cp -rf ~/csound-extended/WebAssembly/dist-wasm/*.map ./docs/
cp -rf ~/csound-extended/WebAssembly/dist-wasm/*.wasm ./docs/
cp -rf ~/csound-extended/WebAssembly/dist-wasm/*.js ./docs/examples/
cp -rf ~/csound-extended/WebAssembly/dist-wasm/*.map ./docs/examples/
cp -rf ~/csound-extended/WebAssembly/dist-wasm/*.wasm ./docs/examples/
cp ~/csound-examples/docs/player.html ./docs/

find . -name "*.js" -ls
find . -name "*.wasm" -ls
find . -name "player.html" -ls
echo "Finished updating all WebAssembly dependencies for csound-examples."
