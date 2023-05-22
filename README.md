# Brain Games

[![Actions Status](https://github.com/zluuba/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-49/actions) 
[![Project Status](https://github.com/zluuba/brain-games/actions/workflows/project-check.yml/badge.svg)](https://github.com/zluuba/brain-games/actions/workflows/project-check.yml) 
[![Maintainability](https://api.codeclimate.com/v1/badges/8f30055514168a104cb1/maintainability)](https://codeclimate.com/github/zluuba/python-project-49/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/8f30055514168a104cb1/test_coverage)](https://codeclimate.com/github/zluuba/python-project-49/test_coverage)


Brain Games includes five math games: 'Parity Check', 'Calculator', 'Greatest Common Divisor', 'Arithmetic Progression' and 'Is it a Simple Number?'. 
This is the **first project** on Python, so it's extremely simple :) <br />
All games are started and played using the terminal. <br />


## Requirements
- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/), version 1.0.0 or higher


## Installation
Clone this repo or download it with pip:
```ch
git clone https://github.com/zluuba/brain-games.git
```
```ch
pip install --user git+https://github.com/zluuba/brain-games.git
```

Install package and dependencies:
```ch
cd brain-games
make install
make build
make package-install
```

## Commands

#### **"Parity Check"** game
Given a number, you must enter "yes" if the number is even and "no" if it's not. <br />
[Demonstration](https://github.com/zluuba/python-project-49#even-game)
```ch
brain-even
```

#### **"Calculator"** game
Given a mathematical expression, you need to calculate it and enter the result. <br />
[Demonstration](https://github.com/zluuba/python-project-49#calculator-game-1)
```ch
brain-calc
```

#### **"The Greatest Common Divisor"** game
Two numbers are given, you need find the greatest common divisor and enter the result [(about GSD)](https://en.wikipedia.org/wiki/Greatest_common_divisor) <br />
[Demonstration](https://github.com/zluuba/python-project-49#greatestcommondivisor-game)
```ch
brain-gcd
```

#### **"Arithmetic Progression"** game
Given an arithmetic sequence in which one number is hidden, you must enter the missing number. <br />
[Demonstration](https://github.com/zluuba/python-project-49#progression-game)
```ch
brain-progression
```

#### **"Is it a Simple Number?"** game
Given a number, you must enter "yes" if the number is prime and "no" if it's not [(about prime numbers)](https://en.wikipedia.org/wiki/Prime_number) <br />
[Demonstration](https://github.com/zluuba/python-project-49#prime-game)
```ch
brain-prime
```


## Demos

### Even Game
[![asciicast](https://asciinema.org/a/h6cIIpEGMbiNajL8XJ02GrOPX.svg)](https://asciinema.org/a/h6cIIpEGMbiNajL8XJ02GrOPX)

### Calculator Game
[![asciicast](https://asciinema.org/a/H00VVTCBDKfmdu3LVuOQPEMza.svg)](https://asciinema.org/a/H00VVTCBDKfmdu3LVuOQPEMza)

### GreatestCommonDivisor Game
[![asciicast](https://asciinema.org/a/hgcLbeJ0WcWTQIHewflnZrFGQ.svg)](https://asciinema.org/a/hgcLbeJ0WcWTQIHewflnZrFGQ)

### Progression Game
[![asciicast](https://asciinema.org/a/PBE94ttXoDZKKZ4EcT5A3vaC7.svg)](https://asciinema.org/a/PBE94ttXoDZKKZ4EcT5A3vaC7)

### Prime Game
[![asciicast](https://asciinema.org/a/rELtozb3KeYL1sz5XDkqLyZhv.svg)](https://asciinema.org/a/rELtozb3KeYL1sz5XDkqLyZhv)
