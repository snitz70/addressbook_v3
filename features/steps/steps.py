from behave import *
from hamcrest import *
import peewee

import models

db = peewee.MySQLDatabase('test', user='root', password='snitz086745')


def empty_database():
    db.execute_sql('DROP TABLE IF EXISTS contact, addressbook')
    models.initialize_db()


@given("I have no addressbooks in database")
def clear_database(context):
    empty_database()


@given("I already have addressbook '{addressbook_name}' saved")
def create_addressbook_for_duplicate(context, addressbook_name):
    empty_database()
    models.create_new_addressbook(addressbook_name)


@when("I create a new addressbook called '{addressbook_name}'")
def create_new_addressbook(context, addressbook_name):
    context.addressbook_name = addressbook_name


@when('I ask for a list of existing addressbooks')
def get_existing_addressbooks(context):
    context.addressbooks = models.get_addressbooks()


@when("I ask to delete addressbook '{addressbook_name}'")
def delete_addressbook(context, addressbook_name):
    models.delete_addressbook(addressbook_name)


@when('the addressbook contains no contacts')
def check_contacts(context):
    pass


@then('the addressbook should be deleted')
def check_if_deleted(context):
    pass


@then('I should get a list')
def check_list_of_addressbooks(context):
    assert len(context.addressbooks) > 0


@then("the addressbook should be saved to the database")
def check_new_addressbook_was_saved(context):
    models.create_new_addressbook(context.addressbook_name)
    assert_that(models.get_addressbooks(context.addressbook_name).name,
                equal_to(context.addressbook_name))


@then("I should receive a warning")
def check_for_warning(context):
    assert_that(
        calling(models.create_new_addressbook).with_args(context.addressbook_name),
        raises(peewee.IntegrityError))