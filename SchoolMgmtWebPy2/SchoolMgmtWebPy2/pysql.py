from datetime import date
from Teacher import teacher
from Student import student
from Course import course   
from Report import report
from Test import test
import pyodbc

class pySQL:
    def __init__(self):
        self.cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver}; SERVER=BlueFish; DATABASE=schoolmgmt; UID=pytest; PWD=pytest;')
        self.cursor = self.cnxn.cursor() 

    def Disconnection(self):
        self.cursor.close()

    def StudentLogIn(self, user, pwd):
        self.cursor.execute("{CALL PQ_LOG_STUDENT(?,?)} ", user, pwd)
        rset = self.cursor.fetchone()
        if rset == None:
            print('No such user and pass\n')
            return None
        else:
            newStd = student()
            newStd.SID = int(rset[0])
            newStd.User = rset[1]
            newStd.Pass = rset[2]
            newStd.FName = rset[3]
            newStd.LName = rset[4]
            newStd.DOB = rset[5]
            newStd.Addr1 = rset[6]
            newStd.Addr2 = rset[7]
            newStd.City = rset[8]
            newStd.State = rset[9]
            newStd.Zip = rset[10]
            newStd.Email = rset[11]
            newStd.PhoneNo = rset[12]
            newStd.GPA = rset[13]
            newStd.Fixed = rset[14]

            return newStd

    def RegisterStudent(self, newStd):
        self.cursor.execute("{CALL PQ_NEW_SID}")
        newStd.SID = self.cursor.fetchone()[0]
        
        args = (newStd.SID, newStd.User, newStd.Pass, newStd.FName, newStd.LName, newStd.DOB, newStd.Addr1, newStd.Addr2, newStd.City, newStd.State, newStd.Zip, newStd.Email, newStd.PhoneNo)
        self.cursor.execute("{CALL PQ_REG_STUDENT(?,?,?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()

        return newStd

    def ModifyStudent(self, modStd):
        args = (modStd.SID, modStd.User, modStd.Pass, modStd.FName, modStd.LName, modStd.DOB, modStd.Addr1, modStd.Addr2, modStd.City, modStd.State, modStd.Zip, modStd.Email, modStd.PhoneNo)
        self.cursor.execute("{CALL PQ_MOD_STUDENT(?,?,?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()

    def GetCategories(self):
        self.cursor.execute("{CALL PQ_GET_CATEGORIES}") 
        categories = self.cursor.fetchall()
        
        return categories
    
    def GetCourses(self, category, sid):
        self.cursor.execute("{CALL PQ_GET_COURSES_IN_CAT(?,?)}", (category,sid))
        courses = self.cursor.fetchall()
        
        return courses

    def JoinCourse(self, CID, SID, time, year):
        args = (CID, SID, time, "F1", year)
        self.cursor.execute("{CALL PQ_JOIN_COURSE(?,?,?,?,?)}", args)
        self.cnxn.commit()

    def StudentCourses(self, SID):
        self.cursor.execute("{CALL PQ_VIEW_COURSES(?)}", SID)
        courses = self.cursor.fetchall()

        return courses

    def LeaveCourse(self, SID, CID):
        self.cursor.execute("{CALL PQ_LEAVE_COURSE(?,?)}", (SID, CID))
        self.cnxn.commit()
        

    def GetStudentReports(self, CID, SID):
        self.cursor.execute("{CALL PQ_FIND_REPORT_IN_CID_WITH_SID(?,?)}", (CID, SID)) 
        reportList = self.cursor.fetchall()

        return reportList

    def GetStudentReport(self, ReportID, SID):
        self.cursor.execute("{CALL PQ_FIND_REPORT_WITH_SID(?,?)}", (SID, ReportID)) 
        report = self.cursor.fetchall()[0]

        return report
                        
    def DoReport(self, ReportId, SID, answer):
        args = (ReportId, SID, answer)
        self.cursor.execute("{CALL PQ_UPDATE_REPORT_ANSWERS(?,?,?)}", args) 
        self.cnxn.commit()

    def GetStudentTests(self, CID, SID):
        self.cursor.execute("{CALL PQ_FIND_TEST_IN_CID_WITH_SID(?,?)}", (CID, SID)) 
        testList = self.cursor.fetchall()

        return testList

    def GetStudentTest(self, TestID, SID):
        self.cursor.execute("{CALL PQ_FIND_TEST_WITH_SID(?,?)}", (SID, TestID)) 
        test = self.cursor.fetchall()[0]

        return test
                        
    def DoTest(self, TestId, SID, answer):
        self.cursor.execute("{CALL PQ_UPDATE_TEST_ANSWERS(?,?,?)}", (TestId, SID, answer)) 
        self.cnxn.commit()

    def TeacherLogIn(self, user, pwd):
        self.cursor.execute("{CALL PQ_LOG_TEACHER(?,?)}", (user, pwd))
        rset = self.cursor.fetchone()
        if rset == None:
            print('No such user and pass\n')
            return None
        else:
            newTch = teacher()
            newTch.TID = rset[0]
            newTch.User = rset[1]
            newTch.Pass = rset[2]
            newTch.FName = rset[3]
            newTch.LName = rset[4]
            newTch.Email = rset[5]
            newTch.Dptmt = rset[6]
            newTch.College = rset[7]
            newTch.Subj = rset[8]
            newTch.PhoneNo = rset[9]
            newTch.Website = rset[10]

            return newTch
        
    def GetGrades(self, SID):
        self.cursor.execute("{CALL PQ_GET_GRADES(?)}", (SID)) 
        grades = self.cursor.fetchall()
        
        return grades
        
    def RegisterTeacher(self, newTch):
        self.cursor.execute("{CALL PQ_NEW_TID}")
        newTch.TID = self.cursor.fetchone()[0]
        
        args = (newTch.TID, newTch.User, newTch.Pass, newTch.FName, newTch.LName, newTch.Email, newTch.Dptmt, newTch.College, newTch.Subj, newTch.PhoneNo, newTch.Website)
        self.cursor.execute("{CALL PQ_REG_TEACHER(?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()

        return newTch

    def ModifyTeacher(self, newTch):
        args = (newTch.TID, newTch.User, newTch.Pass, newTch.FName, newTch.LName, newTch.Email, newTch.Dptmt, newTch.College, newTch.Subj, newTch.PhoneNo, newTch.Website)
        self.cursor.execute("{CALL PQ_MOD_TEACHER(?,?,?,?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()

    def AppendCourse(self, TID, newCourse):
        args = (TID, newCourse.CollegeId, newCourse.ClassName, newCourse.Textbook, newCourse.MaxSize, newCourse.RoomNo, newCourse.Category, newCourse.Time)
        self.cursor.execute("{CALL PQ_MAKE_COURSE(?,?,?,?,?,?,?,?)}", args)
        self.cnxn.commit()
        
    def GetColleges(self):
        self.cursor.execute("SELECT * FROM COLLEGES") 
        departments = self.cursor.fetchall()
        
        return departments

    def GetCollegeName(self, CollegeId):
        self.cursor.execute("{CALL PQ_GET_COLLEGENAME_WITH_ID(?)}", CollegeId) 
        name = self.cursor.fetchone()
        return name

    def TeacherCourses(self, TID):
        self.cursor.execute("{CALL PQ_TEACHER_COURSES(?)}", (TID))
        courses = self.cursor.fetchall()

        return courses

    def DropCourse(self, CID):
        self.cursor.execute("{CALL PQ_DROP_COURSE(?)}", (CID))
        self.cnxn.commit()

    def ExpandCourse(self, CID):
        self.cursor.execute("{CALL PQ_EXPAND_COURSE(?)}", (CID))
        info = self.cursor.fetchall()

        return info

    def GetSidListInCID(self, CID):
        self.cursor.execute("{CALL PQ_SID_LIST_IN_CID(?)}", CID)
        SIDlist = self.cursor.fetchall()

        return SIDlist

    def MakeReport(self, SIDlist, newReport):   
        for SID in SIDlist:
            newReport.SID = SID[0]
            args = (newReport.SID, newReport.TID, newReport.CID, newReport.Title, newReport.Task, newReport.DueDate, newReport.Year)
            self.cursor.execute("{CALL PQ_MAKE_REPORT(?,?,?,?,?,?,?)}", args)
            self.cnxn.commit()

    def MakeTest(self, SIDlist, newTest):
        for SID in SIDlist:
            newTest.SID = SID[0]
            args = (newTest.SID, newTest.TID, newTest.CID, newTest.Subj, newTest.Task, newTest.TakeDate, newTest.Year)
            self.cursor.execute("{CALL PQ_MAKE_TEST(?,?,?,?,?,?,?)}", args)
            self.cnxn.commit()
            
    def ViewCoursesTeacher(self, TID):
        self.cursor.execute("{CALL PQ_SELECT_COURSES_BY_TID(?)}", TID)
        courses = self.cursor.fetchall()

        return courses

    def ReportList(self, CID):
        self.cursor.execute("{CALL PQ_REPORT_LIST_WITH_CID(?)}", CID)
        reports = self.cursor.fetchall()

        return reports

    def TeacherReport(self, ReportTitle):
        self.cursor.execute("{CALL PQ_FIND_REPORTS_WITH_TITLE(?)}", ReportTitle)
        report = self.cursor.fetchall()

        return report
        

    def JudgeReport(self, RID, SID, CID, sgrade, prvgrade):
        grade = float(sgrade)

        self.cursor.execute("{CALL PQ_JUDGE_REPORT(?,?)}", (RID, grade))
        self.cnxn.commit()
        self.cursor.execute("{CALL PQ_UPDATE_STUDENT_GRADE(?,?,?,?)}", (SID, CID, grade, prvgrade))
        self.cnxn.commit()


    def TestList(self, CID):
        self.cursor.execute("{CALL PQ_TEST_LIST_WITH_CID(?)}", CID)
        tests = self.cursor.fetchall()

        return tests

    def TeacherTest(self, TestTitle):
        self.cursor.execute("{CALL PQ_FIND_TEST_WITH_TITLE(?)}", TestTitle)
        test = self.cursor.fetchall()

        return test
        

    def JudgeTest(self, TTID, SID, CID, sgrade, prvgrade):
        grade = float(sgrade)
        self.cursor.execute("{CALL PQ_JUDGE_TEST(?,?)}", (TTID, grade))
        self.cnxn.commit()
        self.cursor.execute("{CALL PQ_UPDATE_STUDENT_GRADE(?,?,?,?)}", (SID, CID, grade, prvgrade))
        self.cnxn.commit()