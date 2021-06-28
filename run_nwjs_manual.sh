#!/bin/bash
# Modify this script if needed for your system.
export SSDIR=$SSDIR:/home/mkg/csound-extended-manual/docs/html/examples
~/nwjs/nw --context-mixed --experimental-modules --alsa-input-device=plughw:2,0 --alsa-output-device=plughw:2,0 --device-scale-factor=2 docs
