# cf
Get inputs and outputs for a specific problem on [codeforces](https://www.codeforces.com) or [URI](www.urionlinejudge.com.br/).

![Example](http://i.imgur.com/ZDCb1po.png?1)

# Install

Make sure you have Python installed.
```
python -m pip install git+https://github.com/guilhermeleobas/cf
```

# Version
1.2

# Usage

### get
```
cf get cf550A  # Download inputs and outputs for problem 550A
cf get cf600   # Download inputs and outputs for all problems on contest 600.
cf get uri1400 # URI
```
You can also specify a link to get inputs and outputs.
```
cf get https://www.urionlinejudge.com.br/judge/pt/problems/view/1001
```

### compile
```
cf compile code.cc # Compile code.cc using g++.
cf compile -l c++11 code.cc  # Compile code.cc with g++ 11.
cf compile code.py # nothing will happen.
```

### run/test
Run code.cc with 620A inputs and check if their outputs are correct.
```
cf run code.cc cf620A
```

Or you can run `cf test uri1574.cc` which is a syntactic sugar for `cf run uri1574.cc uri1574`

To get full list of available commands run cf with `--help` flag.

# License
MIT
