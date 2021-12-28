# from crontab import CronTab
# cron = CronTab(user=True)
# print(cron)
# cron.new(command='my command')

# from crontab import CronTab

# job = cron.new(command='python example1.py')
# job.minute.every(1)

# cron.write()

# from datetime import datetime
# myFile = open('append.txt', 'a')
# myFile.write('\nAccessed on ' + str(datetime.now()))


def fun(num):
    for i in range(1, 11):
        print(num, 'X', i, '=', num*i)


fun(5)
print('Table 6')
fun(6)
