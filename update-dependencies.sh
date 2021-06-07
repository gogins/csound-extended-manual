#!/bin/bash
echo "Updating all dependencies for csound-extended-manual..."
sudo -k apt-get install -y docbook docbook-xsl xsltproc
echo "Updating all submodules for csound-extended-manual..."
git submodule update --init --recursive --remote
git submodule update --recursive
git submodule status --recursive
cd manual
git stash
git checkout master
git pull
cd ..
echo "Finished updating all submodules for csound-extended-manual..."
echo "Updating WebAssemby dependencies for csound-extended-manual..."
rm -f csound-extended-wasm-2.0.0.zip*
wget https://github.com/gogins/csound-extended-wasm/releases/download/v2.0.0/csound-extended-wasm-2.0.0.zip
unzip -v csound-extended-wasm-2.0.0.zip
unzip csound-extended-wasm-2.0.0.zip -d -f docs/
find . -name "*.js" -ls
find . -name "*.wasm" -ls
echo "Finished updating all WebAssembly dependencies for csound-extended-manual."
echo "Finished updating all dependencies for csound-extended-manual..."
