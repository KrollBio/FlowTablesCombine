# FlowTablesCombine
Python script to combine csv tables exported from FlowJo

Author: Kyle Kroll

Affiliation: Reeves Lab - Center for Virology and Vaccine Research, BIDMC/HMS

## Requirements
- Python 3.x

- Pandas

## Installation
Install script to a target location. You can optionally add to your systems path. 

## Usage

```
python FTC.py --input INPUT_DIR --output OUTPUT_FILE --separator [csv][tab]
```

## Extras
This script can be added to unix system paths by placing in a folder, for example `~/Desktop/scripts` and adding this folder to path with:
```
export PATH=~/Desktop/scripts:$PATH
```
Then enabling the script to be executable 
```
sudo chmod a+x ~/Desktop/scripts/FTC.py
```
The script can then be envoked anywhere on your system with 
```
FTC.py -h
```

