#!/bin/bash

echo "Started fresh build of live Csound Reference Manual..."
bash update-dependency-submodules.sh
cd manual
git checkout master
git stash
git pull
make clean
make html-dist
python2 makeframes.py
cd ..
cp -rf manual/html docs/
python create_playable_csound_manual.py
# TODO: Check paths for your system.
bash local-update-dependencies.sh
git add docs/
git commit -a -m "Fresh build and commit."

echo "Check with local Web server before pushing."
python -m http.server -d docs/ 5103

# git push

echo "Finished fresh build of live Csound Reference Manual."
