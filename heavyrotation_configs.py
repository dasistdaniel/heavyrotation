#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ConfigParser import SafeConfigParser
import os


def list_configs():
    configs = []
    for root, dirs, files in os.walk("./configs"):
        for file in files:
            if file.endswith('.config'):
                configs.append(file)
    return configs


def read_configs(configs):
    sender = {}
    for config in configs:
        sender[config] = {}
        parser = SafeConfigParser()
        parser.read('./configs/' + config)
       
        if 'settings' and 'xpath' in parser.sections():
            sender[config]['settings'] = dict(parser.items('settings'))
            sender[config]['xpath'] = dict(parser.items('xpath'))

    return sender


