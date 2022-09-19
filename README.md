# STFU

Welcome to the Securities Transactions Fluctuations Understander!

This is a tiny JEMSCI app that understands fluctuations in securities transactions.
 
## Local development

A few things you're going to need to install if you haven't yet:

```bash
sudo apt install jq postgresql-client redis-tools 
curl -sL https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh | bash
source ~/.bash_profile
nvm install 16.13.0 # (yes, not v17 - it has a problem with OpenSSL)
npm install -g npx
```

To set up your local environment, simply:
```
make build
```

### Back-end

To work on the back-end locally, simply run flask:
```
make run
```

And visit http://localhost:5000/ in the browser.

### Front-end

To work on the front-end locally, simply run webpack:
```
make serve
```

And visit http://localhost:8000/ in your browser.
