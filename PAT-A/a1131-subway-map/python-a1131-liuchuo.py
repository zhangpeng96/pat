"""
    @name     : a1131
    @version  : 21.0309
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

from math import inf
from copy import copy
from itertools import tee
from types import SimpleNamespace
from collections import defaultdict


def pair_wise(it):
    a, b = tee(it)
    next(b, None)
    return zip(a, b)

def find_transfer(path):
    count, pre_line = 0, 0
    for (a, b) in pair_wise(path):
        if line[a, b] != pre_line:
            count += 1
            pre_line = line[a, b]
    return count

def dfs(root, station, temp_path):
    if station > mini.station:
        return
    # 如果到达终点，判断该条路径最优条件
    if root == end:
        # 先优先选取经过站点最少的路径
        if station < mini.station:
            mini.station = station
            mini.transfer = find_transfer(temp_path)
            mini.path = copy(temp_path)
        # 若经过站点数相同，则选择换乘站最少的路径
        elif station == mini.station and find_transfer(temp_path) < mini.transfer:
            mini.station = station
            mini.transfer = find_transfer(temp_path)
            mini.path = copy(temp_path)
        return
    # 遍历邻接表
    for child in adj[root]:
        if not visit[child]:
            visit[child] = True
            temp_path.append(child)
            dfs(child, station+1, temp_path)
            visit[child] = False
            temp_path.pop()

def print_path(path):
    pre_line, pre_transfer = 0, path[0]
    for i in range(1, len(path)):
        now_line = line[ path[i-1], path[i] ]
        if now_line != pre_line:
            if pre_line:
                print('Take Line#{} from {:04} to {:04}.'.format(pre_line, pre_transfer, path[i-1]))
            pre_line = now_line
            pre_transfer = path[i-1]
    print('Take Line#{} from {:04} to {:04}.'.format(pre_line, pre_transfer, path[-1]))


adj = defaultdict(list)
line = defaultdict(int)
visit = defaultdict(bool)

for i in range(int(input())):
    station = map(int, input().split()[1:])
    for a, b in pair_wise(station):
        adj[a].append(b)
        adj[b].append(a)
        line[a, b] = line[b, a] = i + 1

for i in range(int(input())):
    mini = SimpleNamespace(station=inf, transfer=inf, path=[])
    start, end = map(int, input().split())
    visit[start] = True
    dfs(start, 0, [start])
    visit[start] = False
    print(mini.station)
    print_path(mini.path)
