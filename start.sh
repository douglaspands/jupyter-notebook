#!/bin/bash

DIR=$(dirname "$0")
cd "$DIR"
source venv/bin/activate
cd ./notebook
jupyter notebook
