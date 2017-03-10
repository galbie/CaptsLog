import datetime
import random
import string
import unittest

from bson import ObjectId

from source.db.DBHandler import DBHandlerClass

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
        test1_title = self.generate_random_strings(10)
        test1_tag = [self.generate_random_strings(4),
                     self.generate_random_strings(3)]
        test1_content = "File"
        test2_title = self.generate_random_strings(10)
        test2_tag = [self.generate_random_strings(4),
                     self.generate_random_strings(3)]
        test2_content = None
        test3_title = self.generate_random_strings(10)
        test3_tag = []
        test3_content = "File"
        test4_title = ""
        test4_tag = [self.generate_random_strings(4),
                     self.generate_random_strings(3)]
        test4_content = "File"  # TODO implement the new test cases
        db_handler = DBHandlerClass()
        print "Test Case one with a non-Null Title "
        self.assertTrue(
            db_handler.insert_to_entries_table(
                self.generate_random_strings(10),
                [self.generate_random_strings(4),
                 self.generate_random_strings(4)], "File"), "Test Failed")
        print "Test Case two with a Null Title "
        self.assertFalse(
            db_handler.insert_to_entries_table(
                "", [self.generate_random_strings(4),
                     self.generate_random_strings(4)], "File")
            , "Test Failed")

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
        test5_name = self.generate_random_strings(5)
        test5_username = ""
        test5_password = self.generate_random_strings(6)
        print "Running test case 1 with all valid inputs"
        self.assertTrue(db_handler.insert_to_user_table(test1_name,
                                                        test1_username,
                                                        test1_password),
                        "Test Failed")
        print "Running test case 2 with invalid name and rest valid inputs"
        self.assertFalse(db_handler.insert_to_user_table(test2_name,
                                                         test2_username,
                                                         test2_password),
                         "Test Failed")
        print "Running test case 3 with invalid username and rest valid inputs"
        self.assertFalse(db_handler.insert_to_user_table(test3_name,
                                                         test3_username,
                                                         test3_password),
                         "Test Failed")
        print "Running test case 4 with invalid password and rest valid inputs"
        self.assertFalse(db_handler.insert_to_user_table(test4_name,
                                                         test4_username,
                                                         test4_password),
                         "Test Failed")
        print "Running test case 5 with Empty Username and rest valid inputs"
        self.assertFalse(db_handler.insert_to_user_table(test5_name,
                                                         test5_username,
                                                         test5_password),
                         "Test Failed")

    def test_search_entries_by_title(self):
        db_handler = DBHandlerClass()
        test1_title = self.generate_random_strings(10)
        test1_tag = [self.generate_random_strings(4),
                     self.generate_random_strings(3)]
        test1_content = "File"
        db_handler.insert_to_entries_table(test1_title, test1_tag,
                                           test1_content)
        result1 = db_handler.search_entries_by_title(test1_title)
        result2 = db_handler.search_entries_by_title(
            self.generate_random_strings(5))

        self.assertTrue(result1["Title"] == test1_title, "Test Failed")
        # self.assertTrue(result2 == None, "Test Failed")

    def test_search_entries_by_created_date(self):
        db_handler = DBHandlerClass()
        date = datetime.datetime.now()
        date += datetime.timedelta(days=1)
        self.assertTrue(
            int(db_handler.search_entries_by_created_date(date)) == int(0),
            "Test Failed")
        entry = db_handler.support_func_get_all(1)[0]
        self.assertTrue(not (db_handler.search_entries_by_created_date(
            entry["Date_Created"]) == 0), "Test Failed")

    def test_search_entries_by_modified_date(self):
        db_handler = DBHandlerClass()
        date = datetime.datetime.now()
        date += datetime.timedelta(days=1)
        self.assertTrue(
            int(db_handler.search_entries_by_modified_date(date)) == int(0),
            "Test Failed")
        entry = db_handler.support_func_get_all(1)[0]
        self.assertTrue(not (db_handler.search_entries_by_modified_date(
            entry["Last_Modified"]) == 0),
                        "Test Failed")

    def test_update_entries(self):
        db_handler = DBHandlerClass()
        entry = db_handler.support_func_get_all(1)[0]
        entry["Title"] = str(entry["Title"]) + str("1")
        self.assertTrue(db_handler.update_entries(
            entry["_id"], entry), "Update Test Failed")
        self.assertFalse(db_handler.update_entries(
            ObjectId("111111111111111111111111"), entry),
            "Update Test Failed")

    def test_delete_entries(self):
        db_handler = DBHandlerClass()
        entry = db_handler.support_func_get_all(3)[0]
        self.assertTrue(db_handler.delete_entries(
            entry["_id"]), "Delete Test Failed")
        self.assertFalse(
            db_handler.delete_entries("111111111111111111111111"),
            "Delete Test Failed")


suite = unittest.TestLoader().loadTestsFromTestCase(DBHandlerTestClasses)
unittest.TextTestRunner(verbosity=2).run(suite)
