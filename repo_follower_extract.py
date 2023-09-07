from github import GithubApi
import yaml
from argparse import ArgumentParser

f = open('./config.yml')
params = yaml.load(f, Loader=yaml.FullLoader)

parser = ArgumentParser()

parser.add_argument("-e", "--environment", dest="environment",help="environment in config.yml")
parser.add_argument("-o", "--owner", dest="owner",help="repo owner")
parser.add_argument("-r", "--repo", dest="repo",help="repo name")

args = parser.parse_args()

github_token = params['hosts'][args.environment]['github_token']
github_personal = GithubApi(key=github_token)

def user_print(users,type):
    for user in users:
        username = user["login"]
        user_info = github_personal.get_user(username)
        print('{},{},{},{},{}'.format(username,user_info["email"],user_info["company"],user_info["public_repos"],type))

hasMore = True
page = 1

#watchers
watchers = github_personal.list_watchers(args.owner,args.repo,page)

while hasMore:
    user_print(watchers,"watcher")
    if len(watchers) < 100:
        hasMore = False
    else:
        page += 1
        watchers = github_personal.list_watchers(args.owner,args.repo,page)

#stargazers
hasMore = True
page = 1
stargazers = github_personal.list_stargazers(args.owner,args.repo,page)

while hasMore:
    user_print(stargazers,"stargazer")
    if len(watchers) < 100:
        hasMore = False
    else:
        page += 1
        stargazers = github_personal.list_stargazers(args.owner,args.repo,page)

#filing issues
hasMore = True
page = 1
issues = github_personal.list_issues(args.owner,args.repo,page)

while hasMore:
    for issue in issues:
        username = issue["user"]["login"]
        user_info = github_personal.get_user(username)
        print('{},{},{},{},{}'.format(username,user_info["email"],user_info["company"],user_info["public_repos"],"issue"))
    if len(issues) < 100:
        hasMore = False
    else:
        page += 1
        issues = github_personal.list_issues(args.owner,args.repo,page)

# forks
hasMore = True
page = 1
forks = github_personal.list_forks(args.owner,args.repo,page)

while hasMore:
    for fork in forks:
        username = fork["owner"]["login"]
        user_info = github_personal.get_user(username)
        print('{},{},{},{},{}'.format(username,user_info["email"],user_info["company"],user_info["public_repos"],"fork"))
    if len(forks) < 100:
        hasMore = False
    else:
        page += 1
        forks = github_personal.list_forks(args.owner,args.repo,page)