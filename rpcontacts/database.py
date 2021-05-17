from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createContactsTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec()

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createContactsTable()
    return True
