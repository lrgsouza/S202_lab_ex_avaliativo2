# from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json as wj




if __name__ == '__main__':
    db = Graph(uri='bolt://44.202.73.42:7687', user='neo4j', password='sentries-blanks-debts')

    # ==================================== Questão 01 ====================================
    # A
    wj(db.execute_query("MATCH(t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf;"),'1A')

    # B
    wj(db.execute_query("MATCH(t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf;"),'1B')

    # C
    wj(db.execute_query("MATCH(c:City) RETURN c.name"),'1C')

    # D
    wj(db.execute_query("MATCH(s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address"),'1D')

    # ==================================== Questão 02 ====================================
    # A
    wj(db.execute_query("MATCH(t:Teacher) return MIN(t.ano_nasc), MAX(t.ano_nasc)"),'2A')

    # B
    wj(db.execute_query("MATCH(c:City) return AVG(c.population)"),'2B')

    # C
    wj(db.execute_query("MATCH(c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A')"),'2C')

    # D
    wj(db.execute_query("MATCH(t:Teacher) RETURN SUBSTRING(t.name, 3, 1)"),'2D')


    # ==================================== Questão 03 ====================================

    # A
    class TeacherCRUD():

        def __init__(self):
            self.db = Graph(uri='bolt://44.202.73.42:7687', user='neo4j', password='sentries-blanks-debts')

        def create(self, name, ano_nasc, cpf):  # cria um Teacher`
            return wj(self.db.execute_query('CREATE (t:Teacher {name:$name, ano_nasc:$ano_nasc, cpf:$cpf}) return t',
                                            {'name': name, 'ano_nasc': ano_nasc,
                                             'cpf': cpf}), 'create')
        def read(self, name):  # retorna apenas um Teacher`
            return wj(self.db.execute_query('MATCH (t:Teacher {name:$name}) return t',
                                            {'name': name}), 'read')
        def update(self, name, newCpf):  # atualiza cpf com base no name`
            return wj(self.db.execute_query('MATCH (t:Teacher {name:$name}) SET t.cpf = $cpf RETURN t',
                                            {'name': name, 'cpf':newCpf}), 'update')
        def delete(self, name):  # deleta Teacher com base no name`
            return wj(self.db.execute_query('MATCH (t:Teacher {name:$name}) DELETE t',
                                            {'name': name}), 'delete')
    # instanciando objeto
    TCRUD = TeacherCRUD()

    # B
    TCRUD.create('Chris Lima',1956,'189.052.396-66')

    # C
    TCRUD.read('Chris Lima')

    # D
    TCRUD.update('Chris Lima','162.052.777-77')

