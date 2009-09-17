#!/usr/bin/env python

import sys, re

class Conf(object):

  def __init__(self):
    self.objects = []
    self.capacity = 0

  def read_file(self, filename):
    f = open(filename, 'r')

    for line in f.readlines():
      result = re.match("^capacity=(\d+)$", line)
      if result:
        self.capacity = int(result.group(1))
      else:
        result = re.match("^\((\d+)\s*,\s*(\d+)\)$", line)
        if result:
          item = (int(result.group(1)), int(result.group(2)))
          self.objects.append(item)
        else:
          raise Exception("Config error: invalid item")

    return (self.objects, self.capacity)


class Exhaust(object):

  def __init__(self):
    pass

  def solve(self, filename):
      conf = Conf().read_file(filename)
      return self.optimal_knapsack(conf)

  def optimal_knapsack(self, conf):
      items, capacity = conf
      best = 0
      opt = []
      for idx in self.all_combinations(range(0,len(items))):
        solution = map(lambda i: items[i], idx)
        w = self.weight_of_solution(solution)
        if w > capacity:
          continue

        v = self.value_of_solution(solution)
        if v > best:
          best = v
          opt = solution

      return opt, self.weight_of_solution(opt), self.value_of_solution(opt)

  def weight_of_solution(self, solution):
      weight = 0
      for item in solution:
          weight += item[0]
      return weight

  def value_of_solution(self, solution):
      value = 0
      for item in solution:
          value += item[1]
      return value

  def all_combinations(self, indices):
    combos = []
    for r in range(1, len(indices)+1):
        for c in self.combinations(indices, r):
            yield(list(c))

  # from http://docs.python.org/library/itertools.html#itertools.combinations - available from itertools in >= 2.6
  def combinations(self, iterable, r):
      # combinations('ABCD', 2) --> AB AC AD BC BD CD
      # combinations(range(4), 3) --> 012 013 023 123
      pool = tuple(iterable)
      n = len(pool)
      if r > n:
          return
      indices = range(r)
      yield tuple(pool[i] for i in indices)
      while True:
          for i in reversed(range(r)):
              if indices[i] != i + n - r:
                  break
          else:
              return
          indices[i] += 1
          for j in range(i+1, r):
              indices[j] = indices[j-1] + 1
          yield tuple(pool[i] for i in indices)
