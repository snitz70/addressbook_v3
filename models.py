from peewee import *
from collections import OrderedDict


#db = SqliteDatabase('addressbook.db')
db = MySQLDatabase('test', user='root', password='snitz086745')


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
    db.close()


def create_new_addressbook(name):
    """Create a new addressbook, or if the addressbook name already exists,
    return the existing one."""

    db.connect()
    try:
        return Addressbook.create(name=name)
    except IntegrityError:
        raise


def get_addressbooks(name=None):
    query = Addressbook.select()
    if name:
        query = query.where(Addressbook.name == name).get()

    return query


def delete_addressbook(name):
    addressbook = Addressbook.get(Addressbook.name == name)
    addressbook.delete_instance()


def add_contact(addressbook=None, name=None):
    """Add a new contact"""
    if not addressbook:
        raise ValueError
    if not name:
        raise ValueError

    return Contact(addressbook=addressbook, name=name)


def menu_loop():
    """Show the menu."""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))

        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

#
#
# menu = OrderedDict([
#     ('a', create_addressbook),
#     ('l', select_addressbook),
# ])


if __name__ == '__main__':
    initialize_db()
    menu_loop()
