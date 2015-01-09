#!/usr/bin/python

bound = 29

def add(c, k, s):
        return (c + k + s) % bound

def sub(c, k, s):
        return (c - k + s) % bound

def mul(c, k, s):
        return ((c * k) + s) % bound

def xor(c, k, s):
        return ((c ^ k) + s) % bound

def sf3301(c, k, s):
        return (3301 - (c+k) + s) % bound

def ti3301(c, k, s):
        return (c + k*3301 + s) % bound

def pow3301(c, k, s):
        return (c + pow(k, 3301) + s) % bound

def topow3301(c, k, s):
        return (c + pow(3301, k) + s) % bound

def sf1033(c, k, s):
        return (1033 - (c+k) + s) % bound

def ti1033(c, k, s):
        return (c + k*1033 + s) % bound

def pow1033(c, k, s):
        return (c + pow(k, 1033) + s) % bound

def topow1033(c, k, s):
        return (c + pow(1033, k) + s) % bound





allAppls = [add, sub, mul, xor, sf3301, ti3301, sf1033, ti1033]
