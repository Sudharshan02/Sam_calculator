import json

# import requests


def lambda_handler(event, context):

    x = event["x"]
    y = event["y"]

    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))



def add(x, y):
    return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by Zero!')
    return x/y
