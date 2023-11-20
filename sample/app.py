import connexion
from flask_apscheduler.scheduler import BackgroundScheduler
import atexit

from scrappers.scrapping import scrap

app = connexion.FlaskApp(__name__, specification_dir='./')

app.add_api('openapi.yaml')


def scrapping():
    scrap()


# Adding cron to scrappe
cron = BackgroundScheduler()
# Scrap when the application start
cron.add_job(scrapping)
# Scrap every 6 hours to update data
cron.add_job(scrapping, 'interval', hours=6)
cron.start()

print(cron.get_jobs())

# Shutdown the cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))
