#!/bin/bash
echo "Started fresh build of csound-extended-manual..."
bash update-dependencies.sh
bash build.sh
echo "Finished fresh build of csound-extended-manual."
