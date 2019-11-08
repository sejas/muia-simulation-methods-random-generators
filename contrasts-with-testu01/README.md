# Requirements

You need to have installed the TestU01 library to be able to compile the code.
http://simul.iro.umontreal.ca/testu01/tu01.html

If you are on Unix or MacOS system, you can try to directly execute the `./muia` application.

## Compilation

After installing the code

```
➜ clang muia.c  -lmylib -lprobdist -ltestu01 -o muia
```

# How to execute

```bin
➜ ./muia
```

## RESULTS

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                 Starting SmallCrush
                 Version: TestU01 1.2.3
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


smarsa_BirthdaySpacings test:
-----------------------------------------------
   N =  1,  n = 5000000,  r =  0,    d = 1073741824,    t = 2,    p = 1


      Number of cells = d^t = 1152921504606846976
      Lambda = Poisson mean =      27.1051


----------------------------------------------------
Total expected number = N*Lambda      :      27.11
Total observed number                 : 4987281
p-value of test                       :   eps      *****


-----------------------------------------------
CPU time used                    :  00:00:00.86

Generator state:
 s = 1768507984




***********************************************************
Test sknuth_Collision calling smultin_Multinomial

***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


smultin_Multinomial test:
-----------------------------------------------
   N =  1,  n = 5000000,  r =  0,   d = 65536,   t =  2,
       Sparse =   TRUE

       GenerCell = smultin_GenerCellSerial
       Number of cells = d^t =         4294967296
       Expected number per cell =  1 /  858.99346
       EColl = n^2 / (2k) =  2910.383046
       Hashing =   TRUE

       Collision test,    Mu =      2909.2534,    Sigma =    53.8957

-----------------------------------------------
Test Results for Collisions

Expected number of collisions = Mu    :     2909.25
Observed number of collisions         :     5671
p-value of test                       :   eps      *****

-----------------------------
Total number of cells containing j balls

  j =  0                              :       4289972967
  j =  1                              :          4988658
  j =  2                              :             5671
  j =  3                              :                0
  j =  4                              :                0
  j =  5                              :                0

-----------------------------------------------
CPU time used                    :  00:00:01.09

Generator state:
 s = 33648008




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


sknuth_Gap test:
-----------------------------------------------
   N =  1,  n = 200000,  r = 22,   Alpha =        0,   Beta  = 0.00390625


-----------------------------------------------
Number of degrees of freedom          : 1114
Chi-square statistic                  : 1076.09
p-value of test                       :    0.79

-----------------------------------------------
CPU time used                    :  00:00:00.76

Generator state:
 s = 49433600




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


sknuth_SimpPoker test:
-----------------------------------------------
   N =  1,  n = 400000,  r = 24,   d =   64,   k =   64


-----------------------------------------------
Number of degrees of freedom          :   19
Chi-square statistic                  :   23.93
p-value of test                       :    0.20

-----------------------------------------------
CPU time used                    :  00:00:00.58

Generator state:
 s = 2114271677




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


sknuth_CouponCollector test:
-----------------------------------------------
   N =  1,  n = 500000,  r = 26,   d =   16


-----------------------------------------------
Number of degrees of freedom          :   44
Chi-square statistic                  :   45.37
p-value of test                       :    0.41

-----------------------------------------------
CPU time used                    :  00:00:00.48

Generator state:
 s = 690686278




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


sknuth_MaxOft test:
-----------------------------------------------
   N =  1,  n = 2000000,  r =  0,   d = 100000,   t =  6

      Number of categories = 100000
      Expected number per category  = 20.00


-----------------------------------------------
Number of degrees of freedom          : 99999
Chi-square statistic                  : 2.71e+5
p-value of test                       :   eps      *****


-----------------------------------------------
Anderson-Darling statistic            :    0.99
p-value of test                       :  6.6e-3


-----------------------------------------------
CPU time used                    :  00:00:00.50

Generator state:
 s = 1056183403




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


svaria_WeightDistrib test:
-----------------------------------------------
   N =  1,  n = 200000,  r = 27,  k = 256,  Alpha =      0,  Beta =  0.125


-----------------------------------------------
Number of degrees of freedom          :   41
Chi-square statistic                  :   35.65
p-value of test                       :    0.71

-----------------------------------------------
CPU time used                    :  00:00:00.80

Generator state:
 s = 1583175107




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


smarsa_MatrixRank test:
-----------------------------------------------
   N =  1,  n = 20000,  r = 20,    s = 10,    L = 60,    k = 60


-----------------------------------------------
Number of degrees of freedom          :    3
Chi-square statistic                  :    0.64
p-value of test                       :    0.89

-----------------------------------------------
CPU time used                    :  00:00:00.49

Generator state:
 s = 1384528142




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


sstring_HammingIndep test:
-----------------------------------------------
   N =  1,  n = 500000,  r = 20,   s = 10,   L = 300,   d = 0



Counters with expected numbers >= 10
-----------------------------------------------
Number of degrees of freedom          : 2209
Chi-square statistic                  : 2185.49
p-value of test                       :    0.63

-----------------------------------------------
CPU time used                    :  00:00:00.98

Generator state:
 s = 292182416




***********************************************************
HOST = Moshnast.local, Darwin

ulcg_CreateLCG:   m = 2147483647,   a = 16807,   c = 0,   s = 1


swalk_RandomWalk1 test:
-----------------------------------------------
   N =  1,  n = 1000000,  r =  0,   s = 30,   L0 =  150,   L1 =  150



-----------------------------------------------
Test on the values of the Statistic H

Number of degrees of freedom          :   52
ChiSquare statistic                   :   41.53
p-value of test                       :    0.85


-----------------------------------------------
Test on the values of the Statistic M

Number of degrees of freedom          :   52
ChiSquare statistic                   :   50.86
p-value of test                       :    0.52


-----------------------------------------------
Test on the values of the Statistic J

Number of degrees of freedom          :   75
ChiSquare statistic                   :  102.85
p-value of test                       :    0.02


-----------------------------------------------
Test on the values of the Statistic R

Number of degrees of freedom          :   44
ChiSquare statistic                   :   38.94
p-value of test                       :    0.69


-----------------------------------------------
Test on the values of the Statistic C

Number of degrees of freedom          :   26
ChiSquare statistic                   :   17.33
p-value of test                       :    0.90


-----------------------------------------------
CPU time used                    :  00:00:00.67

Generator state:
 s = 165191659





========= Summary results of SmallCrush =========

 Version:          TestU01 1.2.3
 Generator:        ulcg_CreateLCG
 Number of statistics:  15
 Total CPU time:   00:00:07.26
 The following tests gave p-values outside [0.001, 0.9990]:
 (eps  means a value < 1.0e-300):
 (eps1 means a value < 1.0e-15):

       Test                          p-value
 ----------------------------------------------
  1  BirthdaySpacings                 eps
  2  Collision                        eps
  6  MaxOft                           eps
 ----------------------------------------------
 All other tests were passed
```

---

MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
