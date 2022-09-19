# STFU

Welcome to the Securities Transactions Fluctuations Understander!

This is a tiny JEMSCI app that understands fluctuations in securities transactions.
 
### Local development

A few things you're going to need to install if you haven't yet:

```bash
sudo apt install jq postgresql-client redis-tools 
curl -sL https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh -o install_nvm.sh
bash install_nvm.sh
source ~/.bash_profile
nvm install 16.13.0 # (yes, not v17 - it has a problem with OpenSSL)
npm install -g npx
```

If you want to work on the front-end locally, simply install node:
```
brew update
brew install node
npm install
```

And then run webpack:
```
make serve
```

And visit http://localhost:8000/ in your browser.
