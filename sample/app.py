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
cron.add_job(scrapping, 'interval', seconds=5)
cron.start()

# Shutdown the cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))
