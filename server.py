#coding:utf-8
from flask import Flask,request
import pymysql,datetime


app = Flask(__name__)



@app.route('/login',methods=['POST','GET'])
def login():
	
	username = request.values.get("username")
	password = request.values.get("password")
	#print username,password
	table = username+"_info"
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
	cursor = connection.cursor()
	sql = "select *  from user"
	#sql_1 = "select password  from user_data where username = \'%s\'"%(username)
	cursor.execute(sql)
	results= cursor.fetchall()
	for result in results:
		if(username == result[0] and password == result[1]):
			return "success"

	return "failure"
		


@app.route('/register',methods=['POST','GET'])
def register():
	username = request.values.get("username")
	password = request.values.get("password")
	#print username,password
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
	cursor = connection.cursor()
	sql = "select username from user where username = \'%s\'" %(username)
	table = username + "_info"
	table_1 = username
	cursor.execute(sql)
	results= cursor.fetchall()
	length = len(results)
	flag = 0
	for result in results:
		
		if(username == result[0]):
		
			return "failure"
		else:
			flag = flag+1

	if(flag == length):

		sql_1 = "insert into user (username,password) values(\'%s\',\'%s\')" %(username,password)
		cursor.execute(sql_1)
		connection.commit()
		try:
			sql_2 = "create table %s (user varchar(200),doctor varchar(200));" %(table)
			cursor.execute(sql_2)
			connection.commit()
		except Exception as e:
			return "failure"

		try:
			sql_3 = "create table  %s (mid INT NOT NULL AUTO_INCREMENT ,Dtitle varchar(200),Dname varchar(200),Date varchar(200),num int(100),all_per int(100),everyday int(100),PRIMARY KEY(mid))ENGINE=InnoDB DEFAULT CHARSET=UTF8" %(table_1)
			cursor.execute(sql_3)
			connection.commit()
			sql_4 = "insert into %s (doctor) values('doctor1');" %(table)
                        cursor.execute(sql_4)
                        connection.commit()

			
		except Exception as e:
			return "failure"
		
		return "success"

@app.route('/add_user',methods=['POST','GET'])
def useradd():

	add = request.values.get("add")
	login_user = request.values.get("login_user")
	register_user = request.values.get("register_user")
	if(login_user != None):
		table = str(login_user)+"_info"
	if(register_user!=None):
		table = str(register_user)+"_info"
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
	cursor = connection.cursor()
	sql_1 = "select * from %s where user = \'%s\'" %(table,add)
	cursor.execute(sql_1)
	add_result= cursor.fetchall()
	add_length = len(add_result)
	add_flag = 0
	for r in add_result:
		
		if(add == r[0]):
			return "failure"
		else:
			add_flag = add_flag +1;
	if(add_flag == add_length):

		sql = "insert into   %s (user) values(\'%s\') "%(table,add)
		cursor.execute(sql)
		results= cursor.fetchall()
		connection.commit()
		length = len(results)
		return "success"

@app.route('/sub_user',methods=['POST','GET'])
def usersub():
	sub = request.values.get("sub")
	login_user = request.values.get("login_user")
        #print login_user
	register_user = request.values.get("register_user")
	if(login_user != None):
		table = str(login_user)+"_info"
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
	cursor = connection.cursor()
	sql_1 = "select * from %s where user = \'%s\'" %(table,sub)
	cursor.execute(sql_1)
	sub_result= cursor.fetchall()
	sub_length = len(sub_result)
	sub_flag = 0
	for r in sub_result:
		if(sub != r[0]):
			sub_flag = sub_flag +1;				
			
	if(sub_flag == sub_length):
		return "failure"

	else:

		sql = "delete  from %s where user = \'%s\'" %(table,sub)
		cursor.execute(sql)
		connection.commit()
		return "success"


