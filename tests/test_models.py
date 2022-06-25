"""
Test cases for YourResourceModel Model

"""
import os
import logging
import unittest
from datetime import date
from venv import create
from werkzeug.exceptions import NotFound
from service.models import DataValidationError, Shopcart, db
from service import app
from tests.factories import ShopcartFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/testdb"
)

######################################################################
#  <your resource name>   M O D E L   T E S T   C A S E S
######################################################################


class TestYourResourceModel(unittest.TestCase):
    """Test Cases for YourResourceModel Model"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Shopcart.init_db(app)
        

    @classmethod
    def tearDownClass(cls):
        """This runs once after the entire test suite"""
        db.session.close()

    def setUp(self):
        """This runs before each test"""
        db.session.query(Shopcart).delete()  # clean up the last tests
        db.session.commit()

    def tearDown(self):
        """This runs after each test"""
        db.session.remove()
        

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_XXXX(self):
        """It should always be true"""
        self.assertTrue(True)

    def test_addShopCart(self):
        '''Try to create a new shopcart and add it to the table'''
        createdShopCart = Shopcart(2, "hello world")
        createdShopCart.create()
        shopCart = Shopcart.find(2)
        self.assertTrue(shopCart.id==createdShopCart.id)
        self.assertTrue(shopCart.name==createdShopCart.name)

