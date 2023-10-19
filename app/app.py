#!/usr/bin/env python3

import json
import requests
import logging
import os

logger = logging.getLogger()

if __name__ == '__main__':
    resp = requests.get('https://httpbin.org/status/200')
    resp.raise_for_status()
    logger.warning('It ran')