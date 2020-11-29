# productivity-tools

## GitHub Commit Reminder

This displays a little welcome message whenever you open your Bash terminal, reminding you to make a GitHub commit if you haven't already made one today.  If you have already committed today, it'll tell you how many commits you've done.

#### Usage

Place `greetings.py` into your home directory (on Linux, usually `/home/username`).  Then, open up your `.bashrc` in your favourite text editor and add the following two lines (don't forget to use your own GitHub handle):

```
export GITHUB_USERNAME="YourGitHubUsernameHere"
python ~/greeting.py $GITHUB_USERNAME
```

To make this work, you'll have to register for the GitHub API to properly be able to query it for your commit history.
