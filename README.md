# cftool
Get inputs and outputs for a specific problem on [codeforces](https://www.codeforces.com) or [URI](www.urionlinejudge.com.br/).

![Example](http://i.imgur.com/ZDCb1po.png?1)

# Install

Make sure you have Python installed.
```
python -m pip install git+https://github.com/guilhermeleobas/cftool
```
Or
```
python -m pip install cftool
```

# Version
1.0.3

# Usage

### get
```
cftool get cf550A  # Download inputs and outputs for problem 550A
cftool get cf600   # Download inputs and outputs for all problems on contest 600.
cftool get uri1400 # URI
```
You can also specify a link to get inputs and outputs.
```
cftool get https://www.urionlinejudge.com.br/judge/pt/problems/view/1001
```

### compile
```
cftool compile code.cc # Compile code.cc using g++.
cftool compile -l c++11 code.cc  # Compile code.cc with g++ 11.
cftool compile code.py # nothing will happen.
```

### run/test
Run code.cc with 620A inputs and check if their outputs are correct.
```
cftool run code.cc cf620A
```

Or you can run `cftool test uri1574.cc` which is a syntactic sugar for `cftool run uri1574.cc uri1574`

To get full list of available commands run cf with `--help` flag.

# License
MIT
