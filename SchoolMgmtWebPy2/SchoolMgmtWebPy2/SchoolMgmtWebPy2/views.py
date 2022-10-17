"""
Routes and views for the flask application.
"""

from datetime import date
from flask import request, render_template, redirect, session, flash
from SchoolMgmtWebPy2 import app
from Student import student
from Teacher import teacher
from Course import course
from Test import test
from Report import report
from pysql import pySQL

curStudent = student()
curTeacher = teacher()
sql = pySQL()

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    session.pop('curLog', None)

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        logtype = request.form.getlist('logtype')[0]

        if logtype == 'Student':
            global curStudent
            result = sql.StudentLogIn(username, password)
            if result == None:
                flash('No such username and password', category='error')
                return render_template("login.html")
            else:
                flash('Successful Login!', category = 'success')
                curStudent = result
                session['curLog'] = 'student'
                return redirect("home")

        elif logtype == 'Teacher':
            global curTeacher
            result = sql.TeacherLogIn(username, password)
            if result == None:
                flash('No such username and password', category='error')
                return render_template("login.html")
            else:
                flash('Successful Login!', category = 'success')
                curTeacher = result
                session['curLog'] = 'teacher'
                return redirect("home")
        elif username.upper() == 'ADMIN':
            session['curLog'] = 'admin'
            return redirect("home")

    return render_template(
        'login.html',
        title = "Login Page"
    )

@app.route('/register', methods = ['GET', 'POST'])
def register():
    print('got this far')
    session.pop('curLog', None)

    if request.method == "POST":
        register = request.form.get('register')

        if register == 'Student':
            print('got this far')
            global curStudent
            curStudent.User = request.form.get('username')
            if len(curStudent.User) == 0:
                flash('Username cannot be empty', category='error')
                return render_template("register.html")

            curStudent.Pass = request.form.get('password')
            if len(curStudent.Pass) == 0:
                flash('Password cannot be empty', category='error')
                return render_template("register.html")

            curStudent.FName = request.form.get('firstname')
            if len(curStudent.FName) == 0:
                flash('First name cannot be empty', category='error')
                return render_template("register.html")

            curStudent.LName = request.form.get('lastname')
            if len(curStudent.LName) == 0:
                flash('Last name cannot be empty', category='error')
                return render_template("register.html")

            curStudent.DOB = request.form['dob']

            curStudent.Addr1 = request.form.get('addr1')
            if len(curStudent.Addr1) == 0:
                flash('Address 1 cannot be empty', category='error')
                return render_template("register.html")

            curStudent.Addr2 = request.form.get('addr2')

            curStudent.City = request.form.get('city')
            if len(curStudent.City) == 0:
                flash('City cannot be empty', category='error')
                return render_template("register.html")


            curStudent.Zip = request.form.get('zip')
            if len(curStudent.Zip) == 0:
                flash('Zip cannot be empty', category='error')
                return render_template("register.html")

            curStudent.Email = request.form.get('email')
            if len(curStudent.Email) == 0:
                flash('Email cannot be empty', category='error')
                return render_template("register.html")

            curStudent.PhoneNo = request.form.get('phoneno')
            if len(curStudent.PhoneNo) == 0:
                flash('Phone number cannot be empty', category='error')
                return render_template("register.html")
            
            print('got this far')

            flash('Account Created!', category='success')
            sql.RegisterStudent(curStudent)
            session['curLog'] = 'student'
            return redirect('home')

        elif register == 'Teacher':
            global curTeacher
            curTeacher.User = request.form.get('username')
            if len(curTeacher.User) == 0:
                flash('Username cannot be empty', category='error')
                return render_template("register.html")

            curTeacher.Pass = request.form.get('password')
            if len(curTeacher.Pass) == 0:
                flash('Password cannot be empty', category='error')
                return render_template("register.html")

            curTeacher.FName = request.form.get('firstname')
            if len(curTeacher.FName) == 0:
                flash('First name cannot be empty', category='error')
                return render_template("register.html")

            curTeacher.LName = request.form.get('lastname')
            if len(curTeacher.LName) == 0:
                flash('Last name cannot be empty', category='error')
                return render_template("register.html")
            
            curTeacher.Email = request.form.get('email')
            if len(curTeacher.Email) == 0:
                flash('Email cannot be empty', category='error')
                return render_template("register.html")
            
            curTeacher.Dptmt = request.form.get('department')
            if len(curTeacher.Dptmt) == 0:
                flash('Department cannot be empty', category='error')
                return render_template("register.html")
            
            curTeacher.College = request.form.get('college')
            if len(curTeacher.College) == 0:
                flash('College cannot be empty', category='error')
                return render_template("register.html")
            
            curTeacher.Subj = request.form.get('subject')
            if len(curTeacher.Subj) == 0:
                flash('Subject cannot be empty', category='error')
                return render_template("register.html")

            curTeacher.PhoneNo = request.form.get('phoneno')
            if len(curTeacher.PhoneNo) == 0:
                flash('Phone number cannot be empty', category='error')
                return render_template("register.html")

            curTeacher.Website = request.form.get('website')
            if len(curTeacher.Website) == 0:
                flash('Website cannot be empty', category='error')
                return render_template("register.html")
            
            flash('Account Created!', category='success')
            sql.RegisterTeacher(curTeacher)
            session['curLog'] = 'teacher'
            return redirect('home')

    return render_template(
        'register.html',
        title = "Register Page"
    )

