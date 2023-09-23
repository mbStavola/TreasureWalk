# TreasureWalk

A simple program/game for teaching people how to navigate on the command line.

This script will create a nested directory structure with a flag file that the learner is meant to find using basic command line tools like pwd, cd, find, et al.

You should also make your learner "clean up" the files and directories using rm and rmdir for some added experience.

## Usage

```shell
python3 ./treasure_walk.py
```

There are a few options for configuring the hunt:

```
usage: treasure_walk.py [-h] [-m MAX_DEPTH] [-f MAX_FAKES] [-r]

options:
  -h, --help            show this help message and exit
  -m MAX_DEPTH, --max-depth MAX_DEPTH
                        how deep down the directories can go
  -f MAX_FAKES, --max-fakes MAX_FAKES
                        how many fake directories we will create total
  -r, --random-flag-name
                        makes the flag file name random
```
