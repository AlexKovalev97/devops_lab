import argparse
import datetime
import getpass
import requests


def get_json(user, password, repo):
    url = 'https://api.github.com/repos/alenaPy/{0}/pulls?page=1&per_page=100'
    answer = requests.get(url.format(repo),
                          auth=(user, password))
    return answer.json()


def get_lines(user, password, num):
    url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls/%d'
    answer = requests.get(url % num, auth=(user, password))
    return answer.json()


def keys():
    parser = argparse.ArgumentParser(description='Get PR(Pull \
        Request)statistics from GitHub')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')
    parser.add_argument('-a', '--number of lines added',
                        action="store_true",
                        dest='a', help='show number of added lines')
    parser.add_argument('-d', '--number of lines deleted',
                        action="store_true",
                        dest='d', help='show number of deleted lines')
    parser.add_argument('-l', '--label', action="store_true",
                        dest='l', help='attached label')
    parser.add_argument('-u', '--user', action="store_true",
                        dest='u', help='user who opened')
    parser.add_argument('-n', '--number of days opened', action="store_true",
                        dest='n', help='number of weeks')
    parser.add_argument(metavar='<user>', type=str,
                        dest='user', help='login')
    parser.add_argument(metavar='<repo>', type=str,
                        dest='repo', help='repository ')
    args = parser.parse_args().__dict__
    return args


def pr_stat():
    key = keys()
    password = getpass.getpass()
    getter = get_json(key['user'], password, key['repo'])
    if key['a']:
        for i in range(1, 93):
            getter_lines = get_lines(key['user'], password, i)
            print(str(getter_lines['user']['login']), 'added',
                  str(getter_lines['additions']), 'lines')
    if key['d']:
        for i in range(1, 93):
            getter_lines = get_lines(key['user'], password, i)
            print(str(getter_lines['user']['login']), 'deleted',
                  str(getter_lines['deletions']), 'lines')
    if key['l']:
        for k in getter:
            print(str(k['user']['login']), str(k['number']),
                  str(k['labels'][0]['name']))
    if key['u']:
        for k in getter:
            print('Opened by: ', str(k['user']['login']), 'at',
                  str(k['created_at']))
    if key['n']:
        for k in getter:
            current = str(datetime.date.today())
            t = str(k['created_at'])
            t_Pos = t.find('T')
            before_t = t[:t_Pos]
            current = current.split('-')
            before_t = before_t.split('-')
            aa = datetime.date(int(current[0]), int(current[1]),
                               int(current[2]))
            bb = datetime.date(int(before_t[0]), int(before_t[1]),
                               int(before_t[2]))
            cc = aa - bb
            result = str(cc)
            print(str(k['user']['login']), 'created', result.split()[0],
                  'days ago')


pr_stat()
