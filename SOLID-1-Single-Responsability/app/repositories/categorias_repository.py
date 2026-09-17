from app.db.conexao_sqlite import ConexaoSqlite as db

class CategoriasRepository:
    @staticmethod
    def listar():
        sql = '''
            SELECT  id, 
                    descricao
            FROM Categoria 
            ORDER BY descricao
        '''
        registros = db.conexao().cursor().execute(sql).fetchall()
        return registros

    @staticmethod
    def incluir(descricao):
        sql = '''
            INSERT INTO Categoria(descricao) VALUES(?)
        '''
        conexao = db.conexao()
        conexao.cursor().execute(sql, (descricao,))
        conexao.commit()

    @staticmethod
    def alterar(id, descricao):
        sql = '''
            UPDATE Categoria SET descricao=? WHERE id=?
        '''
        conexao = db.conexao()
        conexao.cursor().execute(sql, (descricao, id))
        conexao.commit()

    @staticmethod
    def excluir(id):
        sql_verificar = '''
        SELECT COUNT(*)
        FROM Produto
        WHERE categoria_id = ?
    '''
        quantidade = db.conexao().cursor().execute(sql_verificar,(id,)).fetchone()[0]
        if quantidade > 0:
            raise Exception('Não é possível excluir esta categoria porque existem produtos vinculados.')
        
        sql = '''
            DELETE FROM Categoria WHERE id=?
        '''
        conexao = db.conexao()
        conexao.cursor().execute(sql, (id,))
        conexao.commit()

    @staticmethod
    def buscar_por_id(id):
        sql = '''
            SELECT id, descricao FROM Categoria WHERE id=?
        '''
        registro = db.conexao().cursor().execute(sql,(id,)).fetchone()
        return {'id': registro[0], 'descricao': registro[1]}