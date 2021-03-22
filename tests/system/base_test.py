from unittest import TestCase
from myproject import app
from myproject import db
class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists
        app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app=app.test_client()#access to test client
        self.app_context=app.app_context() #allow to get app context in later on out test

        pass
    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
        pass