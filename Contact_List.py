# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('*******')
        print('¡Not found!')
        print('*******')


def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(raw_input('''
            chose one

            [a] Add new contact
            [u] Update contact
            [f] Find contact
            [d] Delete contact
            [l] contact list
            [e] exit
        '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el tel del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'u':
            print('update contact')

        elif command == 'f':

            name = str(raw_input('Write name contact: '))

            contact_book.search(name)

        elif command == 'd':
            name = str(raw_input('Write name contact: '))

            contact_book.delete(name)

        elif command == 'l':

            contact_book.show_all()

        elif command == 'e':
            break
        else:
            print('Write name contact.')


if __name__ == '__main__':
    print('W E L C O M E')
    run()
