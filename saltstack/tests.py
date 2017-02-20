#coding=utf8

a={u'192.168.11.61': [u'Feb 20 15:00:38 cluster-node01 systemd: Starting Session 24610 of user devops.\nFeb 20 15:00:38 cluster-node01 python: ansible-command Invoked with warn=True executable=None _uses_shell=True _raw_params=sudo /usr/bin/tail -n 5 /var/log/messages removes=None creates=None chdir=None\nFeb 20 15:00:38 cluster-node01 systemd-logind: Removed session 24596.\nFeb 20 15:00:39 localhost haproxy[17480]: 192.168.11.63:42203 [20/Feb/2017:15:00:39.477] mysql-pxc-cluster mysql-pxc-cluster/cluster-node02 1/0/208 5460 -- 17/0/0/0/0 0/0\nFeb 20 15:00:40 cluster-node01 python: ansible-command Invoked with warn=True executable=None _uses_shell=True _raw_params=sudo /usr/bin/tail -n 5 /var/log/messages removes=None creates=None chdir=None']}
print type(a)
print a.keys(),'\n',a.values()[0][0]
