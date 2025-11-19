#!/bin/bash
LECTRUE=${1:-1}
ISSUES=${2:-5}
dir_name="230250329_${LECTRUE}"
mkdir "${dir_name}"
for i in $(seq 1 $ISSUES); do
	py_name="230250329_${LECTRUE}_${i}"
	touch "${dir_name}/${py_name}.py"
done
