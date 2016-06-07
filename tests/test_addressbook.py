import pytest

import models

def test_addressbook_gets_created():
    name = 'new addressbook1'
    addressbook = models.initialize_addressbook(name)
    assert addressbook.name == name


def test_contacts_get_added_to_addressbook():
    addressbook_name = 'new addressbook1'
    addressbook = models.Addressbook(name=addressbook_name)
    contact_name = 'Brian Snyder'
    contact = models.add_contact(addressbook, contact_name)
    assert contact.name == contact_name
    assert contact.addressbook.id == addressbook.id


def test_blank_addressbook_for_new_contact():
    contact_name = 'Brian Snyder'
    with pytest.raises(ValueError):
        contact = models.add_contact(name=contact_name)


def test_blank_name_for_new_contact():
    with pytest.raises((ValueError)):
        contact = models.add_contact(addressbook='testing')






