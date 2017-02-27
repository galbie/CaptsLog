import unittest
import time
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
        print "NOT IMPLEMENTED"  # TODO implement test_insert_to_user_table

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
