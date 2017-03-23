import pprint
from datetime import datetime
import pymongo
from pymongo import MongoClient
from bson import ObjectId
import time


class DBHandlerClass:
    client = MongoClient()
    db = client['Captains_Log_DB']

    def __init__(self):
        client = MongoClient()
        self.db = client['Captains_Log_DB']

    def insert_to_user_table(self, name, username, user_password):
        """Insert Data into the User_Table in the Database
        Args:
            name (str): Name of the User
            username (str): Username for future logins. should be at least 4 characters
            user_password (str): Password for future logins.

        Returns:
            bool: True for success or False for failure
        """

        if name == str(""):
            # print "Error!! name Can't be Empty"
            return False
        if username == str(""):
            # print "Error!! username Can't be Empty"
            return False
        if len(username) < 4:
            # print "Error!! username should be at least 4 characters"
            return False
        if len(user_password) < 5:
            # print "Error!! password should be at least 5 characters"
            return False
        entry = {"Name": name,
                 "Username": username,
                 "User_Password": user_password,
                 "First_Login_Date": datetime.now(),
                 "Last_Login_Date": datetime.now()}
        t = self.db["User_Table"]
        try:
            if t.insert_one(entry):
                return True
            else:
                return False
        except pymongo.errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return True

    def insert_to_entries_table(self, title, tags, content):
        """Insert Data into the Entries_Table in the Database

        Args:
            title (str): Title of the Journel Entry
            tags (list): Tangs for the Entry
            content(str): Content of the Entry

        return:
            int: 1 for success or 0 for failure

        """
        if title == str(""):
            # print "Error!! Title Can't be Empty"
            return False
        entry = {"Title": title,
                 "Date_Created": datetime.now(),
                 "Last_Modified": datetime.now(),
                 "Tags": tags,
                 "Content": content}
        # TODO reformat the 'content'
        # variable to include the Markup file (data = Binary(open(content).read()))
        t = self.db["Entries_Table"]
        try:
            if t.insert_one(entry):
                return True
            else:
                return False
        except pymongo.errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return True

    def search_entries_by_title(self, title):
        """Search For a Specified Title in the Entries_Table

        Args:
            title: the title you are searching for

        Return:
            collection: the search result

        """

        entries_table = self.db["Entries_Table"]
        try:
            result = entries_table.find_one({"Title": title})
            return result
        except pymongo.errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return False
            # TODO Modify to allow multiple results using find(),
            # TODO also find similar results which are not exact matches

    def search_entries_by_created_date(self, date):
        """Search For Entries created on the specified Date in the Entries_Table

        Args:
            date: the date you are searching for

        Return:
            collection: the search result

        """

        if date.date() <= datetime.now().date():
            entries_table = self.db["Entries_Table"]
            try:
                return entries_table.find_one(
                    {"Date_Created": date})
                # TODO Modify to allow multiple results using find()
            except pymongo.errors.ServerSelectionTimeoutError:
                print('ERROR : No connection could be made because'
                      ' the target machine actively refused it')
                return True
        return False

    def search_entries_by_modified_date(self, date):
        """Search For Entries modified on the specified Date in the Entries_Table

         Args:
            date: the date you are searching for

        Return:
            collection: the search result

        """
        if date.date() <= datetime.now().date():
            entries_table = self.db["Entries_Table"]
            try:
                return entries_table.find_one(
                    {"Last_Modified": date})  # TODO Modify to allow multiple results using find()
            except pymongo.errors.ServerSelectionTimeoutError:
                print('ERROR : No connection could be made because'
                      ' the target machine actively refused it')
                return True
        return False

    def update_entries(self, _id, vals):
        """Update entries in the Entries_Table

        Args:
            _id:  ObjectID of the entry you want to change
            vals: New values

        Return:
             int:1 if the update was successful. 0 if it fails
        """

        entries_table = self.db["Entries_Table"]
        try:
            if not entries_table.find_one({"_id": ObjectId(_id)}):
                # print "The specified entry does not Exist"
                return False
            vals["Last_Modified"] = datetime.now()
            entries_table.update_one({"_id": ObjectId(_id)},
                                     {"$set": vals})
            return True
        except pymongo.errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return False

    def delete_entries(self, _id):
        """Delete entries in the Entries_Table

        Args:
            _id:  Object ID of the entry you want to change

        Return:
            bool:1 if the delete was successful. 0 if it fails
        """

        entries_table = self.db["Entries_Table"]
        try:
            if not entries_table.find_one({"_id": ObjectId(_id)}):
                # print "The specified entry does not Exist"
                return False
            entries_table.delete_one({"_id": ObjectId(_id)})
            return True
        except pymongo.errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return False

    def support_func_get_all(self, lim):
        """This is just a support function which returns all the data in the Entries table upto a specified limit

        Args:
            lim: Max number of elements to be retrieved
        Return:
            collection: All the entries in the Entries_table uto the specified limit
        """

        try:
            entries_table = self.db["Entries_Table"]
            result = entries_table.find().limit(lim)
            print(result[0])
            return result
        except pymongo.errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  'the target machine actively refused it')
            return False
            # TODO Save the Entire text in the MArkdown file instead of the markdown file itself
