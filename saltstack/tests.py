#coding=utf8
code_branch=[]
a=('  origin/HEAD -> origin/master\n  origin/dev\n  origin/master\n', '')
for i in a[0].split('\n'):
    code_branch.append(i)

print code_branch