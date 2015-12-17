from crontab import CronTab
from lib.helpers import get_times


###################################################################################################
class Cron_Base(object):
    COMMENTS = ["reload_pins"]

    #----------------------------------------------------------------------------------------------
    def __init__(self):
        self.cron = CronTab(tabfile='/etc/crontab', user='root')


    #----------------------------------------------------------------------------------------------
    def set_times(self):
        times = get_times()
        command = "root     curl 127.0.0.1/reload_pins"
        for hour, minute in times:
            job = self.cron.new(command=command, comment="reload_pins", user="root")
            job.hour.on(hour)
            job.minute.on(minute)
        self.cron.write()


    #----------------------------------------------------------------------------------------------
    def clean_cron(self):
        for job in self.cron:
            if job.comment in self.COMMENTS:
                self.cron.remove(job)
                self.cron.write()

Cron = Cron_Base()
