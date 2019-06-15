# coding:utf-8

scores = {'bob':'98','tom':'87'}
print(scores['bob'])

scores['alice'] = '100'
print(scores)

# scores['jerry']
if 'jerry' in scores:
    print(scores['jerry'])
else:
    print('Not Found')

if scores.get('alice'):
    print(scores['alice'])
else:
    print('Not Found')

print(scores.get('alice1','0'))