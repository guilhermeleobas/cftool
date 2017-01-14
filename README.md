# cf
Get inputs and outputs for a specific problem on [codeforces](https://www.codeforces.com).
# Install

Make sure you have Python installed.
```
python -m pip install git+https://github.com/guilhermeleobas/cf
```

# Version
1.0

# Usage

### get
```
cf get cf550A # Download inputs and outputs for problem 550A
cf get cf600 # Download inputs and outputs for all problems on contest 600.
```

You can also specify a Codeforces link to get inputs and outputs.

### compile
```
cf compile code.cc # Compile code.cc using g++.
cf compile -l c++11 code.cc  # Compile code.cc with g++ 11.
cf compile code.py # nothing will happen.
```

### test
```
cf run code.cc cf620A # will run code.cc with 620A inputs and check if their outputs are correct.
```

To get full list of available commands run cf with --help flag.

# License
MIT
