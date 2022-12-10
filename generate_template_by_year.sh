#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No args supplied"
    echo "Example: ./generate_template_by_year 2022"
fi
year=$1
mkdir -p "./aoc${year}/riddles"
mkdir "./aoc${year}/inputs"
echo "./aoc${year}/inputs"

for riddle_num in {1..25} ; do
  cp "./common/template.py" "./aoc${year}/riddles/day${riddle_num}.py"
done