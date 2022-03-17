import mysql.connector as mc



banco = mc.connect(host='localhost', user='root', password='admin', database='bd_lista_tarefas')

#Insere dados na tabela   
def inserir_dados(tarefa, dataC, dataR, statusL):
    if banco.is_connected():
        cursor = banco.cursor()
        comando = 'insert into listagem(nomeTarefa, dataCriacao, dataRealizar, statusList) value(%s, %s, %s, %s)'
        valores = (tarefa, dataC, dataR, statusL)
        cursor.execute(comando, valores)
        banco.commit()


#Mostra dados da tabela 
def mostrar():
    if banco.is_connected():
        cursor = banco.cursor()
        comando = 'select * from listagem order by idLista desc'
        cursor.execute(comando)
        return cursor.fetchall()

#Exclui dados da tabela
def excluir(numId):
    if banco.is_connected():
        cursor = banco.cursor()
        apagar = 'delete from listagem where idLista = %s'
        valorId = (numId,)
        cursor.execute(apagar, valorId)
        banco.commit()

#Edita o campo status da tabela.
def editar(idNum):
    if banco.is_connected():
        cursor = banco.cursor()
        cmdEdicao = 'update listagem set statusList = 1 where idLista = %s'
        valores = (idNum,)
        cursor.execute(cmdEdicao, valores)
        banco.commit()

    