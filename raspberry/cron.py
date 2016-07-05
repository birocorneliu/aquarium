from crontab import CronTab

cron = CronTab(tabfile='/etc/crontab', user='root')


import pdb;pdb.set_trace()
job = cron.new(command="date >> /home/corneliu/output.txt", comment="cron_no_2", user="root")
job.minute.on(10)
job.hour.on(10)

cron.write()


import pdb;pdb.set_trace()
