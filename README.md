# backgroundr
A simple way to create backgrounds for your computer with custom colors and text.

## Requirements
Currently Backgroundr only works on *nix machines and requires python3 to run.

## Installation
Clone this repository and then run:
```
pip install -r requirements.txt
```

## Usage
Modify the settings in ```settings.py``` to choose your screen size and the output directory of your backgrounds, as well as your font.  Next, you simply need to use:  
```
python cli.py RED GREEN BLUE FILE_NAME QUOTED_TEXT
```
Where ```RED```, ```GREEN```, and ```BLUE``` are all integers between 0 and 255 that represent the amount of the particular color, ```FILE_NAME``` is the name you would like your background to be stored as, and ```QUOTED_TEXT``` is the text you would like to have appear on your background (in quotes).  

Your background will be created and saved in the output directory.
