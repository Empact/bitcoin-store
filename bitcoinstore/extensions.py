from flask_apscheduler import APScheduler
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest


debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
flask_static_digest = FlaskStaticDigest()
scheduler = APScheduler()

@scheduler.task('interval', id='expire_stale_item_reservations', seconds=30, misfire_grace_time=900)
def expire_stale_item_reservations():
    print('Job 1 executed')
