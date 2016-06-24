************
Introduction
************

.. contents:: Table of Contents
   :depth: 2


Background
==========
Benford's Law was first published by American astronomer Simon Newcomb in a paper called "Note on the Frequency of Use of the Different Digits in Natural Numbers", which appeared in The American Journal of Mathematics (1881) 4, 39-40. It was re-discovered by Frank Benford in 1938, who published an article called "The Law of Anomalous Numbers" in Proc. Amer. Phil. Soc 78, pp 551-72.


Benford's Law
=============
Specifically, in data sets, the leading digit(s) is (are) distributed in a specific, nonuniform way. While one might think that the number 1 would appear as the first digit 11 percent of the time (i.e., one of nine possible numbers), it actually appears about 30 percent of the time. Nine, on the other hand, is the first digit less than 5 percent of the time. The theory covers the first digit, second digit, first two digits, last digit and other combinations of digits because the theory is based on a logarithm of probability of occurrence of digits.


Graphical summary
-----------------
Benford's Law is summarized below for the first two digits of the numbers being observed.


+---+----------------+----------------+
| d | Prob(digit1=d) | Prob(digit2=d) |
+===+================+================+
| 0 |     0.0        |     0.1197     |
+---+----------------+----------------+
| 1 |     0.301      |     0.1139     |
+---+----------------+----------------+
| 2 |     0.1761     |     0.1088     |
+---+----------------+----------------+
| 3 |     0.1249     |     0.1043     |
+---+----------------+----------------+
| 4 |     0.0969     |     0.1003     |
+---+----------------+----------------+
| 5 |     0.0792     |     0.0967     |
+---+----------------+----------------+
| 6 |     0.0669     |     0.0934     |
+---+----------------+----------------+
| 7 |     0.0580     |     0.0904     |
+---+----------------+----------------+
| 8 |     0.0512     |     0.0876     |
+---+----------------+----------------+
| 9 |     0.0458     |     0.0850     |
+---+----------------+----------------+


Here the same data is shown graphically to emphasize just how counter-intuitive the law really is, especially with respect to the first digit probabilities.

.. figure:: ./images/Benford's_Law_Digits_1_2.png
   :scale: 75%
   :width: 500
   :align: center


Intuitive Explanation
---------------------
An excellent intuitive explanation of the phenomenon is provided here: `How / Why does it work? <http://datagenetics.com/blog/march52012/index.html>`_




.. NOTE::

    Although Simon Newcomb first reported the phenomenon, it is called Benford's law in honor of Frank Benford who re-discovered it later.


