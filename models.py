from peewee import *
from collections import OrderedDict


db = SqliteDatabase('addressbook.db')


class Addressbook(Model):
    name = CharField(unique=True)

    class Meta:
        database = db


class Contact(Model):
    name = CharField(unique=False)
    addressbook = ForeignKeyField(Addressbook, related_name='contacts')

    class Meta:
        database = db


def initialize_db():
    """connect to the database and create any tables if they do no exist."""
    db.connect()
    db.create_tables([Addressbook, Contact], safe=True)


def initialize_addressbook(name):
    """Create a new addressbook, or if the addressbook name already exists,
    return the existing one."""

    try:
        return Addressbook(name=name)
    except IntegrityError:
        return Addressbook.get(Addressbook.name == name)


def add_contact(addressbook=None, name=None):
    """Add a new contact"""
    if not addressbook:
        raise ValueError
    if not name:
        raise ValueError

    return Contact(addressbook=addressbook, name=name)


def list_addressbooks():
    """list all available addressbooks"""


def menu_loop():
    """Show the menu."""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit")
        for key, value in menu.items():
            print('{}'.format(key))

        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()



menu = OrderedDict([
    ('a) Select addressbook', initialize_db),
    ('l) List addressbooks', list_addressbooks),
])


if __name__ == '__main__':
    initialize_db()
    menu_loop()
