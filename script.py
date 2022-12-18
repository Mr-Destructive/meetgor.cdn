import sys
from git import Repo
import os

username = os.environ.get("BOT_USERNAME", "cdn-commit-bot")
token = os.environ.get("BOT_TOKEN", "")


def commit_code(image):
    repo = Repo(".")
    #repo = g.remote("origin")#, "https://github.com/mr-destructive/meetgor.cdn")#, username, token)
    #with open(image, 'r') as f:
    #    content = f.read()
    repo.git.add(image)
    repo.git.commit(message=f"snap image: {image}")
    repo.git.push()

def main():
    image = sys.argv[1]
    commit_code(image)

main()