@app.route('/studentView')
def studentView():
    return render_template(
        'studentView.html',
        title='Student View',
        student = curStudent
    )

@app.route('/studentModify', methods=['GET', 'POST'])
def studentModify():
    global curStudent
    if request.method == 'POST':
        username = request.form.get('username')
        if len(username) != 0:
            curStudent.User = username 

        password = request.form.get('password')
        if len(password) != 0:
            curStudent.Pass = password 

        firstname = request.form.get('firstname')
        if len(firstname) != 0:
            curStudent.FName = firstname 

        lastname = request.form.get('lastname')
        if len(lastname) != 0:
            curStudent.LName = lastname 

        dob = request.form.get('dob')
        if len(dob) != 0:
            curStudent.DOB = dob 

        addr1 = request.form.get('addr1')
        if len(addr1) != 0:
            curStudent.Addr1 = addr1

        curStudent.Addr2 = request.form.get('addr2')
            
        city = request.form.get('city')
        if len(city) != 0:
            curStudent.City = city
                
        state = request.form.get('state')
        if len(state) != 0:
            curStudent.State = state
                
        email = request.form.get('email')
        if len(email) != 0:
            curStudent.Email = email
                
        phoneno = request.form.get('phoneno')
        if len(phoneno) != 0:
            curStudent.PhoneNo = phoneno
            
        flash('Account Modified!', category='success')
        sql.ModifyStudent(curStudent)
        return redirect('studentView')

    return render_template(
        'studentmodify.html',
        title='Student Modify',
        student = curStudent
    )

@app.route('/studentDelete', methods=['GET', 'POST'])
def studentDelete():
    global curStudent
    if request.method == 'POST':
        if request.form['submit_button'] == 'DELETE':
            sql.DeleteStudent(curStudent.SID)
            flash("Deleted Teacher Account!", category='success')
            return redirect('logout')
        if request.form['submit_button'] == 'CANCEL':
            flash("Canceled Deletion", category='success')
            return redirect('home')

    return render_template(
        'studentdelete.html',
        title='Student Delete'
    )

@app.route('/exploreCategories', methods=['GET', 'POST'])
def exploreCategories():
    global curStudent
    if request.method == 'POST':
        session['category'] = request.form.get("submit_category")
        return redirect('exploreCourses')
    
    return render_template(
        'exploreCategories.html',
        title='Explore Categories',
        categories = sql.GetCategories()
    )

