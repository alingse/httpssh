#coding=utf-8
#author@shibin
#2016.04.21

import os


class Session(object):
    """Session is a connect for the http user"""
    def __init__(self,user,host):
        self._user = user
        self._host = host


        local_ssh_path = 
        local_ssh_file = 'id_rsa'

        public_path = '/home/{}/.ssh/id_rsa.pub'.format(user)
        private_path = '/home/{}/.ssh/id_rsa'.format(user)

        if os.path.exists(public_path) and os.path.exists(private_path):
            self.public_key = self.__load_public(public_path)
            self.private_key = self.__load_private(private_path)
        else:
            pass

    def __load_public(self,public_path):
        pass
        return None


    def __load_private(self,private_path):
        pass
        return None


    def auth(self,enc_passwd):
        pass