@app.route('/member',methods=['POST','GET'])
def member():
	table = ''
	login_user = request.values.get("login_user")
	register_user = request.values.get("register_user")
	if(login_user != None):
		table = str(login_user)+"_info"
	#print table
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
	cursor = connection.cursor()
	sql = "select user from %s" %(table)
	cursor.execute(sql)
	results = cursor.fetchall()
	length = len(results)
	member_result = ''
	if(length != 0):

		for  r in results:
			if(r[0] != None):
				

				member_result = member_result+ str(r[0]) + ","
	else:
		member_result = ' , '
	
	return member_result

@app.route('/doctor',methods=['POST','GET'])
def doctor():
	table =''
	login_user = request.values.get("login_user")
	if(login_user != None):
		table = str(login_user)+"_info"
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
	cursor = connection.cursor()
	sql = "select doctor from %s" %(table)
	cursor.execute(sql)
	results = cursor.fetchall()
	length = len(results)
	doctor_result = ''
	if(length != 0):

		for  r in results:
			if(r[0] != None):
				doctor_result = doctor_result+str(r[0]) + ","
	else:
		doctor_result = " , "
	return doctor_result

@app.route('/banzi',methods=['POST','GET'])
def receive():
        c=0
	info = request.values.get("string")
        medicine_title = info.split(' ')[0]
	medicine_name = info.split(' ')[1]
	medicine_save_mode = info.split(' ')[2]
	medicine_overdue = info.split(' ')[3]
	medicine_amount = info.split(' ')[4]
	medicine_inorout = info.split(' ')[5]
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
	cursor = connection.cursor()
        sql="select * from drug"
        cursor.execute(sql)
        results = cursor.fetchall()
        length = len(results)
        amount=int(medicine_amount)
	for result in results:
	    if(result[1] == medicine_title):
		    sql_1= "update drug set Dnum=Dnum+%s where Dtitle = %s " % (amount,medicine_title)
		    cursor.execute(sql_1)
                    connection.commit()
	    else:
                    c=c+1
        if(c == length):	
            sql_1 = "insert into drug (Dtitle,Dname,Dstate,Ddate,Dnum,Dinout) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" %(medicine_title,medicine_name,medicine_save_mode,medicine_overdue,medicine_amount,medicine_inorout) 
            cursor.execute(sql_1)
	connection.commit()
	return "success" 
@app.route('/person',methods=['POST','GET'])
def myperson():
        b=0
        info = request.values.get("string")
        medicine_title = info.split(' ')[0]
        medicine_name = info.split(' ')[1]
        medicine_overdue = info.split(' ')[3]
        medicine_amount = info.split(' ')[4]
	medicine_own = info.split(' ')[6]
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
        cursor = connection.cursor()
        try:
            sql="select * from %s" % (medicine_own)
            cursor.execute(sql)
           # print "s" 
        except Exception:
            #print "a" 
            return "failed"
        else:
            results = cursor.fetchall()
            length = len(results)
            amount=int(medicine_amount)
           # print "q"  
            for result in results:
                if(result[1] == medicine_title):
                   # print "z"
                    sql_1= "update %s set num=num+%s where Dtitle = %s " % (medicine_own,amount,medicine_title)
                    cursor.execute(sql_1)
                    connection.commit()
                else:
                    b=b+1
            if(b == length):
                #print medicine_own
                sql_1 = "insert into %s (Dtitle,Dname,Date, num) values('%s','%s','%s','%s')" %(medicine_own,medicine_title,medicine_name,medicine_overdue,medicine_amount)
                #print "OK"
                cursor.execute(sql_1)
                connection.commit()
	    return "success"
