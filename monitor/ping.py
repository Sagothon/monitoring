import sqlite3

def Ping(ip_table, other_config, command):

    data_base = sqlite3.connect('../stronka/db.sqlite3')
    c = data_base.cursor()

    c.execute('SELECT ip FROM monitoring_device')
    ip_list = c.fetchall()
    lista = []
    for i in ip_list:
        lista.append(i[0])