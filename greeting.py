import os
import sys
import requests
from datetime import datetime

def getCommitsToday(username, today = None):
    if today == None:
        today = datetime.today().strftime('%Y-%m-%d')
        
    responses = requests.get('https://api.github.com/users/{}/events'.format(username))
    commits = 0
    for response in responses.json():
        if(response['type'] == 'PushEvent' and response['created_at'][:10] == today):
            commits = commits + 1
    
    return commits
        

try:
    username = sys.argv[1]
except IndexError:
    print("{}: no GitHub username passed as command-line argument.  Exiting.".format(sys.argv[0]))
    sys.exit(-1)


today = datetime.today().strftime('%Y-%m-%d')

os.system('echo "Welcome, $(tput setaf 6)$(whoami)! $(tput sgr 0)  [$(date)]"')

commits = getCommitsToday(username)

if commits == 0:
	output = 'echo "$(tput setaf 1)You have not yet made a GitHub commit today.$(tput sgr 0)"'
elif commits == 1:
	output = 'echo "You have committed once today.  Nice job!"'
elif commits > 1:
	output = 'echo "You have committed {} times today.  Nice job!"'.format(commits)

os.system(output)
exit()

