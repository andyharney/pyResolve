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

# Define the function

def resolver():


    # Import the modules
    import os.path
    from urllib import request
    from time import gmtime, strftime, sleep, time
    from random import choice

    # Grab some info from the user
    while True:
        try:
            usr_log = int(input('Log length in days? - '))
            max_logs = int(input('How many logs do you wish to create? - '))
            sleep_timer = int(input('In seconds, how long do you wish to wait between checks? - '))
            break
        except ValueError:
            print('Hmmm.... please only enter whole numbers. E.g. 1, 2, 3 Not. 2.5, 3.3')
            continue
    # Define the list of addresses (IPs) to resolve
    res_serv = ['http://74.125.228.100',
                 'http://74.125.224.72/',
                 'http://173.194.115.23',
                 'http://173.194.115.24',
                 'http://173.194.115.31',
                 'http://212.58.244.68',
                 'http://212.58.244.69',
                 'http://173.194.64.160',
                 'http://134.170.188.84',
                 'http://87.98.168.164']
    # Set a few vars, day or log_length not elegant
    logs = 0
    mins = 0
    day = 1440
    log_length = day * usr_log
    # Initial print to let the user know its running
    print('Running.....')
    start_time = time()
    while logs < max_logs:
        logs += 1
        # Current time is taken and logged into the filename
        # This avoids overwriting logs with new ones
        curtime = strftime("%Y-%m-%d %H-%M-%S", gmtime())
        outlog = os.path.expanduser('ping_' + curtime + '.log')
        outfile = open(outlog, 'w')
        outfile.close()
        while mins < log_length:
            mins += 1
            # A failure to resolve with urlopen throws an exception, we catch it
            try:
                # Here we pick a server to resolve from res_servs
                # If it resolves the time and url are logged
                randserv = choice(res_serv)
                request.urlopen(ranserv, timeout=2)
                outfile = open(outlog, 'a')
                outfile.write(curtime + ' - Resolves - ' + randserv + '\n')
                outfile.close()
            # Catch the unresolved url and log the url and time
            # Who knows the url might actually be down
            except:
                outfile = open(outlog, 'a')
                outfile.write(curtime + ' - No Connection - ' + randserv + '\n')
                outfile.close()
            # Now we wait
            sleep(sleep_timer)
            run_time = time() - start_time
            if run_time > 60:
                minutes, seconds = divmod(run_time, 60)
                print('Running for ' + str(int(minutes)) + ' minutes ' + str(int(seconds)) + ' seconds', end = '\r')
            else:
                seconds = time() - start_time
                print('Running for ' + str(int(seconds)) + ' seconds', end = '\r')

resolver()
