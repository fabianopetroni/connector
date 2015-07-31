import os
import sys

# Constant for verify connection
FTRACK_CONNECTED = False

sys.path += ["D:/server/apps/3rdparty/ftrack-python"]

os.environ['FTRACK_SERVER'] = 'https://cas.ftrackapp.com'
os.environ['LOGNAME'] = 'fabianopetroni'
import ftrack

FTRACK_CONNECTED = True


class Connector(object):
    """docstring for Connector"""
    def __init__(self, user=None):
        super(Connector, self).__init__()

        self.user = user
        self.userDetails = None
        self.userTasks = None

        if not self.user:
            self.user = os.environ['USERNAME']

    def getUser(self):
        return self.user

    def setUser(self, value):
        self.user = value

    def connect(self):

        os.environ['LOGNAME'] = self.user
        if FTRACK_CONNECTED is True:
            print 'Connecion Succesful !'

    def getUserDetails(self):

        self.userDetails = ftrack.getUser(self.user)
        return self.userDetails

    def getUserTasks(self):

        userDetail = self.getUserDetails()

        self.userTasks = userDetail.getTasks()
        return self.userTasks
