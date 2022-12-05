#!/bin/bash

dates=$(grep -E '(INFO - Running for)|(Ending GECToR)' -B 4 $1 | grep RECEIVED | awk -F ' - ' '{printf "%s\n", $1}')
while read line; do date --date="$line" +"%s"; done <<< "$dates"
