# RANDOM GENERATORS AND CONTRASTS [MUIA - SIMULATION METHODS]

Implementation of congruential random generator. IMSL.
Using Schrage method to avoid overflow.

> Park, Stephen & Miller, Keith. (1988). Random Number Generators: Good Ones Are Hard to Find. Commun. ACM. 31. 1192-1201. 10.1145/63039.63042.

**Authors**

- Antonio Sejas
- Danielle Pellegrino
- Sergio Cavero

## ======= CREATE A CONGRUENTIAL RANDOM GENERATOR IN PYTHON =======

> You can find our custom development in python in the folder: `/generator-in-python`

## Execute

```
python main.py
```

It will create `random-numbers-sample.txt` with the random numbers list

## Test algorithm

```
python imsl_test.py
```

## ======= STUDY OF RANDOM GENERATOR CONTRASTS WITH TESTU01 =======

> You can find our constrast study in the folder: `/contrasts-with-testu01`

## Requirements

You need to have installed the TestU01 library to be able to compile the code.
http://simul.iro.umontreal.ca/testu01/tu01.html

If you are on Unix or MacOS system, you can try to directly execute the `./muia` application.

## Compilation

After installing the code

```
➜ clang muia.c  -lmylib -lprobdist -ltestu01 -o muia
```

## How to execute

```bin
➜ ./muia
```

---

MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
