from subprocess import check_output
import sys

def get_merged_branches():

    raw_results = check_output('git branch --merged master', shell=True)
    
    branchs = []
    for branch in raw_results.decode('utf-8').strip().split('\n'):
        if not branch.startswith('*') and branch.strip() not in ['master', 'staging', 'sprint', 'dev', 'main']:
            branchs.append(branch.strip()) 

    return branchs


def delete_branch(branch):
    return check_output('git branch -D %s' % branch, shell=True).strip()

for branch in get_merged_branches():
    delete_branch(branch)