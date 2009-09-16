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

  def test_all_combinations(self):
    allpossibilities = [[1], [2], [3], [1,2], [2,3], [1,3], [1,2,3]]
    ret = list(self.e.all_combinations([1,2,3])) # listify generator.

    # sort so that we can compare; we do not care about order.
    [combo.sort() for combo in allpossibilities]
    allpossibilities.sort()

    [combo.sort() for combo in ret]
    ret.sort()

    self.assertEquals(ret, allpossibilities)

  def test_weight_of_solution(self):
      expected = 10
      solution = [(2,5),(3,4),(5,10)]
      self.assertEquals(self.e.weight_of_solution(solution), expected)

  def test_value_of_solution(self):
      expected = 19
      solution = [(2,5),(3,4),(5,10)]
      self.assertEquals(self.e.value_of_solution(solution), expected)

  def test_find_best_knapsack(self):
    c = Conf()
    confknapsack = c.read_file('../input/referenceExample.txt')

    optset, size, value = self.e.optimal_knapsack(confknapsack)

    self.assertEquals(size, 9)
    self.assertEquals(value, 29)

    goal = [(3,13), (1,4), (5,12)]
    goal.sort()
    optset.sort()
    self.assertEquals(optset, goal)

if __name__ == '__main__':
    unittest.main()
