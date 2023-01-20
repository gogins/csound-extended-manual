# csound-extended-manual

Michael Gogins<br>
https://github.com/gogins<br>
http://michaelgogins.tumblr.com

## Introduction

This repository hosts, and serves, an online version of the **_Csound Reference 
Manual_** that embeds the csound-extended-wasm build of Csound to play 
examples live in standard Web browsers.

## Usage

This live manual is hosted as GitHub pages at: https://gogins.github.io/csound-extended-manual/indexframes.html.

At this time, Mozilla Firefox runs Csound and plays the examples somewhat more smoothly than Google Chrome.

## Building

Clone this repository.

Change to the `manual` directory.

Pull the latest sources.

Build the manual according to instructions in the `README.md` file. Basically:
```
make clean;make html-dist;python3 makeframes.py
```

Change back to the root directory of this repository. Execute:
```
cp -rf manual/html/ docs/
python create_playable_csound_manual.py
```

## Run locally

Copy the WebAssembly files from csound-extended-wasm into the `docs/examples`
directory here. Execute `python -m http-server` to run a local Web server so 
you can test the manual.

The WebAssembly build of Csound does not currently play examples that are based 
on external assets such as soundfiles, samples, SoundFonts, or text data files.
However, such examples _can_ be played by running the the manual in NW.js using 
[csound.node](https://github.com/gogins/csound-extended-node).

## Update the GitHub pages

Using git, add the entire `docs` directory, commit your updates, and push them.
