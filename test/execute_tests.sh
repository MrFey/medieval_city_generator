#!/bin/bash
#-- bash-version: 3  --#

echo "[*] launching block test"
python3 block_test.py 2> /dev/null
echo "[*] launching castle test"
python3 castle_test.py 2> /dev/null
echo "[*] launching city_final test"
python3 city_final_test.py 2> /dev/null
echo "[*] launching city test"
python3 city_test.py 2> /dev/null
echo "[*] launching field test"
python3 field_test.py 2> /dev/null
echo "[*] launching house test"
python3 house_test.py 2> /dev/null
echo "[*] launching lake test"
python3 lake_test.py 2> /dev/null
echo "[*] launching land test"
python3 land_test.py 2> /dev/null
echo "[*] launching district test"
python3 district_test.py 2> /dev/null


echo "[+] Launch the notebook to see all the results"
echo "      --> python3 -m jupyter notebook notebook/result_viewer.ipynb"
