import pprint
import pymongo


class DBHandler(object):
    from pymongo import MongoClient
    client = MongoClient()
    db = client['Captains_Log_DB']

    def insert_to_user_table(self, name, username, user_password, first_login_date, last_login_date):
        """Insert Data into the User_Table in the Database
        Args:
            name (str): Name of the User
            username (str): Username for future logins.
            user_password (str): Password for future logins.
            first_login_date (date): Date the user was first created
            last_login_date (date): Last Login date of the user

        Returns:
            bool: True for success or False for failure

        """
        entry = {"Name": name,
                 "Username": username,
                 "User_Password": user_password,
                 "First_Login_Date": first_login_date,
                 "Last_Login_Date": last_login_date}
        t = DBHandler.db["User_Table"]
        t.insert_one(entry)

    def insert_to_entries_table(self, title, date_created, last_modified, tags, content):
        """Insert Data into the Entries_Table in the Database

        Args:
            title (str): Title of the Journel Entry
            date_created (date): Date the Entry was created
            last_modified (date): Date the Entry was last Modified
            tags (list): Tangs for the Entry
            content(str): Content of the Entry

        return:
            bool: True for success or False for failure

        """

        entry = {"Title": title,
                 "Date_Created": date_created,
                 "Last_Modified": last_modified,
                 "Tags": tags,
                 "Content": content}  # TODO reformat the 'content' variable to include the Markup file
        t = DBHandler.db["Entries_Table"]
        t.insert_one(entry)

    def search_entries_by_title(self, title):
        """Search For a Specified Title in the Entries_Table

        Args:
            title: the title you are searching for

        Return:
            dict: the search result

        """

        entries_table = DBHandler.db.Entries
        return entries_table.find_one({"Title": title})  # TODO Modify to allow multiple results using find(),
        # TODO also find similar results which are not exact matches

    def search_entries_by_created_date(self, date):
        """Search For Entries created on the specified Date in the Entries_Table

        Args:
            date: the date you are searching for

        Return:
            dict: the search result

        """

        entries_table = DBHandler.db.Entries
        return entries_table.find_one({"Date_Created": date})  # TODO Modify to allow multiple results using find()

    def search_entries_by_modified_date(self, date):
        """Search For Entries modified on the specified Date in the Entries_Table

         Args:
            date: the date you are searching for

        Return:
            dict: the search result

        """

        entries_table = DBHandler.db.Entries
        return entries_table.find_one({"Date_Modified": date})  # TODO Modify to allow multiple results using find()

    def update_entries(self, id, vals):
        """Update entries in the Entries_Table

        Args:
            id:  ID of the entry you want to change
            vals: New values

        Return:
        """
        entries_table = DBHandler.db.Entries
        entries_table.update({"_id": id}, {"$set": vals})
