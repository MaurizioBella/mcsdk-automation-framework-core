import json
import os
from urllib import parse

import requests
from mcsdk.git.client import RepoClient

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
TRAVIS_BUILD_DIR = os.environ.get('TRAVIS_BUILD_DIR')
TRAVIS_REPO_OWNER_DIR = os.path.dirname(TRAVIS_BUILD_DIR)


def request_new_build(repo_owner, repo):
    base_branch = os.environ.get('TRAVIS_BRANCH')
    pull_req_branch = os.environ.get('TRAVIS_PULL_REQUEST_BRANCH')

    # PR build trigger
    repo_basename = repo.split('/')[1]
    builder_repo_dir = os.path.join(TRAVIS_REPO_OWNER_DIR, repo_basename)
    builder_repo = RepoClient(TRAVIS_REPO_OWNER_DIR, GITHUB_TOKEN, repo_owner, repo_basename, builder_repo_dir)
    builder_repo.clone()
    builder_repo.fetch()

    if builder_repo.branch_exists(pull_req_branch):
        if builder_repo.make_pull_request(base_branch, pull_req_branch) == 0:
            return True
        else:
            print("Could not create PR on builder repository!")
            print('Falling back to the normal flow...')

    data = {
        'request': {
            'branch': base_branch,
            'config': {
                'env': {
                    'BASE_BRANCH': base_branch,
                    'HEAD_BRANCH': pull_req_branch
                }
            }
        }
    }

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Travis-API-Version': '3',
        'Authorization': 'token {token}'.format(token=os.environ.get('TRAVIS_TOKEN'))
    }

    print('API call for repository: ' + repo)
    print('Request headers: ' + json.dumps(headers, indent=2))
    print('Request data: ' + json.dumps(data, indent=2))

    response = requests.post(
        url='https://api.travis-ci.com/repo/{repo}/requests'.format(repo=parse.quote(repo, safe='')),
        headers=headers,
        json=data
    )

    print(response.status_code)

    # Method exit
    return True


# Code vars
owner = 'salesforce-marketingcloud'

repos = [
    '{owner}/mcsdk-automation-framework-csharp'.format(owner=owner),
    '{owner}/mcsdk-automation-framework-java'.format(owner=owner),
    '{owner}/mcsdk-automation-framework-php'.format(owner=owner),
    '{owner}/mcsdk-automation-framework-node'.format(owner=owner)
]

# Triggering the builds
for repository in repos:
    request_new_build(owner, repository)
