#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

import requests
import json

BASE_URL = 'http://localhost:8000/dose/get_or_create_dose'
headers = {'content-type': 'application/json'}

if __name__ == '__main__':
    for i in range(0, 10):
        data = {
            "dose_number": str(i),
        }
        x = requests.post(BASE_URL, data=json.dumps(data), headers=headers)
        print(x.text)
