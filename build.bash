#!/bin/bash
echo "Started build of csound-extended-manual..."
cd manual
git stash
git checkout master
git pull
make clean
make html-dist
python2 makeframes.py
cd ..
cp -rf manual/html docs/
python create_playable_csound_manual.py
git add docs/
git commit -a -m "Fresh build and commit."
echo "Check with local Web server before pushing."
python3 -m http.server -d docs/ 5103
# git push
echo "Finished build of csound-extended-manual."