@app.route('/exploreCourses', methods=['GET', 'POST'])
def exploreCourses():
    global curStudent
    if request.method == 'POST':
        CID = request.form.get('cid')
        Time = request.form.get('time')

        sql.JoinCourse(CID, curStudent.SID, Time, date.today().year)
        flash("Successfully joined " + request.form.get('classname'), category= "success")
        session.pop('category', None)
        return redirect('home')

    return render_template(
        'exploreCourses.html',
        title='Explore Courses',
        courses = sql.GetCourses(session['category'], curStudent.SID),
        category = session['category']
    )

@app.route('/studentCourses', methods=['GET', 'POST'])
def studentCourses():
    global curStudent
    if request.method == 'POST':
        if request.form['submit_button'] == 'DEL':
            sql.LeaveCourse(curStudent.SID, request.form.get('cid'))
            flash("Successfully left " + request.form.get('classname'), category= "success")
            
        if request.form['submit_button'] == 'REPORT':
            session['cid'] = request.form.get('cid')
            session['classname'] = request.form.get('classname')
            return redirect('sReportList')

        if request.form['submit_button'] == 'TEST':
            session['cid'] = request.form.get('cid')
            session['classname'] = request.form.get('classname')
            return redirect('sTestList')

    courses = sql.StudentCourses(curStudent.SID)
    return render_template(
        'studentCourses.html',
        title='Student Courses',
        courses = courses
    )

@app.route('/sReportList', methods=['GET', 'POST'])
def sReportList():
    global curStudent
    if request.method == 'POST':
        reportid = request.form.get('reportid')
        session['reportid'] = reportid
        return redirect('studentReport')

    reports = sql.GetStudentReports(session['cid'], curStudent.SID)
    return render_template(
        's_reportlist.html',
        title='Report List',
        classname = session['classname'],
        reports = reports
    )

@app.route('/sTestList', methods=['GET', 'POST'])
def sTestList():
    global curStudent
    if request.method == 'POST':
        testid = request.form.get('testid')
        session['testid'] = testid
        return redirect('studentTest')

    tests = sql.GetStudentTests(session['cid'], curStudent.SID)
    return render_template(
        's_testlist.html',
        title='Test List',
        classname = session['classname'],
        tests = tests
    )

@app.route('/studentReport', methods=['GET', 'POST'])
def studentReport():
    global curStudent
    if request.method == 'POST':
        sql.DoReport(session['reportid'], curStudent.SID, request.form.get('answer'))
        session.pop('reportid', None)
        session.pop('cid', None)
        session.pop('classname', None)
        flash('Successfully submitted report!', category = 'success')
        return redirect('home')

    report = sql.GetStudentReport(session['reportid'], curStudent.SID)

    return render_template(
        'studentReport.html',
        title='Student Report',
        classname = session['classname'],
        report = report
    )

@app.route('/studentTest', methods=['GET', 'POST'])
def studentTest():
    global curStudent
    if request.method == 'POST':
        sql.DoTest(session['testid'], curStudent.SID, request.form.get('answer'))
        session.pop('testid', None)
        session.pop('cid', None)
        session.pop('classname', None)
        flash('Successfully submitted test!', category = 'success')
        return redirect('home')

    test = sql.GetStudentTest(session['testid'], curStudent.SID)

    return render_template(
        'studentTest.html',
        title='Student Test',
        classname = session['classname'],
        test = test
    )

@app.route('/viewGrades', methods=['GET', 'POST'])
def viewGrades():
    global curStudent
    grades = sql.GetGrades(curStudent.SID)
    
    GPA = 0.0
    if len(grades) > 0:
        for grade in grades:
            GPA += float(grade[1])

        GPA = GPA/(len(grades)*25)

    return render_template(
        's_viewGrades.html',
        title='Student Grades',
        student = curStudent,
        grades = grades,
        GPA = "{:.2f}".format(GPA)
    )







@app.route('/teacherView')
def teacherView():
    return render_template(
        'teacherView.html',
        title='Teacher View',
        teacher = curTeacher
    )

