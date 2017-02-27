import unittest
from captslog.db.DBHandler import DBHandlerClass
import string
import random

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
char_list = []
for c in lower_case:
    char_list.append(c)
for c in upper_case:
    char_list.append(c)
char_list.append(str(" "))


class DBHandlerTestClasses(unittest.TestCase):
    def generate_random_strings(self, length):
        x = 0
        str_val = ""
        while x < length:
            i = int(random.random() * 50)
            str_val = str(str_val) + str(char_list[i])
            x += 1
        return str_val

    def test_insert_to_entries_table(self, ):
        db_handler = DBHandlerClass()
        test1_title = self.generate_random_strings(10)
        test2_title = str("")
        print "Test Case one with a non-Null Title "
        self.assertTrue(db_handler.insert_to_entries_table(test1_title, [self.generate_random_strings(4),
                                                                         self.generate_random_strings(4)], "File"),
                        "Test Failed")
        print "Test Case two with a Null Title "
        self.assertFalse(db_handler.insert_to_entries_table(test2_title, [self.generate_random_strings(4),
                                                                          self.generate_random_strings(4)], "File"),
                         "Test Failed")

    def test_insert_to_user_table(self):
        db_handler = DBHandlerClass()
        test1_name = self.generate_random_strings(5)
        test1_username = self.generate_random_strings(10)
        test1_password = self.generate_random_strings(6)
        test2_name = str("")
        test2_username = self.generate_random_strings(10)
        test2_password = self.generate_random_strings(6)
        test3_name = self.generate_random_strings(5)
        test3_username = self.generate_random_strings(3)
        test3_password = self.generate_random_strings(6)
        test4_name = self.generate_random_strings(5)
        test4_username = self.generate_random_strings(10)
        test4_password = self.generate_random_strings(4)
        print "Running test case 1 with all valid inputs"
        self.assertTrue(db_handler.insert_to_user_table(test1_name, test1_username, test1_password), "Test Failed")
        print "Running test case 2 with invalid name and rest valid inputs"
        self.assertFalse(db_handler.insert_to_user_table(test2_name, test2_username, test2_password), "Test Failed")
        print "Running test case 3 with invalid username and rest valid inputs"
        self.assertFalse(db_handler.insert_to_user_table(test3_name, test3_username, test3_password), "Test Failed")

        print "Running test case 4 with invalid password and rest valid inputs"
        self.assertFalse(db_handler.insert_to_user_table(test4_name, test4_username, test4_password), "Test Failed")

    def test_search_entries_by_title(self):
        print "NOT IMPLEMENTED"  # TODO implement test_search_entries_by_title

    def test_search_entries_by_created_date(self):
        print "NOT IMPLEMENTED"  # TODO implement test_search_entries_by_created_date

    def test_entries_by_modified_date(self):
        print "NOT IMPLEMENTED"  # TODO implement test_entries_by_modified_date

    def test_update_entries(self):
        print "NOT IMPLEMENTED"  # TODO implement test_update_entries

    def test_delete_entries(self):
        print "NOT IMPLEMENTED"  # TODO implement test_delete_entries


suite = unittest.TestLoader().loadTestsFromTestCase(DBHandlerTestClasses)
unittest.TextTestRunner(verbosity=2).run(suite)
