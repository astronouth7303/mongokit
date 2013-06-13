"""
Replica Set integration with for MongoKit
Liyan Chang, liyan@filepicker.io
(same license as Mongokit)
"""

from pymongo.replica_set_connection import ReplicaSetConnection as PymongoReplicaSetConnection
from mongokit.connection import MongoKitConnection

class ReplicaSetConnection(MongoKitConnection, PymongoReplicaSetConnection):
    """ Replica Set support for MongoKit """

    def __init__(self, *args, **kwargs):
        """ The ReplicaSetConnection is a wrapper around the
            pymongo.replica_set_connection implementation.
        """
        super(ReplicaSetConnection, self).__init__(*args, **kwargs)

