#!/bin/bash

npm install
npx webpack build --node-env=public
ssh ajmoon "
cp /opt/stfu/public/assets/latest.json /opt/stfu/latest.bak
"
rsync -av --delete public/ ajmoon:/opt/stfu/public/
ssh ajmoon "
cd /opt/stfu/
python3 latest.py
"
