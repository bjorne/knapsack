#!/usr/bin/env python

import re

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
        v = self.value_of_solution(solution)
        if w <= capacity and v > best:
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
    return self.__get_all_combinations__([ [i] for i in indices ])

  # problem for large inputs> RuntimeError: maximum recursion depth exceeded in cmp
  def __get_all_combinations__(self, indices):
    if indices == []:
      return []

    if len(indices) == 1:
      return indices

    head = indices[0]
    tail = indices[1:]

    combos = self.__get_all_combinations__(tail)
    return [head] + [ head + k for k in combos ] + combos
