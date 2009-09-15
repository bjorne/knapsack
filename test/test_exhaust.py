#!/usr/bin/env python

import sys
sys.path.append('../lib')

from exhaust import *
import random
import unittest

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_read(self):
      objects = [(3,13), (1,4), (2,6), (5,12), (4,8)]
      capacity = 9
      knapsack = (objects, capacity)

      c = Conf()
      conf_knapsack = c.read_file('../input/referenceExample.txt')

      self.assertEqual(conf_knapsack, knapsack)

      self.assertRaises(Exception, c.read_file, './input/faulty.txt')

class TestExhaust(unittest.TestCase):
  def setUp(self):
    self.e = Exhaust()

  def test_all_permutations(self):
    allpossibilities = [[1], [2], [3], [1,2], [2,3], [1,3], [1,2,3]]
    ret = self.e.all_combinations([1,2,3])

    # sort so that we can compare; we do not care about order.
    [combo.sort() for combo in allpossibilities]
    allpossibilities.sort()

    [combo.sort() for combo in ret]
    ret.sort()

    self.assertEquals(ret, allpossibilities)

  def test_find_best_knapsack(self):
    c = Conf()
    confknapsack = c.read_file('../input/referenceExample.txt')

    optset, size, value = self.e.optimal_knapsack(confknapsack)

    assertEqual(size, 9)
    assertEqual(value, 9)

    optset.sort()
    goal = [(1,4), (3,13), (5,12)]
    goal.sort() # not needed

    assertEqual(optset, goal)

if __name__ == '__main__':
    unittest.main()
