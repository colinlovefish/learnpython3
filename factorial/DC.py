#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def landDivision(lenth,wth):
	if lenth == wth:
		return lenth
	
	temp = lenth - wth
	if temp > wth:
	    return landDivision(temp,wth)
	return landDivision(wth,temp)
	



print landDivision(1680,640)

	    	
     
	