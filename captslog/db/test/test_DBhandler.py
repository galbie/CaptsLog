import datetime
import random
import string
import bson.objectid

from captslog.db.DBHandler import DBHandlerClass

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
char_list = []
for c in lower_case:
    char_list.append(c)
for c in upper_case:
    char_list.append(c)
char_list.append(str(" "))


def generate_random_strings(length):
    x = 0
    str_val = ""
    while x < length:
        i = int(random.random() * 50)
        str_val = str(str_val) + str(char_list[i])
        x += 1
    return str_val


def test_insert_to_entries_table():
    test1_title = generate_random_strings(10)
    test1_tag = [generate_random_strings(4),
                 generate_random_strings(3)]
    test1_content = "File"
    test2_title = generate_random_strings(10)
    test2_tag = [generate_random_strings(4),
                 generate_random_strings(3)]
    test2_content = None
    test3_title = generate_random_strings(10)
    test3_tag = []
    test3_content = "File"
    test4_title = ""
    test4_tag = [generate_random_strings(4),
                 generate_random_strings(3)]
    test4_content = "File"  # TODO implement the new test cases
    db_handler = DBHandlerClass()
    # print "Test Case one with a non-Null Title "
    assert db_handler.insert_to_entries_table(
        generate_random_strings(10),
        [generate_random_strings(4),
         generate_random_strings(4)], "File")
    # print "Test Case two with a Null Title "
    assert not db_handler.insert_to_entries_table(
        "", [generate_random_strings(4),
             generate_random_strings(4)], "File")


def test_insert_to_user_table():
    db_handler = DBHandlerClass()
    test1_name = generate_random_strings(5)
    test1_username = generate_random_strings(10)
    test1_password = generate_random_strings(6)
    test2_name = str("")
    test2_username = generate_random_strings(10)
    test2_password = generate_random_strings(6)
    test3_name = generate_random_strings(5)
    test3_username = generate_random_strings(3)
    test3_password = generate_random_strings(6)
    test4_name = generate_random_strings(5)
    test4_username = generate_random_strings(10)
    test4_password = generate_random_strings(4)
    test5_name = generate_random_strings(5)
    test5_username = ""
    test5_password = generate_random_strings(6)
    # print "Running test case 1 with all valid inputs"
    value1 = db_handler.insert_to_user_table(test1_name,
                                             test1_username,
                                             test1_password)
    assert value1
    # print "Running test case 2 with invalid name and rest valid inputs"
    val2 = db_handler.insert_to_user_table(test2_name,
                                           test2_username,
                                           test2_password)
    assert not val2
    # print "Running test case 3 with " \
    # "invalid username and rest valid inputs"
    val3 = db_handler.insert_to_user_table(test3_name,
                                           test3_username,
                                           test3_password)
    assert not val3
    # print "Running test case 4 with invalid password and rest valid inputs"
    val4 = db_handler.insert_to_user_table(test4_name,
                                           test4_username,
                                           test4_password)
    assert not val4
    # print "Running test case 5 with Empty Username and rest valid inputs"
    val5 = db_handler.insert_to_user_table(test5_name,
                                           test5_username,
                                           test5_password)
    assert not val5


def test_search_entries_by_title():
    db_handler = DBHandlerClass()
    test1_title = generate_random_strings(10)
    test1_tag = [generate_random_strings(4),
                 generate_random_strings(3)]
    test1_content = "File"
    db_handler.insert_to_entries_table(test1_title, test1_tag,
                                       test1_content)
    result1 = db_handler.search_entries_by_title(test1_title)
    result2 = db_handler.search_entries_by_title(
        generate_random_strings(5))
    r1 = True
    rr1 = False
    r2 = False
    if not isinstance(result1, bool):
        r1 = False
        if result1["Title"] == test1_title:
            rr1 = True
        if result2 is None:
            r2 = True
    assert rr1 or r1
    assert r2 or r1


def test_search_entries_by_created_date():
    db_handler = DBHandlerClass()
    date = datetime.datetime.now()
    date1 = date - datetime.timedelta(days=1)
    date += datetime.timedelta(days=1)
    assert not db_handler.search_entries_by_created_date(date)
    assert db_handler.search_entries_by_created_date(date1)
    entry = db_handler.support_func_get_all(1)
    print isinstance(entry, bool)
    if entry is not None:
        result = db_handler.search_entries_by_created_date(
            entry[0]["Date_Created"])
        if isinstance(result, bool):
            assert result
        else:
            assert result is not None


def test_search_entries_by_modified_date():
    db_handler = DBHandlerClass()
    date = datetime.datetime.now()
    date += datetime.timedelta(days=1)
    assert not db_handler.search_entries_by_modified_date(date)
    entry = db_handler.support_func_get_all(1)
    if entry is not None:
        result = db_handler.search_entries_by_modified_date(
            entry[0]["Last_Modified"])
        if isinstance(result, bool):
            assert result
        else:
            assert result is not None


def test_update_entries():
    db_handler = DBHandlerClass()
    entry1 = {"Title": "Modified Title",
              "Date_Created": datetime.datetime.now(),
              "Last_Modified": datetime.datetime.now(),
              "Tags": ["MTag1", "MTag2"],
              "Content": "Content in Markdown File"}
    assert not db_handler.update_entries(
        bson.objectid.ObjectId("111111111111111111111111"), entry1)
    entry = db_handler.support_func_get_all(1)
    if entry is not None:
        entry = entry[0]
        entry["Title"] = str(entry["Title"]) + str("1")
        assert db_handler.update_entries(entry["_id"], entry)


def test_delete_entries():
    db_handler = DBHandlerClass()
    assert not db_handler.delete_entries(
        "111111111111111111111111")
    entry = db_handler.support_func_get_all(3)
    if entry is not None:
        entry = entry[0]
        assert db_handler.delete_entries(entry["_id"])
