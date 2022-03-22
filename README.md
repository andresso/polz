# Lempel-Ziv with Partial Order

## A Python implementation of the Lempel-Ziv with partial order (POLZ) algorithm 

## How to use

### Getting started
* To download the project follow the instructions bellow:

```
1. git clone https://github.com/andresso/polz.git
2. cd polz
```

### Prerequisites
* The POLZ requires
  * lempel-ziv-complexity 0.2.2
  * matplotlib 3.5.1
  * numpy 1.22.3
* To install the project prerequisites, run the command:
```
$ pip install -r rwquitements.txt
```

### Usage
#### Compress
* To compress a sequence, it is necessary the non-commutative graph:
```
from polz.polz_class import POLZ

polz = POLZ()
# Non-commutativity graph
adj = [
  ["n", "s"],
  ["e", "w"],
]

sequence = "nsenwnweewns" # n, s, e, w, nw, ee, wns -> Complexity = 7
complexity, encoded_dict = polz.encode(sequence, adj)

print(f"Sequence: {sequence}")
print(f"Complexity: {complexity}")
print(f"Encoded dictionary: {encoded_dict}") 
```
#### Decompress
* And to decompress:
```
sequence_eq, _ = polz.decode(encoded_dict)
print(f"Decompressed sequence: {sequence_eq}")
```

### Examples
#### Robot commands
* To run this example, execute:
```
$ python examples/robot_commands/robot_commands.py
```

#### Constrained robot commands
* To run this example, execute:
```
$ python examples/constrained_robot_commands/constrained_robot_commands.py  
```

#### ATM operations
* To execute this example, follow the instructions bellow:
```
1. python examples/atm_operations/generate_atm_operations.py
2. python examples/atm_operations/atm_operations.py
```

### Tests
* To execute all unit tests:
```
$ python -m unittest tests
```
