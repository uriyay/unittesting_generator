#!/bin/sh

python ../unittesting_generator.py ./config.py > ./test.py
python ./test.py
