import sqlite3
con = sqlite3.connect('mywebsite.db')
cur = con.cursor()

def studentdetails():
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"select * from student"
    cur.execute(sql)
    s = cur.fetchall()
    return s

def departmentdetails():
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"select * from department"
    cur.execute(sql)
    d = cur.fetchall()
    return d

def hoddetails():
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"select * from hod"
    cur.execute(sql)
    h = cur.fetchall()
    return h

def studentsingledetails(idv):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"select * from student where id = {idv}"
    cur.execute(sql)
    s = cur.fetchall()
    return s

def departmentsingledetails(idv):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"select * from department where department_id = {idv}"
    cur.execute(sql)
    d = []
    for a in cur.fetchall():
        d.append(a)
    return d

def hodsingledetails(idv):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"select * from hod where hod_id = {idv}"
    cur.execute(sql)
    h = []
    for a in cur.fetchall():
        h.append(a)
    return h

def deleteallstudent():
    sql = "delete from student"
    cur.execute(sql)
    con.commit()
    cur.close()
    return "successfully deleted all the students"

def deletealldepartment():
    sql = "delete from department"
    cur.execute(sql)
    con.commit()
    cur.close()
    return "successfully deleted all the departments"

def deleteallhod():
    sql = "delete from hod"
    cur.execute(sql)
    con.commit()
    cur.close()
    return "successfully deleted all the hod"

def hodinsert(hod_name,phonenumber):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"insert into hod(hod_name,phonenumber)values('{hod_name}','{phonenumber}')"
    print(sql)
    cur.execute(sql)
    con.commit()
    cur.close()
    return "successfully inserted"


def studentinsert(std_name,m1,m2,m3,dept,location,gender,phonenumber,dob):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql=f"insert into student(name,m1,m2,m3,dept,location,gender,phonenumber,dob)values('{std_name}',{m1},{m2},{m3},'{dept}','{location}','{gender}',{phonenumber},'{dob}')"
    print(sql)
    cur.execute(sql)
    con.commit()
    cur.close()
    return "sucessfully inserted"


def deptinsert(department_name,hod_id):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"insert into department(department_name,hod_id)values('{department_name}','{hod_id}')"
    print(sql)
    cur.execute(sql)
    con.commit()
    cur.close()
    return "successfully inserted"


def studentsingledelete(idv):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"delete from student where id = {idv}"
    cur.execute(sql)
    con.commit()
    cur.close()
    return "student successfully deleted"

def departmentsingledelete(idv):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"delete from department where department_id = {idv}"
    cur.execute(sql)
    con.commit()
    cur.close()
    return "department successfully deleted"

def hodsingledelete(idv):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql = f"delete from hod where hod_id = {idv}"
    cur.execute(sql)
    con.commit()
    cur.close()
    return "hod successfully deleted"

def studentupdate(*args):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql=f"update student set name='{args[1]}',m1={args[2]},m2={args[3]},m3={args[4]},dept='{args[5]}',location='{args[6]}',gender='{args[7]}',phonenumber='{args[8]}',dob='{args[9]}' where id={args[0]}"
    print(sql)
    cur.execute(sql)
    con.commit()
    cur.close()
    return "student successfully updated"

def departmentupdate(*args):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql=f"update department set department_name='{args[1]}',hod_id={args[2]} where department_id={args[0]}"
    print(sql)
    cur.execute(sql)
    con.commit()
    cur.close()
    return "department successfully updated"

def hodupdate(*args):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    sql=f"update hod set hod_name='{args[1]}',phonenumber='{args[2]}' where hod_id={args[0]}"
    print(sql)
    cur.execute(sql)
    con.commit()
    cur.close()
    return "hod successfully updated"

