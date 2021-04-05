#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def createList():
    foodList = []
    foodString = ''
    
    while True:
        foodName = input('Enter your favourite food (If you have no more then press Enter) : \n')
    
        if foodName == '':
            break
        
        foodList.append(foodName)
    
    for i in range(len(foodList)-1):
        foodString += foodList[i] + ', '
        
    foodString += 'and ' + foodList[-1]
    
    print(foodString)
    


if __name__ == '__main__':
    createList()