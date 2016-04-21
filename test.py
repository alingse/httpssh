#coding=utf-8
#author@httpssh
#2016.04.21

#import requests
#import base64

from httpssh.auth import Session


def login(user = 'test', passwd = '123456'):
    
    session = Session('root','localhost')
    public = s.public_key



