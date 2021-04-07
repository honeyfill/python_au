import requests

TOKEN = '80f968033c5d4e9d550c7ddb87fed00a202913d8'

PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLES', 'HEXNUMBER', 'REQUESTS', 'ITERATOR']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Moved']


def prepare_headers():
    return {'Authorization': 'Token {}'.format(TOKEN),
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"
            }


def get_all_pr_commits(pr):
    commits = []
    all = requests.get(pr["commits_url"], headers=prepare_headers())
    for pc in all.json():
        commit = pc["commit"]
        commits.append(commit)
    return commits


def get_all_user_prs(user_login, repo_name, pr_state):
    pulls = requests.get('https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repo_name, pr_state),
                         headers=prepare_headers())
    return pulls


def check_prefixes(title):
    errors = ''
    act = title.split()[1]
    group = title.split('-')[1].split()[0]
    pref = title.split('-')[0]
    if not pref in PREFIX:
        errors += "Prefix must be one of the following {}.\n".format(PREFIX)
    if not group in GROUP:
        errors += "Group must be one of the following {}. \n".format(GROUP)
    if not act in ACTION:
        errors += "Action must be on of the following {}. \n".format(ACTION)
    return errors


def send_pr_comment(pr, errors):
    data = {'body': errors,
            'path': requests.get(pr['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    ans = requests.post(pr['url'] + '/comments', headers=prepare_headers(), json=data)


def verify_pr(pull):
    errors = ''
    commits = get_all_pr_commits(pull)
    for comm in commits:
        errors += check_prefixes(comm['message'])
        if len(errors) > 0:
            send_pr_comment(pull, errors)


if __name__ == '__main__':
    repo_name = 'python_au'
    user_login = 'honeyfill'
    pr_state = 'open'
    pulls = get_all_user_prs(user_login, repo_name, pr_state)
    for pull in pulls.json():
        verify_pr(pull)
