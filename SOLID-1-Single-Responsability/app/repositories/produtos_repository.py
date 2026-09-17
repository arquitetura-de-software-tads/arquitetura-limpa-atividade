from app.db.conexao_sqlite import ConexaoSqlite as db

class ProdutosRepository:
    @staticmethod
    def listar():
        sql = '''
            SELECT
                pro.id,
                pro.descricao,
                pro.preco_unitario,
                pro.quantidade_estoque,
                pro.categoria_id,
                cat.descricao as categoria

            FROM Produto pro

            INNER JOIN Categoria cat
                ON cat.id = pro.categoria_id

            ORDER BY pro.descricao
        '''
        registros = db.conexao().cursor().execute(sql).fetchall()
        return registros

    @staticmethod
    def incluir(produto):
        sql = '''
            INSERT INTO Produto (
                descricao, 
                preco_unitario, 
                quantidade_estoque, 
                categoria_id
            )
            VALUES(?, ?, ?, ?);
        '''
        conexao = db.conexao()
        conexao.cursor().execute(sql, (produto['descricao'], produto['preco_unitario'], produto['quantidade_estoque'], produto['categoria_id']))
        conexao.commit()

    @staticmethod
    def alterar(produto):
        sql = '''
            UPDATE Produto 
            SET descricao = ?, 
                preco_unitario = ?, 
                quantidade_estoque = ?, 
                categoria_id = ?
            WHERE id = ?
        '''
        conexao = db.conexao()
        conexao.cursor().execute(sql, (produto['descricao'], produto['preco_unitario'], produto['quantidade_estoque'], produto['categoria_id'], produto['id']))
        conexao.commit()

    @staticmethod
    def excluir(id):
        sql = '''
            DELETE FROM Produto WHERE id = ?
        '''
        conexao = db.conexao()
        conexao.cursor().execute(sql, (id,))
        conexao.commit()

    @staticmethod
    def buscar_por_id(id):
        sql = '''
            SELECT id, descricao, preco_unitario, quantidade_estoque, categoria_id FROM Produto WHERE id=?
        '''
        registro = db.conexao().cursor().execute(sql,(id,)).fetchone()
        return {'id': registro[0], 'descricao': registro[1], 'preco_unitario': registro[2], 'quantidade_estoque': registro[3], 'categoria_id': registro[4]}