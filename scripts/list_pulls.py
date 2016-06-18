#!/usr/bin/python3

# This script computes the pull requests a player has made and how many points
# they obtained. Tested on Arch. Depends on python-requests

import sys
import requests
import json
import re

REPO = 'https://api.github.com/repos/pimotte/nomic'

def get_point_increase_from_diff_url(diff_url):
    diff = requests.get(diff_url)

    prev_points = {}
    next_points = {}
    #print(diff.text)
    old_style_removal = re.findall(r'^\-.*point.*$', diff.text, flags=re.M)

    for match in old_style_removal:
        #Find handle. Always @.
        username = re.search(r'@\w*', match)
        points_desc = re.search(r'\w[\d\.]* point', match)
        if points_desc is not None:
            points = re.search(r'[\d\.]*', points_desc.group(0))

        if username is not None and points is not None:
            if username in prev_points.keys():
                print('Weirdness: multiple point removals detected for ' + player)

            # Chop off @. 
            prev_points[username.group(0)[1:]] = float(points.group(0))
    
    old_style_addition = re.findall(r'^\+.*point.*$', diff.text, flags=re.M)

    for match in old_style_addition:
        #Find handle. Always @.
        username = re.search(r'@\w*', match)
        points_desc = re.search(r'\w[\d\.]* point', match)
        if points_desc is not None:
            points = re.search(r'[\d\.]*', points_desc.group(0))

        if username is not None and points is not None:
            if username in next_points.keys():
                print('Weirdness: multiple point removals detected for ' + player)

            # Chop off @. 
            next_points[username.group(0)[1:]] = float(points.group(0))
    

    # Detecting new style removal
    player = None
    for line in diff.text.split('\n'):
        if "--- a/players/" in line:
            player = re.search('(\w+)\.md', line).group(1)

        score = re.search('score: ([\d\.]+)', line)
        if score:
            if line[0] == '-':
                if player and player in prev_points.keys():
                    print('Weirdness: multiple point removals detected for ' + player)
                prev_points[player] = float(score.group(1))

            elif line[0] == '+':
                if player and player in next_points.keys():
                    print('Weirdness: multiple point additions detected for ' + player)
                next_points[player] = float(score.group(1))


                
    diff_points = {}
    for username in next_points.keys():
        diff_points[username] = next_points[username] - prev_points.get(username, 0)

    return diff_points





    





#print(json.dumps(prs.json()[0], indent=2))



#patch = requests.get(prs.json()[0]['diff_url'])
pr_data = {}
prs = requests.get(REPO + '/pulls', params={'state' : 'closed'})
while True:
    for pr in prs.json():
        points = get_point_increase_from_diff_url(pr['diff_url'])
        print('Processed PR ' + pr['title'])
        
        for username in points.keys():
            data = ("#" + str(pr['number']), pr['title'], '{:.1f}'.format(points[username]))
            pr_data[username] = pr_data.get(username, list()) + [data]
    if prs.links.get('next') is not None: 
        prs = requests.get(prs.links['next']['url'])
    else:
        break


for username in pr_data.keys():
    if username is not None:
        print('\n' + username + '\n')
        user_prs = sorted(pr_data[username], key=lambda tup: int(tup[0][1:]))
        for pr in user_prs:
            is_merged = requests.get(REPO + '/pulls/' + pr[0][1:] + '/merge')
            if is_merged.status_code == 204:
                print('| ' + ' | '.join(pr) + ' |')
