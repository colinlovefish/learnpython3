
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def personIsSeller():
	return name[-1] == "m"

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if personIsSeller(person):
				print person + "is a seller!"
				return True
			else:
				search_queue += graph[person]
			    searched.append(person)
	return False

search("you")