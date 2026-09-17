import sqlite3

class ConexaoSqlite:
    @staticmethod
    def conexao():
        conexao = sqlite3.connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;")
        return conexao