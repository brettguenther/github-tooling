from github import GithubApi
import yaml
from argparse import ArgumentParser

f = open('./config.yml')
params = yaml.load(f, Loader=yaml.FullLoader)

parser = ArgumentParser()

parser.add_argument("-e", "--environment", dest="environment",help="environment in config.yml for the destination username (account)")
parser.add_argument("-u", "--username", dest="username",help="username (account) to migrate stars from")
args = parser.parse_args()

github_token = params['hosts'][args.environment]['github_token']
github_personal = GithubApi(key=github_token)

stars = github_personal.get_stars(args.username,1)
print("numbers of stars: {}".format(len(stars)))
for star in stars:
    github_personal.add_star(star['owner']['login'],star['name'])