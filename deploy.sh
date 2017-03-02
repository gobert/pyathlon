#!/bin/bash

# save the DB
mv pyathlon.db mv ..
rm -rf * .git/ .gitignore

# Update the code
git clone https://github.com/gobert/pyathlon.git
mv pyathlon/* .
rm -rf pyathlon/

# restore the DB
mv ../pyathlon.db mv .

# link entr point of the webserver to our entry point
ln server.py flask_app.py
