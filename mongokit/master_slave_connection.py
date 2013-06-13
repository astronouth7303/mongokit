"""
Master-Slave integration with for MongoKit
Andreas Jung, info@zopyx.com
(same license as Mongokit)
"""

from pymongo.master_slave_connection import MasterSlaveConnection as PymongoMasterSlaveConnection
try:
    from pymongo import MongoClient as PymongoConnection
except ImportError:
    from pymongo import Connection as PymongoConnection

from mongokit import connection as MongoKitConnection

class MasterSlaveConnection(PymongoMasterSlaveConnection, MongoKitConnection):
    """ Master-Slave support for MongoKit """

    def __init__(self, master, slaves=[]):
        """ The MasterSlaveConnection is a wrapper around the
            pymongo.master_slave_connection implementation. The constructor accepts
            the connection parameter for the master MongoDB server and a non-empty
            list of connection parameters for one or more slaves.  The connection
            parameters are expressed as a dictionary where the keys match the
            signature of the constructor of a standard
            pymongo.connection.Connection instance ('host', 'port' etc.). For the
            'slaves' it is not necessary to specify the 'slave_okay' parameter
            (will be added internally automatically).

            The purpose of the MasterSlaveConnection is to hide a master-slave
            setup with one master and several slave servers. The slave
            server(s) will be used for read and write will be made to the
            master (and re-synced to the slave automatically as part of the
            master-slave setup).
        """

        self._databases = {}
        self._registered_documents = {}

        # I am the master
        if not isinstance(master, dict):
            raise TypeError('"master" must be a dict  containing pymongo.Connection parameters')
        master_connection = PyMongoConnection(**master)

        # You are my dirty slaves
        if not slaves:
            raise ValueError('You must specify at least one slave connection')

        slave_connections = list()
        for slave in slaves:
            if not isinstance(slave, dict):
                raise TypeError('"slaves" must be list of dicts containing pymongo.Connection parameters')
            slave['slave_okay'] = True
            slave_connections.append(PyMongoConnection(**slave))

        super(MasterSlaveConnection, self).__init__(master_connection, slave_connections)

