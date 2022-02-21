from datetime import datetime

odds = []

for x in range(60):
    if x % 2 !=0 :
        odds.append(x)

rigth_this_minute = datetime.today().minute

if rigth_this_minute in odds:
    print('This minute seems a little odd')
else:
    print('Not an odd minute')