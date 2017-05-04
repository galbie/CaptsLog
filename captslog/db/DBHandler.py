import pprint
from datetime import datetime
from pymongo import MongoClient
from pymongo import errors
from bson import ObjectId
from pymongo.errors import ConnectionFailure


class DBHandlerClass:
    def __init__(self):
        client = MongoClient(serverSelectionTimeoutMS=2000)
        self.connection_status = True
        try:
            # The ismaster command is cheap and does not require auth.
            client.admin.command('ismaster')
        except ConnectionFailure:
            print("ERROR : Connection Could Not Be established")
            self.connection_status = False
        self.db = client['Captains_Log_DB']

    def insert_to_user_table(self, name, username, user_password):
        """Insert Data into the User_Table in the Database
        Args:
            name (str): Name of the User
            username (str): Username for future logins. should be at least 4 characters
            user_password (str): Password for future logins.

        Returns:
            result(bool): True for success or False for failure
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
        if self.connection_status:
            if t.insert_one(entry):
                return True
        else:
            return True

    def insert_to_entries_table(self, title, tags, markdown_text):
        """Insert Data into the Entries_Table in the Database

        Args:
            title (str): Title of the Journel Entry
            tags (list): Tags for the Entry
            markdown_text(str): Content of the Entry(Markdown text)

        return:
            result(bool): True for success or False for failure

        """
        if title == str(""):
            # print "Error!! Title Can't be Empty"
            return False
        entry = {"Title": title,
                 "Date_Created": datetime.now(),
                 "Last_Modified": datetime.now(),
                 "Tags": tags,
                 "MarkdownFile": markdown_text}
        t = self.db["Entries_Table"]
        try:
            if t.insert_one(entry):
                return True
        except errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return True

    def search_entries_by_title(self, title):
        """Search For a Specified Title in the Entries_Table

        Args:
            title(str): the title you are searching for

        Return:
            result(collection): the search result

        """

        entries_table = self.db["Entries_Table"]
        try:
            result = entries_table.find_one({"Title": title})
            return result
        except errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return False
            # TODO Modify to allow multiple results using find(),
            # TODO also find similar results which are not exact matches

    def search_entries_by_created_date(self, date):
        """Search For Entries created on the specified Date in the Entries_Table

        Args:
            date(datetime): the date you are searching for

        Return:
            result(collection): the search result

        """

        if date.date() <= datetime.now().date():
            entries_table = self.db["Entries_Table"]
            try:
                return entries_table.find(
                    {"Date_Created": date})
            except errors.ServerSelectionTimeoutError:
                print('ERROR : No connection could be made because'
                      ' the target machine actively refused it')
                return True
        return False

    def search_entries_by_id(self, id):
        """Search For Entries created on the specified Date in the Entries_Table

        Args:
            id(string): the objectID you are searching for

        Return:
            result(collection): the search result

        """

        entries_table = self.db["Entries_Table"]
        try:
            return entries_table.find(
                {"_id": ObjectId(id)})
        except errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return True
        return False

    def search_entries_by_modified_date(self, date):
        """Search For Entries modified on the specified Date in the Entries_Table

        Args:
            date(datetime): the date you are searching for

        Return:
            result(collection): the search result

        """
        if date.date() <= datetime.now().date():
            entries_table = self.db["Entries_Table"]
            try:
                return entries_table.find(
                    {"Last_Modified": date})
            except errors.ServerSelectionTimeoutError:
                print('ERROR : No connection could be made because'
                      ' the target machine actively refused it')
                return True
        return False

    def update_entries(self, _id, vals):
        """Update entries in the Entries_Table

        Args:
            _id(ObjectId):  ObjectID of the entry you want to change
            vals(collection): New values

        Return:
            result(bool):True if the update was successful. False if it fails
        """

        entries_table = self.db["Entries_Table"]
        try:
            vals["Last_Modified"] = datetime.now()
            if not entries_table.find_one({"_id": ObjectId(_id)}):
                return False
            entries_table.update_one({"_id": ObjectId(_id)},
                                     {"$set": vals})
            return True
        except errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return False

    def delete_entries(self, _id):
        """Delete entries in the Entries_Table

        Args:
            _id(str):  Object ID of the entry you want to change

        Return:
            result(bool):true if the delete was successful. false if it fails
        """

        entries_table = self.db["Entries_Table"]
        try:
            if not entries_table.find_one({"_id": ObjectId(_id)}):
                # print "The specified entry does not Exist"
                return False
            entries_table.delete_one({"_id": ObjectId(_id)})
            return True
        except errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  ' the target machine actively refused it')
            return False

    def get_all(self):
        """

        Returns:
            result(collection): all elements in the Entries Table
        """

        try:
            entries_table = self.db["Entries_Table"]
            result = entries_table.find()
            print result[0]
            return result
        except errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  'the target machine actively refused it')
            return None

    def support_func_get_all(self, lim):
        """

        Args:
            lim(int): number of items you need to get from the database

        Returns:
            result(collection): all elements in the
        """

        try:
            entries_table = self.db["Entries_Table"]
            result = entries_table.find().limit(lim)
            print result[0]
            return result
        except errors.ServerSelectionTimeoutError:
            print('ERROR : No connection could be made because'
                  'the target machine actively refused it')
            return None