@app.route('/handsome',methods=['POST','GET'])
def chuku(): 
        info = request.values.get("string")
        medicine_title = info.split(' ')[0]
        medicine_name = info.split(' ')[1]
        medicine_save_mode = info.split(' ')[2]
        medicine_overdue = info.split(' ')[3]
        medicine_amount = info.split(' ')[4]
        medicine_inorout = info.split(' ')[5]
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
        cursor = connection.cursor()
        sql="select * from drug"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            if(result[1] == medicine_title):
                    sql_1= "update drug set Dnum=Dnum-1 where Dtitle = %s " % (medicine_title)
                    cursor.execute(sql_1)
                    connection.commit()
                    if(result[5]==0):
                        sql_2="update drug set Dnum=0 where Dtitle = %s" %(medicine_title)
                        cursor.execute(sql_2)
                        connection.commit()  
        return "success"
@app.route('/cute',methods=['POST','GET'])
def cute():
        info = request.values.get("string")
        medicine_title = info.split(' ')[0]
        medicine_name = info.split(' ')[1]
        medicine_save_mode = info.split(' ')[2]
        medicine_overdue = info.split(' ')[3]
        medicine_amount = info.split(' ')[4]
        medicine_inorout = info.split(' ')[5]
        medicine_own = info.split(' ')[6]
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
        cursor = connection.cursor()
        try:
            sql="select * from %s" % (medicine_own)
            cursor.execute(sql)
        except Exception:
            return "failed"
        else:
            #print medicine_own
            results = cursor.fetchall()
            for result in results:
               # print medicine_title
               # print result[1]
                if(result[1] == medicine_title):
                    sql_2="select all_per from %s where Dtitle= %s" % (medicine_own, medicine_title)
                    cursor.execute(sql_2)
                    data=cursor.fetchone()
                   # print "d"
                    #print data[0]
                    if(data[0]>0):
                        sql_3="update %s set all_per=all_per-1 where Dtitle = %s"%(medicine_own,medicine_title)
                        cursor.execute(sql_3)
                        connection.commit()
                        sql_1= "update %s set num=num-1 where Dtitle = %s " % (medicine_own,medicine_title)
                        cursor.execute(sql_1)
                        connection.commit()            
                    return "success"
                else:
                    print "b"

@app.route('/time_medicine',methods=['POST','GET'])
def time_md():
	name = request.values.get("name")
	print name
	sql_1= "select Dname from %s where everyday = 3 and all_per > 0" %(name)
	sql_2 = "select Dname from %s where everyday = 2 and all_per > 0" %(name)
	sql_3 = "select Dname from %s where everyday = 1 and all_per > 0" %(name)
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
	cursor = connection.cursor()
	cursor.execute(sql_1)
	result1 = cursor.fetchall()
	three_length = len(result1)
	three = ''
	t1= 0
	if(three_length != 0):

		for r1 in result1:
			t1 = t1 +1
			if(t1 == three_length):
				three = three+r1[0]
			else:
				three = three+r1[0]+","
	else:
		three = ' ,'

	cursor.execute(sql_2)
	result2 = cursor.fetchall()
	two_length = len(result2)
	two = ''
	t2= 0
	if(two_length !=0):

		for r2 in result2:
			t2 = t2 +1
			if(t2 == two_length):
				two = two+r2[0]
			else:
				two = two+r2[0]+","
	else:
		two = ' ,'

	cursor.execute(sql_3)
	result3 = cursor.fetchall()
	one_length = len(result3)
	one = ''
	t3 = 0
	if(one_length != 0):

		for r3 in result3:
			t3 = t3 +1
			if(t3 == one_length):
				one = one+r3[0]
			else:
				one = one+r3[0]+","
	else:
		one = ' , '

#	d = one+","+two+","+three+";"+three+";"+three+","+two
	d1=d2=d3=''
	if(one == ' , ' and two == ' , ' and three == ' , '):
		d = " , ; , ; , "

	elif(one == ' , ' and two == ' , ' and three != ' , '):
		d = three +";"+three+";"+three
	elif(one == ' , ' and two != ' , ' and three == ' , '):
		d = two+";"+three+";"+two
	elif(one == ' , ' and two != ' , ' and three != ' , '):
		d = three+","+two+";"+three+";"+three+","+two
	elif(one != ' , ' and two == ' , ' and three == ' , '):
		d = one+";"+three+";"+three
	elif(one != ' , ' and two == ' , ' and three != ' , '):
		d = one+","+three+";"+three+";"+three
	elif(one != ' , ' and two != ' , ' and three == ' , '):
		d = one+","+two+";"+three+";"+two
	elif(one != ' , ' and two != ' , ' and three != ' , '):
		d = three+","+two+","+one+";"+three+";"+three+","+two	
	
	
	return d

