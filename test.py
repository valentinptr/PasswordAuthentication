import unittest

from PasswordAuthentication import add_user, delete_user, update_password
from dataset import *


class TestAddUser(unittest.TestCase):

    def test_typeDatabaseInt(self):
        self.assertEqual(add_user(0, 'auto20', 'auto20'), -1)

    def test_typeDatabaseFloat(self):
        self.assertEqual(add_user(0.5, 'auto20', 'auto20'), -1)

    def test_typeDatabaseChar(self):
        self.assertEqual(add_user('coucou', 'auto20', 'auto20'), -1)

    def test_typeUserInt(self):
        self.assertEqual(add_user(database_addUser_avant, 1, 'auto20'), -2)

    def test_typeUserFloat(self):
        self.assertEqual(add_user(database_addUser_avant, 0.2, 'auto20'), -2)

    def test_typeUserDict(self):
        self.assertEqual(add_user(database_addUser_avant, database_addUser_avant, 'auto20'), -2)

    def test_typePasswordInt(self):
        self.assertEqual(add_user(database_addUser_avant, 'auto20', 1), -3)

    def test_typePasswordFloat(self):
        self.assertEqual(add_user(database_addUser_avant, 'auto20', 0.2), -3)

    def test_typePasswordDict(self):
        self.assertEqual(add_user(database_addUser_avant, 'auto20', database_addUser_avant), -3)

    def test_KnownUser(self):
        self.assertEqual(add_user(database_addUser_avant, 'auto1', 'auto1'), -4)

    def test_NewUser(self):
        self.assertEqual(add_user(database_addUser_avant, 'auto20', 'auto20'), database_addUser_apres)


class TestUpdatePassword(unittest.TestCase):

    def test_typeDatabaseInt(self):
        self.assertEqual(update_password(0, 'auto20', 'auto20'), -1)

    def test_typeDatabaseFloat(self):
        self.assertEqual(update_password(0.5, 'auto20', 'auto20'), -1)

    def test_typeDatabaseChar(self):
        self.assertEqual(update_password('coucou', 'auto20', 'auto20'), -1)

    def test_typeUserInt(self):
        self.assertEqual(update_password(database_updatePassword_avant, 1, 'auto20'), -2)

    def test_typeUserFloat(self):
        self.assertEqual(update_password(database_updatePassword_avant, 0.2, 'auto20'), -2)

    def test_typeUserDict(self):
        self.assertEqual(update_password(database_updatePassword_avant, database_updatePassword_avant, 'auto20'), -2)

    def test_typePasswordInt(self):
        self.assertEqual(update_password(database_updatePassword_avant, 'auto20', 1), -3)

    def test_typePasswordFloat(self):
        self.assertEqual(update_password(database_updatePassword_avant, 'auto20', 0.2), -3)

    def test_typePasswordDict(self):
        self.assertEqual(update_password(database_updatePassword_avant, 'auto20', database_updatePassword_avant), -3)

    def test_NewUser(self):
        self.assertEqual(update_password(database_updatePassword_avant, 'autoXX', 'toto'), -4)

    def test_IdentiPassword(self):
        self.assertEqual(update_password(database_updatePassword_avant, 'auto1', 'auto1'), -5)

    def test_NewPassword(self):
        self.assertEqual(update_password(database_updatePassword_avant, 'admin', 'admin'), database_updatePassword_apres)


class TestDeleteUser(unittest.TestCase):

    def test_typeDatabaseInt(self):
        self.assertEqual(delete_user(0, 'auto20'), -1)

    def test_typeDatabaseFloat(self):
        self.assertEqual(delete_user(0.5, 'auto20'), -1)

    def test_typeDatabaseChar(self):
        self.assertEqual(delete_user('coucou', 'auto20'), -1)

    def test_typeUserInt(self):
        self.assertEqual(delete_user(database_deleteUser_avant, 1), -2)

    def test_typeUserFloat(self):
        self.assertEqual(delete_user(database_deleteUser_avant, 0.2), -2)

    def test_typeUserDict(self):
        self.assertEqual(delete_user(database_deleteUser_avant, database_deleteUser_avant), -2)

    def test_NewUser(self):
        self.assertEqual(delete_user(database_deleteUser_avant, 'autoXX'), -3)

    def test_DeleteUser(self):
        self.assertEqual(delete_user(database_deleteUser_avant, 'admin'), database_deleteUser_apres)


if __name__ == '__main__':
    unittest.main()
