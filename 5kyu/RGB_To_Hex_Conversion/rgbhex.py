#!/usr/bin/python


def rgb(*args):
    return ''.join(map(lambda i: '%02X'%i if i<=255 else 'FF', map(lambda j: j if j>0 else 0, args)))


print rgb(255, 255, 255) ,' returns FFFFFF'
print rgb(255, 255, 300) ,' returns FFFFFF'
print rgb(0,0,0) ,' returns 000000'
print rgb(148, 0, 211) ,' returns 9400D3'
print rgb(-148, 0, 211) ,' returns 9400D3'