@app.route('/teacherModify', methods=['GET', 'POST'])
def teacherModify():
    global curTeacher
    if request.method == 'POST':
        username = request.form.get('username')
        if len(username) != 0:
            curStudent.User = username 

        password = request.form.get('password')
        if len(password) != 0:
            curStudent.Pass = password 

        firstname = request.form.get('firstname')
        if len(firstname) != 0:
            curStudent.FName = firstname 

        lastname = request.form.get('lastname')
        if len(lastname) != 0:
            curStudent.LName = lastname 

        dob = request.form.get('dob')
        if len(dob) != 0:
            curStudent.DOB = dob 

        addr1 = request.form.get('addr1')
        if len(addr1) != 0:
            curStudent.Addr1 = addr1

        curStudent.Addr2 = request.form.get('addr2')
            
        city = request.form.get('city')
        if len(city) != 0:
            curStudent.City = city
                
        state = request.form.get('state')
        if len(state) != 0:
            curStudent.State = state
                
        email = request.form.get('email')
        if len(email) != 0:
            curStudent.Email = email
                
        phoneno = request.form.get('phoneno')
        if len(phoneno) != 0:
            curStudent.PhoneNo = phoneno
            
        flash('Account Modified!', category='success')
        sql.ModifyTeacher(curTeacher)
        return redirect('teacherView')
    return render_template(
        'teacherModify.html',
        title='Teacher Modify',
        teacher = curTeacher
    )

@app.route('/teacherDelete', methods=['GET', 'POST'])
def teacherDelete():
    global curTeacher
    if request.method == 'POST':
        if request.form['submit_button'] == 'DELETE':
            sql.DeleteTeacher(curTeacher.TID)
            flash("Deleted Teacher Account!", category='success')
            return redirect('logout')
        if request.form['submit_button'] == 'CANCEL':
            flash("Canceled Deletion", category='success')
            return redirect('home')

    return render_template(
        'teacherdelete.html',
        title='Teacher Delete'
    )

@app.route('/makeCourse', methods=['GET', 'POST'])
def makeCourse():
    global curTeacher
    if request.method == 'POST':
        newCourse = course()
        newCourse.ClassName = request.form.get('classname')
        newCourse.CollegeId = int(request.form.get('department'))
        newCourse.Textbook = request.form.get('textbook')
        newCourse.MaxSize = int(request.form.get('maxsize'))
        newCourse.RoomNo = int(request.form.get('roomno'))
        newCourse.Category = request.form.get('category').upper()
        newCourse.Department = sql.GetCollegeName(newCourse.CollegeId)
        newCourse.Time = str(request.form.get('time'))
        
        sql.AppendCourse(curTeacher.TID, newCourse)
        flash('Successfully Made Course!', category = 'success')
        return redirect('home')
            
    return render_template(
        't_makecourse.html',
        title='Make Course',
        departments = sql.GetColleges()
    )

@app.route('/teacherCourses', methods=['GET', 'POST'])
def teacherCourses():
    global curTeacher
    if request.method == 'POST':
        if request.form['submit_button'] == 'EXPAND':
            session['cid'] = request.form.get('cid')
            session['classname'] = request.form.get('classname')
            return redirect('expandCourse')

        if request.form['submit_button'] == 'WORK':
            session['cid'] = request.form.get('cid')
            return redirect('teacherAssign')

        if request.form['submit_button'] == 'DEL':
            sql.DropCourse(request.form.get('cid'))
            flash("Successfully dropped " + request.form.get('classname'), category= "success")
            
    courses = sql.TeacherCourses(curTeacher.TID)
    return render_template(
        'teacherCourses.html',
        title='Teacher Courses',
        courses = courses
    )

@app.route('/expandCourse')
def expandCourse():
    info = sql.ExpandCourse(session['cid'])
    classname = session['classname']
    session.pop('cid', None)
    session.pop('classname', None)

    return render_template(
        't_CourseInfo.html',
        title='Course Info',
        students = info,
        classname = classname
    )

