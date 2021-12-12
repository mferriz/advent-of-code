--------------
Advent Of Code
--------------

`Advent of code <https://adventofcode.com>`_ is a yearly event that provides
puzzles and challenges that are mainly oriented to be resolved using computer
programming. The participant of the event can choose to solve each puzzle
using a language of choice.

The programs that are within this repository includes this author's solution
to the puzzles. The language of choice is `Python <https://www.python.org>`_,
and some libraries used that do not belong to the standard Python libraries
include:

* `NumPy <https://www.numpy.org>`_, the fundamental package for scientific
  computing with Python, and
* `Bitarray <https://github.com/ilanschnell/bitarray>`_, efficient array
  of booleans.


Installation
------------

The following instructions can help to install this code in Linux operating
systems, or Mac OS.

.. code-block:: bash

   git clone git@github.com:mferriz/advent-of-code.git
   cd advent-of-code
   python3 -m venv aoc
   source aoc/bin/activate
   pip install -U pip
   pip install -r requirements.txt
   pip install -e .
   

Executing a Program for Solving a Puzzle
----------------------------------------

After installation, it is simple to execute a program by doing
``aoc YYYY.DD``, where YYYY is the year of the puzzles, and DD corresponds
to the day.

For example, to execute day 10 of year 2021, run ``aoc 2021.10``.


