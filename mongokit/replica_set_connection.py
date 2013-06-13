"""
Replica Set integration with for MongoKit
Liyan Chang, liyan@filepicker.io
(same license as Mongokit)
"""

from pymongo.replica_set_connection import ReplicaSetConnection as PymongoReplicaSetConnection
from mongokit import connection as MongoKitConnection

class ReplicaSetConnection(PymongoReplicaSetConnection, MongoKitConnection):
    """ Replica Set support for MongoKit """

    def __init__(self, *args, **kwargs):
        """ The ReplicaSetConnection is a wrapper around the
            pymongo.replica_set_connection implementation.
        """

        self._databases = {}
        self._registered_documents = {}

        super(ReplicaSetConnection, self).__init__(*args, **kwargs)