@app.route('/overdate',methods = ['POST','GET'])
def overdue():
	name = request.values.get("name")
	if(name != ""):

		current = datetime.datetime.today()
		sql_1 = "select * from %s" %(name)
		connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
		cursor = connection.cursor()
		cursor.execute(sql_1)
		result = cursor.fetchall()
		medicine = ""
		for t in result:
			strftime = datetime.datetime.strptime(str(t[3]), "%Y-%m-%d")
			#print strftime
			if(current>strftime):
				medicine = medicine+str(t[2])+","

		if(medicine == "" ):
			medicine = "noover"	
		return medicine	
@app.route('/lack_medicine',methods = ['POST','GET'])
def lack():
        name = request.values.get("name")
	if(name != ""):

	        sql_1 = "select * from %s" %(name)
       		connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project')
       		cursor = connection.cursor()
       		cursor.execute(sql_1)
       		result = cursor.fetchall()
       		medicine = ""
       		for t in result:
                	if(t[4]==0):
                        	medicine = medicine+str(t[2])+","
	
		if(medicine == ""):
			medicine = "nolack"
        	return medicine

@app.route('/allInventory',methods=['POST','GET'])
def allInventory():
	connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
	cursor = connection.cursor()
	sql = "select * from drug "
	
	cursor.execute(sql)
	results= cursor.fetchall()
	strAll = ''
	for result in results:
		strAll = strAll +"  "+ str(result[2]) +"  "+ str(result[3]) +"  "+ str(result[4]) +"  "+ str(result[5]) + ","
        return strAll


@app.route('/myInventory',methods=['POST','GET'])
def myInventory():
	
    name = request.values.get("name")
    print "d"
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
    cursor = connection.cursor()
	#sql = "select * from %s "%(name)
    sql = "select * from %s " %(name)	
    cursor.execute(sql)
    results= cursor.fetchall()
    strMy = ''
    for result in results:
	if((result[5] != None)):
	
        	strMy = strMy +str(result[1])+" "+ str(result[2]) + " " + str(result[4])  + " " + str(result[3]) + " " + str(result[5]) + ","
	else:
		strMy = strMy +str(result[1])+" "+ str(result[2]) + " " + str(result[4])  + " " + str(result[3]) + " " + "0" + ","
    return strMy

@app.route('/medicine_settings',methods=['POST','GET'])
def medicine_settings():

    table_name = request.values.get("name")
    medicine_set = request.values.get("medicine_set")
    #print medicine_set 
    value = []
    value = medicine_set.split("  ")
    #print value[0]
    #print value[1]
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='project') 
    cursor = connection.cursor()
	
    #sql = "update %s set Uday='%s' where Dname='%s' "%(name, value[1], value[0])
	#cursor.execute(sq)
    sql_4 = "select * from %s"%(table_name) 
    cursor.execute(sql_4)
    num_result = cursor.fetchall()
    n = 0
    for r in num_result:
	n = r[4]
	if(n > int(value[1],10)):
		
	
    		sql1 = "update %s set all_per=%d where Dtitle=%d "%(table_name,int(value[1],10), int(value[0],10)) 
   		cursor.execute(sql1)
    		connection.commit()
   		sql2 = "update %s set everyday=%d where Dtitle=%d "%(table_name,int(value[2],10), int(value[0],10))
    		cursor.execute(sql2)
    		connection.commit()

		return "success"
	else:
		return "failure"



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=23333)


