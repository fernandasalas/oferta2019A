import glob
import json
import mysql.connector

conexion = mysql.connector.connect(user='fer', password='pozole', database='proyecto')
cursor = conexion.cursor()
files = glob.glob('*.json')

carreras = {'INCO':1, 'INNI':2, 'INRO':3, 'INCE':4, 'INBI':5, 'IGFO':6}
periodo = {'16/01/19 - 31/05/19':1}

def existe_horas(academia):
    select = 'SELECT * from horas WHERE hora = %s'
    cursor.execute(select, (academia['Hora'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_horas(academia):
    insert = 'INSERT INTO horas(hora) VALUES(%s)'
    cursor.execute(insert, (academia['Hora'],))
    conexion.commit()
    return cursor.lastrowid

def existe_dias(academia):
    select = 'SELECT * from dias WHERE dias = %s'
    cursor.execute(select, (academia['Dias'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_dias(academia):
    insert = 'INSERT INTO dias(dias) VALUES(%s)'
    cursor.execute(insert, (academia['Dias'],))
    conexion.commit()
    return cursor.lastrowid

def existe_profesores(academia):
    select = 'SELECT * from profesores WHERE nombre = %s'
    cursor.execute(select, (academia['Profesor'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_profesores(academia):
    insert = 'INSERT INTO profesores(nombre) VALUES(%s)'
    cursor.execute(insert, (academia['Profesor'],))
    conexion.commit()
    return cursor.lastrowid

def existe_edificio(academia):
    select = 'SELECT * from edificio WHERE edificio = %s'
    cursor.execute(select, (academia['Edificio'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_edificio(academia):
    insert = 'INSERT INTO edificio(edificio) VALUES(%s)'
    cursor.execute(insert, (academia['Edificio'],))
    conexion.commit()
    return cursor.lastrowid

def existe_aula(academia, id_edif):
    select = 'SELECT * from aula WHERE aula = %s AND id_edificio = %s'
    cursor.execute(select, (academia['Aula'], id_edif))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_aula(academia, id_edif):
    insert = 'INSERT INTO aula(aula, id_edificio) VALUES(%s, %s)'
    cursor.execute(insert, (academia['Aula'], id_edif))
    conexion.commit()
    return cursor.lastrowid

def existe_materia(academia):
    select = 'SELECT * from materia WHERE clave = %s AND nombre = %s'
    cursor.execute(select, (academia['Clave'], academia['Materia']))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_materia(academia):
    insert = 'INSERT INTO materia(clave, nombre) VALUES(%s, %s)'
    cursor.execute(insert, (academia['Clave'], academia['Materia']))
    conexion.commit()
    return cursor.lastrowid

def get_id_aula(aula, edificio):
    select = 'SELECT * from aula WHERE aula = %s'
    cursor.execute(select, (aula,))

    rows = cursor.fetchall()
    for aula in rows:
        if aula[2] == get_id_edificio(edificio):
            return aula[0]

def get_id_edificio(edificio):
    select = 'SELECT id from edificio WHERE edificio = %s'
    cursor.execute(select, (edificio,))
    rows = cursor.fetchall()
    return rows[0][0]

def get_id_materia(clave, materia):
    select = 'SELECT id from materia WHERE clave = %s AND nombre = %s'
    cursor.execute(select, (clave, materia))
    rows = cursor.fetchall()
    return rows[0][0]

def get_id_dias(dias):
    select = 'SELECT id from dias WHERE dias = %s'
    cursor.execute(select, (dias,))
    rows = cursor.fetchall()
    return rows[0][0]

def get_id_horas(horas):
    select = 'SELECT id from horas WHERE hora = %s'
    cursor.execute(select, (horas,))
    rows = cursor.fetchall()
    return rows[0][0]

def get_id_profesores(profesores):
    select = 'SELECT id from profesores WHERE nombre = %s'
    cursor.execute(select, (profesores,))
    rows = cursor.fetchall()
    return rows[0][0]

def insertar_oferta(academia, id_mat, id_hora, id_dia, id_aul, id_profe):
    insert = 'INSERT INTO oferta(nrc, seccion, creditos, cupos, disponible, id_materia, id_horas, id_dias, id_aula, id_periodo, id_profesores, id_carrera) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert, (academia['NRC'], academia['Seccion'], academia['Creditos'], academia['Cupos'], academia['Disponible'], id_mat, id_hora, id_dia, id_aul, 1, id_profe, 6))
    conexion.commit()

with open('IGFO.json ', 'r') as archivo:
    academias= json.load(archivo)

    for academia in academias:
        id_edif = 0
        id_aul = 0
        id_mat=0
        id_profe=0
        id_dia=0
        id_hora=0
        if not existe_edificio(academia):
            id_edif=insertar_edificio(academia)
        else:
            id_edif = get_id_edificio(academia['Edificio'])

        if not existe_aula(academia, id_edif):
            id_aul= insertar_aula(academia, id_edif)
        else:
            id_aul = get_id_aula(academia['Aula'], academia['Edificio'])

        if not existe_materia(academia):
            id_mat=insertar_materia(academia)
        else:
            id_mat=get_id_materia(academia['Clave'], academia['Materia'])

        if not existe_profesores(academia):
            id_profe= insertar_profesores(academia)
        else:
            id_profe = get_id_profesores(academia['Profesor'])

        if not existe_dias(academia):
            id_dia = insertar_dias(academia)
        else:
            id_dia = get_id_dias(academia['Dias'])

        if not existe_horas(academia):
            id_hora = insertar_horas(academia)
        else:
            id_hora = get_id_horas(academia['Hora'])

        insertar_oferta(academia, id_mat, id_hora, id_dia, id_aul, id_profe)