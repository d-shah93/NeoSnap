from __future__ import print_function
import contextlib
import datetime
import os
import six
import sys
import time
import unicodedata
import dropbox

"""
This is a test file to ensure uploading to dropbox is working properly
Currently it is set to Deep Shah's account.
To change the account, users create a personalized token by going to https://www.dropbox.com/developers/apps/create
and following instructions for a basic Dropbox API with full access
This is still a work in progress and there are more updates to come, making this more dynamic and eventually
implemented into the main Python file (unless it is agreed to keep as a separate file for simplicity)
"""


TOKEN = 'i0Uyu-jWN94AAAAAAAANb0HoXUi4GvgcnmEunB0sZwSUgME7p7eWEmCTgYRqgoR5'

def main():
    #The next few lines create a Unique file name to ensure there are no name conflicts but remove illegal characters
    # I know the pic is already named but I think is is a much better way, I took the naming convention from my phone's
    # pictures
    today = str(datetime.datetime.today())
    inTab = " -:"
    outTab = "_11"
    transTable = str.maketrans(inTab, outTab)
    today = today.translate(transTable)
    file = today[:19] + '.jpg'

    # Establish a connection to the Dropbox API using the supplied token
    dbx = dropbox.Dropbox(TOKEN)
    # This currently looks for a /Users/Current User/PycharmProjects/ folder, should be changed to reflect where the
    # pictures will be stored.
    folder = '~/PycharmProjects/'
    fullName = os.path.expanduser(folder)
    testPic = "testpic.jpg"
    if (os.path.exists(fullName + testPic)):
        path = fullName + testPic
        print(path)
    mode = dropbox.files.WriteMode.add
    with open(path, 'rb') as f:
        data = f.read()
    print(data)
    mtime = os.path.getmtime(path)
    print(mtime)
    # Need to change testPic to file (it will be a variable we pass in)
    dbPath = '/Photobooth/' + testPic
    # Currently for testing purposes, print to console if it worked.
    # Maybe create an email if there is an error in actual version?
    try:
        dbx.files_upload(data, dbPath, mode, False, datetime.datetime(*time.gmtime(mtime)[:6]), True)
    except dropbox.exceptions.ApiError as err:
        print('*** API Error', err)
        return None
    print('Successfully uploaded %s to %s ', testPic, dbPath)


if __name__ == '__main__':
    main()