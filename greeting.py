import os
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
        

# Remove later.
username = 'ivorysoap'

today = datetime.today().strftime('%Y-%m-%d')

os.system('echo "Welcome, $(whoami)!  [$(date)]"')

commits = getCommitsToday(username)

if commits == 0:
	output = 'echo "You have not yet committed anything today."'
elif commits == 1:
	output = 'echo "You have committed once today.  Nice job!"'
elif commits > 1:
	output = 'echo "You have committed {} times today.  Nice job!"'.format(commits)

os.system(output)
exit()

