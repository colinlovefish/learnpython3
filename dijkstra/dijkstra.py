#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 

node = find_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
	low_cost = float("inf")
	low_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < low_cost and node not in processed:
			low_cost = cost
			low_cost_node = node
	return low_cost_node