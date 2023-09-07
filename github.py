import requests
# from pprint import pprint as pp
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class GithubApi(object):
    def __init__(self, key, username=None):
        self.github_key = key
        self.host = 'https://api.github.com'
        self.session = requests.Session()
        header = {'Authorization': 'Bearer {}'.format(self.github_key),'X-GitHub-Api-Version': '2022-11-28','Accept': 'application/vnd.github+json'}
        self.head = header
        self.username = username

    def list_watchers(self,owner,repo,page):
        url = '{}/repos/{}/{}/subscribers?per_page=100&page={}'.format(self.host,owner,repo,page)
        r = requests.request("GET",url,headers=self.head)
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)
    
    def list_stargazers(self,owner,repo,page):
        url = '{}/repos/{}/{}/stargazers?per_page=100&page={}'.format(self.host,owner,repo,page)
        r = requests.request("GET",url,headers=self.head)
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)

    def list_forks(self,owner,repo,page):
        url = '{}/repos/{}/{}/forks?per_page=100&page={}'.format(self.host,owner,repo,page)
        r = requests.request("GET",url,headers=self.head)
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)

    def list_issues(self,owner,repo,page):
        url = '{}/repos/{}/{}/issues?per_page=100&page={}'.format(self.host,owner,repo,page)
        r = requests.request("GET",url,headers=self.head)
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)

    def get_user(self,username):
        url = '{}/users/{}'.format(self.host,username)
        r = requests.request("GET",url,headers=self.head)
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)

    def issue_add_labels(self,repo,issue_number,labels_array=[]):
        url = '{}/{}/{}/{}/{}/{}/{}'.format(self.host,'repos',self.username,repo,'issues',issue_number,'labels')
        r = requests.request("POST",url,headers=self.head,data=json.dumps(labels_array))
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)

    def issue_add_comments(self,repo,issue_number,comment_body=''): 
        url = '{}/{}/{}/{}/{}/{}/{}'.format(self.host,'repos',self.username,repo,'issues',issue_number,'comments')
        r = requests.request("POST",url,headers=self.head,data=json.dumps(comment_body))
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)

    def issue_labels(self,repo):
        url = '{}/{}/{}/{}/{}'.format(self.host,'repos',self.username,repo,'labels')
        r = requests.request("GET",url,headers=self.head)
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)

    def add_issue(self,repo,issue_body=''):
        url = '{}/{}/{}/{}/{}'.format(self.host,'repos',self.username,repo,'issues')
        r = requests.request("POST",url,headers=self.head,data=json.dumps(issue_body))
        if r.status_code == requests.codes.ok:
            return r.json()

    def add_deploy_keys(self,repo,deploy_key={}):
        url = '{}/{}/{}/{}/{}'.format(self.host,'repos',self.username,repo,'keys')
        r = requests.request("POST",url,headers=self.head,data=json.dumps(deploy_key))
        if r.status_code == requests.codes.ok:
            return r.json()
            
    def create_repository(self,repo_body):
        url = '{}/{}/{}'.format(self.host,'user','repos')
        r = requests.request("POST",url,headers=self.head,data=json.dumps(repo_body))
        if r.status_code == requests.codes.ok:
            return r.json()
        
    def get_stars(self,username,page=1):
        url = '{}/{}/{}/{}'.format(self.host,'users',username,'starred') 
        params = {'per_page':100,'page':page}
        r = requests.request("GET",url,headers=self.head,params=params)
        if r.status_code == requests.codes.ok:
            return r.json()
        
    def add_star(self,owner,repo):
        url = '{}/{}/{}/{}/{}'.format(self.host,'user','starred',owner,repo) 
        headers = {'content-length':'0'}
        r = requests.request("PUT",url,headers=self.head)
        print(r.status_code)
        print(r.url)
        if r.status_code == requests.codes.ok:
            return r.json()