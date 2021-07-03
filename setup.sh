#!/bin/bash
#-- bash-version: 3  --#

echo "Make sure you are in a virtual env (python3 -m venv venv ; source venv/bin/activate) "
echo "[*] installing python dependencies..."
python3 -m pip install -r requirements.txt
echo "[+] ready to go"

