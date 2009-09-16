#!/usr/bin/env python

import re

class Conf(object):

  def __init__(self):
    self.objects = []
    self.capacity = 0

  # TODO: generator.
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

  def optimal_knapsack(self, conf):
      items, capacity = conf
      opt = []
      return opt

  def all_combinations(self, indices):
    return self.__get_all_combinations__([ [i] for i in indices ])

  def __get_all_combinations__(self, indices):
    if indices == []:
      return []

    if len(indices) == 1:
      return indices

    head = indices[0]
    tail = indices[1:]

    combos = self.__get_all_combinations__(tail)
    return [head] + [ head + k for k in combos ] + combos
