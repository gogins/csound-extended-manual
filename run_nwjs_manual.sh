#!/bin/bash
# Modify paths if needed for your system.
export SSDIR=$SSDIR:/home/mkg/csound-extended-manual/docs/html/examples
~/nwjs/nw --context-mixed --experimental-modules --alsa-input-device=plughw:1,0 --alsa-output-device=plughw:1,0 --device-scale-factor=2 docs