@app.route('/teacherAssign', methods=['GET', 'POST'])
def teacherAssign():
    global curTeacher
    if request.method == 'POST':
        CID = request.form.get('cid')
        sidlist = sql.GetSidListInCID(CID)
        if request.form['submit_button'] == 'REPORT':
            newReport = report()
            newReport.TID = curTeacher.TID
            newReport.CID = CID
            newReport.Title = request.form.get('title')
            newReport.Task = request.form.get('task')
            newReport.DueDate = request.form.get('duedate')
            newReport.Year = int(date.today().year)
            
            sql.MakeReport(sidlist, newReport)
            flash("Successfully made new report!", category="success")
        
        elif request.form['submit_button'] == 'TEST':
            newTest = test()
            newTest.TID = curTeacher.TID
            newTest.CID = CID
            newTest.Subj = request.form.get('subject')
            newTest.Task = request.form.get('task')
            newTest.TakeDate = request.form.get('takedate')
            newTest.Year = int(date.today().year)
            
            sql.MakeTest(sidlist, newTest)
            flash("Successfully made new test!", category="success")

        session.pop('cid', None)
        return redirect('home')

    return render_template(
        'teacherAssign.html',
        title='Assign',
        cid = session['cid']
    )

@app.route('/judgeCourses', methods=['GET', 'POST'])
def judgeCourses():
    global curTeacher
    print('1111111111111111111111111111111111111111')
    if request.method == 'POST':
        session['cid'] = request.form.get('cid')
        session['classname'] = request.form.get('classname')

        if request.form['submit_button'] == 'REPORT':
            return redirect('tReportList')

        if request.form['submit_button'] == 'TEST':
            return redirect('tTestList')
        

    return render_template(
        't_judgeCourses.html',
        title='Judge Courses',
        courses = sql.ViewCoursesTeacher(curTeacher.TID)
    )

@app.route('/tReportList', methods=['GET', 'POST'])
def tReportList():
    global curTeacher
    if request.method == 'POST':
        session['reporttitle'] = request.form['reporttitle']
        return redirect('judgeReport')
    
    return render_template(
        't_courseReports.html',
        title='Report List',
        classname = session['classname'],
        reports = sql.ReportList(session['cid'])
    )

@app.route('/judgeReport', methods=['GET', 'POST'])
def judgeReport():
    global curTeacher
    if request.method == 'POST':
        RID = int(request.form.get('reportid'))
        SID = int(request.form.get('sid'))
        CID = session['cid']
        grade = int(request.form.get('grade'))
        prvgrade = int(request.form.get('prvgrade'))

        sql.JudgeReport(RID, SID, CID, grade, prvgrade)
    
    reports = sql.TeacherReport(session['reporttitle'])
    return render_template(
        't_judgeReport.html',
        title='Judge Report',
        rtitle = session['reporttitle'],
        reports = reports)


@app.route('/tTestList', methods=['GET', 'POST'])
def tTestList():
    global curTeacher
    if request.method == 'POST':
        session['testtitle'] = request.form['testtitle']
        return redirect('judgeTest')

    return render_template(
        't_courseTests.html',
        title='Test List',
        classname = session['classname'],
        tests = sql.TestList(session['cid'])
    )

@app.route('/judgeTest', methods=['GET', 'POST'])
def judgeTest():
    global curTeacher
    if request.method == 'POST':
        TTID = int(request.form.get('testid'))
        SID = int(request.form.get('sid'))
        CID = session['cid']
        grade = int(request.form.get('grade'))
        prvgrade = int(request.form.get('prvgrade'))

        sql.JudgeTest(TTID, SID, CID, grade, prvgrade)
    
    tests = sql.TeacherTest(session['testtitle'])
    for test in tests:
        print(test)

     
    return render_template(
        't_judgeTest.html',
        title='Judge Test',
        ttitle = session['testtitle'],
        tests = tests)





@app.route('/home')
def home():
    return render_template(
        'home.html',
        title='Home Page'
    )

@app.route('/logout')
def logout():
    session.pop('curLog', None)
    global curStudent
    global curTeacher
    curStudent = student()
    curTeacher = teacher()

    flash('You have successfully logged out!', category = 'success')
    return redirect('login')
    