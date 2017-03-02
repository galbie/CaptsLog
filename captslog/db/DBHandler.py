import pprint
from datetime import datetime

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
                 "First_Login_Date": time.strftime("%x"),
                 "Last_Login_Date": time.strftime("%x")}
        t = self.db["User_Table"]
        if t.insert_one(entry):
            return True

        return False

    def insert_to_entries_table(self, title, tags, content):
        """Insert Data into the Entries_Table in the Database

        Args:
            title (str): Title of the Journel Entry
            tags (list): Tangs for the Entry
            content(str): Content of the Entry

        return:
            bool: True for success or False for failure

        """
        if title == str(""):
            # print "Error!! Title Can't be Empty"
            return False
        entry = {"Title": title,
                 "Date_Created": time.strftime("%x"),
                 "Last_Modified": time.strftime("%x"),
                 "Tags": tags,
                 "Content": content}  # TODO reformat the 'content' variable to include the Markup file (data = Binary(open(content).read()))
        t = self.db["Entries_Table"]
        if t.insert_one(entry):
            return True

        return False

    def search_entries_by_title(self, title):
        """Search For a Specified Title in the Entries_Table

        Args:
            title: the title you are searching for

        Return:
            dict: the search result

        """

        entries_table = self.db["Entries_Table"]
        result = entries_table.find_one({"Title": title})
        return result  # TODO Modify to allow multiple results using find(),
        # TODO also find similar results which are not exact matches

    def search_entries_by_created_date(self, date):
        """Search For Entries created on the specified Date in the Entries_Table

        Args:
            date: the date you are searching for

        Return:
            dict: the search result

        """
        d = datetime.strptime(date, '%m/%d/%y')
        if d > datetime.now():
            return False
        entries_table = self.db["Entries_Table"]
        return entries_table.find_one({"Date_Created": date})  # TODO Modify to allow multiple results using find()

    def search_entries_by_modified_date(self, date):
        """Search For Entries modified on the specified Date in the Entries_Table

         Args:
            date: the date you are searching for

        Return:
            dict: the search result

        """

        entries_table = self.db["Entries_Table"]
        return entries_table.find_one({"Date_Modified": date})  # TODO Modify to allow multiple results using find()

    def update_entries(self, _id, vals):
        """Update entries in the Entries_Table

        Args:
            id:  ObjectID of the entry you want to change
            vals: New values

        Return:
        """
        entries_table = self.db["Entries_Table"]
        entries_table.update({"_id": ObjectId(_id)}, {"$set": vals})

    def delete_entries(self, _id):
        """Delete entries in the Entries_Table

        Args:
            id:  Object ID of the entry you want to change

        Return:
        """
        entries_table = self.db["Entries_Table"]
        entries_table.remove_one({"_id": ObjectId(_id)})


dbh = DBHandlerClass()
