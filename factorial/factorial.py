#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n - 1)


print factorial(10)


#Hanoi

i = 1
def move(n,f,t):
	global i
	print "第%d步：将%d号盘子从%s -> %s" %(i,n,f,t)
	i += 1
	

def hanoi(n, A, B, C) :
  if n == 1 :
    move(1, A, C)
  else :
    hanoi(n - 1, A, C, B) 
    move(n, A, C)    
    hanoi(n - 1, B, A, C)


try :
  n = int(raw_input("please input a integer :"))
  print "移动步骤如下："
  hanoi(n, 'A', 'B', 'C')
except ValueError:
  print "please input a integer n(n > 0)!" 