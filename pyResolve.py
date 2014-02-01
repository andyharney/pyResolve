# Copyright 2014 Andy Harney (2014)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


def resolver():
    import os.path
    from urllib import request
    from time import gmtime, strftime, sleep
    from random import choice
    while True:
        try:
            usr_log = int(input('Log length in days? - '))
            max_logs = int(input('How many logs do you wish to create? - '))
            break
        except ValueError:
            print('Hmmm.... please only enter whole numbers. E.g. 1, 2, 3 Not. 2.5, 3.3')
            continue
    pingservs = ['http://74.125.228.100',
                 'http://74.125.224.72/',
                 'http://173.194.115.23',
                 'http://173.194.115.24',
                 'http://173.194.115.31',
                 'http://212.58.244.68',
                 'http://212.58.244.69',
                 'http://173.194.64.160',
                 'http://134.170.188.84',
                 'http://87.98.168.164']

    curtime = strftime("%Y-%m-%d %H-%M-%S", gmtime())
    logs = 0
    mins = 0
    day = 1440
    log_length = day * usr_log
    while logs < max_logs:
        logs += 1
        outlog = os.path.expanduser('ping_' + curtime + '.log')
        outfile = open(outlog, 'w')
        outfile.close()
        while mins < log_length:
            mins += 1
            try:
                randserv = choice(pingservs)
                request.urlopen(randserv, timeout=2)
                outfile = open(outlog, 'a')
                outfile.write(curtime + ' - Resolves - ' + randserv + '\n')
                outfile.close()
            except:
                outfile = open(outlog, 'a')
                outfile.write(curtime + ' - No Connection - ' + randserv + '\n')
                outfile.close()
            sleep(60)
            curtime = strftime("%Y-%m-%d %H-%M-%S", gmtime())
            print('Running for ' + str(mins) + ' minutes', end='\r')

resolver()
