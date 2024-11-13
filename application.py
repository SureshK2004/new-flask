from flask import *
from crud_operations import *
app = Flask(__name__)

@app.route("/")
def homepageopen():
    name = "Shajith"
    return render_template("Home_page.html",name = name)

@app.route("/addstudent")
def openstudentpage():
    return render_template("student.html")

@app.route("/adddepartment")
def opendepartmentpage():
    return render_template("department.html")

@app.route("/addhod")
def openhodpage():
    return render_template("hod.html")

@app.route('/savehodtodb',methods=['POST','GET'])
def inserthod():
    if request.method=='POST':
        h=request.form['hname']
        p=request.form['hphone']
        print(h,p)
        msg=hodinsert(h,p)
    return render_template("sucesspage.html",msg=msg)

@app.route('/savestudenttodb',methods=['POST','GET'])
def insertstudent():
    if request.method=='POST':
        try:
            sn = request.form["sname"]
            sm1 = request.form["sm1"]
            sm2 = request.form["sm2"]
            sm3 = request.form["sm3"]
            sd = request.form["dname"]
            sl = request.form["locations"]
            sg = request.form["gender"]
            sp = request.form["sphone"]
            sdo = request.form["sdob"]
            print(sn, sm1, sm2, sm3, sd, sl, sg, sp, sdo)
            msg = studentinsert(sn, sm1, sm2, sm3, sd, sl, sg, sp, sdo)
            #return render_template("sucesspage.html", msg=msg)
        except:
            msg = "not successful"
            #return render_template("sucesspage.html",msg = msg)
        else:
            print("I will run whenever try runs")
        finally:
            return render_template("sucesspage.html",msg = msg)


@app.route('/savedepttodb',methods=['POST','GET'])
def insertdepartment():
    if request.method=='POST':
        dn=request.form['departments']
        hi=request.form['hiname']
        print(dn,hi)
        msg=deptinsert(dn,hi)
    return render_template("sucesspage.html",msg=msg)

@app.route('/viewstudent')
def viewstudentdetails():
    rows = studentdetails()
    print(rows)
    return render_template('view_student.html',rows = rows)

@app.route('/viewhod')
def viewhoddetails():
    rows = hoddetails()
    print(rows)
    return render_template('view_hod.html',rows = rows)


@app.route('/viewdepartment')
def viewdepartmentdetails():
    rows = departmentdetails()
    print(rows)
    return render_template('view_department.html',rows = rows)



@app.route('/<id>/sdelete')
def studentdelete(id):
    print(id)
    msg = studentsingledelete(id)
    return render_template("sucesspage.html",msg = msg)

@app.route('/<department_id>/ddelete')
def departmentdelete(department_id):
    print(department_id)
    msg = departmentsingledelete(department_id)
    return render_template("sucesspage.html",msg = msg)

@app.route('/<hod_id>/hdelete')
def hoddelete(hod_id):
    print(hod_id)
    msg = hodsingledelete(hod_id)
    return render_template("sucesspage.html",msg = msg)

@app.route('/<id>/sedit')
def studentedit(id):
    print(id)
    available_options=['TamilNadu','Andra','Kerala','Mumbai']
    gender_opt=['FEMALE','MALE']
    rows = studentsingledetails(id)
    print(rows)
    selected_value=rows[0][6]
    gender_value=rows[0][7]
    msg = "hi"
    return render_template("update_student.html",rows = rows,available_options=available_options,selected_value=selected_value,gender_opt=gender_opt,gender_value=gender_value)

@app.route('/updatestudenttodb',methods=['POST','GET'])
def studentup():
    if request.method=='POST':
        i=request.form["sid"]
        sn=request.form["sname"]
        sm1=request.form["sm1"]
        sm2=request.form["sm2"]
        sm3=request.form["sm3"]
        sd=request.form["dname"]
        sl=request.form["locations"]
        sg=request.form["gender"]
        sp=request.form["sphone"]
        sdo=request.form["sdob"]
        print(sn,sm1,sm2,sm3,sd,sl,sg,sp,sdo)
        msg=studentupdate(i,sn,sm1,sm2,sm3,sd,sl,sg,sp,sdo)
        return render_template("sucesspage.html",msg=msg)


@app.route('/<id>/dedit')
def departmentedit(id):
    print(id)
    available_options=['Civil','Mech','CSE','IT']
    rows = departmentsingledetails(id)
    print(rows)
    selected_value=rows[0][1]
    msg = "hi"
    return render_template("update_department.html",rows = rows,available_options=available_options,selected_value=selected_value)


@app.route('/updatedepartmenttodb',methods=['POST','GET'])
def departmentup():
    if request.method=='POST':
        i=request.form["did"]
        dn=request.form["departments"]
        hi=request.form["hiname"]
        print(i,dn,hi)
        msg=departmentupdate(i,dn,hi)
        return render_template("sucesspage.html",msg=msg)


@app.route('/<id>/hedit')
def hodedit(id):
    print(id)
    rows = hodsingledetails(id)
    print(rows)
    msg = "hi"
    return render_template("update_hod.html",rows = rows)


@app.route('/updatehodtodb',methods=['POST','GET'])
def hodup():
    if request.method=='POST':
        i=request.form["hid"]
        hn=request.form["hname"]
        hp=request.form["hphone"]
        print(i,hn,hp)
        msg=hodupdate(i,hn,hp)
        return render_template("sucesspage.html",msg=msg)


if __name__=='__main__':
    app.run(debug = True,port=4567)