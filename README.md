Python-based solutions to the Advent of Code 2021

To participate, head over to https://adventofcode.com

# Preface

My aim is to complete as many of the problems as possible using only built-in python packages 🤓

I'm also going to try to avoid stack overflow 😅 - at least outside of the 'how do I do this thing I've done 1000 times before?' questions 🙃

# Getting started

## Installation

1. Install python==3.8.6
1. Create a virtual environment:

   ```
   python -m venv .venv
   ```

1. Install the requirements:
   ```
   python -m pip install -r requirements.txt
   ```

## Environment Variables

The data is downloaded using the package [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data). Follow the instructions there for how to get an access token.

Once you have the token, create a .env file in the project root and assign the token to the variable name `AOC_SESSION`.

Also you'll need to point at your data directory in the .env file, with the variable `DATA_DIR` (relative to the project root)

## Execution

To run the solution for day X:

```
python -m solutions.dayX
```

This will download, ingest and preprocess the data, run the calculations and submit the result! 💪
