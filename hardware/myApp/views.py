from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

# select * from tables
def main(request):
    view = 0
    productList = []; pcList = []; laptopList = []; printerList = [];
    with connection.cursor() as cursor:
        productSel = "SELECT * FROM product"
        cursor.execute(productSel)
        fetchResultProduct = cursor.fetchall()

        pcSel = "SELECT * FROM pc"
        cursor.execute(pcSel)
        fetchResultPc = cursor.fetchall()

        laptopSel = "SELECT * FROM laptop"
        cursor.execute(laptopSel)
        fetchResultLaptop = cursor.fetchall()

        printerSel = "SELECT * FROM printer"
        cursor.execute(printerSel)
        fetchResultPrinter = cursor.fetchall()

        connection.commit()
        connection.close()

        for tmp in fetchResultProduct:
            eachRow = {'maker': tmp[0], 'model': tmp[1], 'type': tmp[2]}
            productList.append(eachRow)

        for temp in fetchResultPc:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4], 'maker': temp[5]}
            pcList.append(eachRow)

        for temp in fetchResultLaptop:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4], 'price': temp[5], 'maker': temp[6]}
            laptopList.append(eachRow)

        for temp in fetchResultPrinter:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3], 'maker': temp[4]}
            printerList.append(eachRow)

    return render(request, 'myApp/main.html',\
    {"view": view, "productList": productList, "pcList": pcList, "laptopList": laptopList, "printerList": printerList})

# create table
def create(request):
    with connection.cursor() as cursor:
        createProduct = "CREATE TABLE product (\
                        maker VARCHAR(10),\
                        model INT PRIMARY KEY,\
                        type VARCHAR(20));"
        createPc = "CREATE TABLE PC (\
                    model INT PRIMARY KEY,\
                    speed NUMERIC(3,2),\
                    ram INT,\
                    hd INT,\
                    price INT);"
        createLaptop = "CREATE TABLE Laptop (\
                        model INT PRIMARY KEY,\
                        speed DECIMAL(3,2),\
                        ram INT,\
                        hd INT,\
                        screen DECIMAL(3,1),\
                        price INT);"
        createPrinter = "CREATE TABLE Printer (\
                        model INT PRIMARY KEY,\
                        color BOOLEAN,\
                        type VARCHAR(20),\
                        price INT);"
        
        cursor.execute(createProduct)
        cursor.execute(createPc)
        cursor.execute(createLaptop)
        cursor.execute(createPrinter)
        connection.commit()
        connection.close()

    return HttpResponseRedirect(reverse('main'))

# insert data
def insert(request):
    with connection.cursor() as cursor:
        insertProduct = "INSERT INTO product VALUES\
                        ('A',1001,'pc'),('A',1002,'pc'),('A',1003,'pc'),\
                        ('A',2004,'laptop'),('A',2005,'laptop'),('A',2006,'laptop'),\
                        ('B',1004,'pc'),('B',1005,'pc'),('B',1006,'pc'),('B',2007,'laptop'),\
                        ('D',1007,'pc'),('D',1008,'pc'),('D',1009,'pc'),('D',1010,'pc'),\
                        ('D',3004,'printer'),('D',3005,'printer'),\
                        ('E',2001,'laptop'),('E',2002,'laptop'),('E',2003,'laptop'),\
                        ('E',3001,'printer'),('E',3002,'printer'),('E',3003,'printer'),\
                        ('F',2008,'laptop'),('F',2009,'laptop'),\
                        ('G',2010,'laptop'),\
                        ('H',3006,'printer'),('H',3007,'printer');"

        insertPc = "INSERT INTO pc VALUES\
                    (1001,2.66,1024,250,2114),(1002,2.10,512,250,995),\
                    (1003,1.42,512,80,478),(1004,2.80,1024,250,649),\
                    (1005,3.20,512,250,630),(1006,3.20,1024,320,1049),\
                    (1007,2.20,1024,200,510),(1008,2.20,2048,250,770),\
                    (1009,2.00,1024,250,650),(1010,2.80,2048,300,770),\
                    (1011,1.86,2048,160,959),(1012,2.80,1024,160,649),\
                    (1013,3.06,512,80,529);"

        insertLaptop = "INSERT INTO laptop VALUES\
                        (2001,2.00,2048,240,20.1,3673),(2002,1.73,1024,80,17.0,949),\
                        (2003,1.80,512,60,15.4,549),(2004,2.00,512,60,13.3,1150),\
                        (2005,2.16,1024,120,17.0,2500),(2006,2.00,2048,80,15.4,1700),\
                        (2007,1.83,1024,120,13.3,1429),(2008,1.60,1024,120,15.4,900),\
                        (2009,1.60,512,80,14.1,680),(2010,2.00,2048,160,15.4,2300);"

        insertPrinter = "INSERT INTO printer VALUES\
                        (3001,true,'ink-jet',99),(3002,false,'laser',239),\
                        (3003,true,'laser',899),(3004,true,'ink-jet',120),\
                        (3005,false,'laser',120),(3006,true,'ink-jet',100),\
                        (3007,true,'laser',200);"

        cursor.execute(insertProduct)
        cursor.execute(insertPc)
        cursor.execute(insertLaptop)
        cursor.execute(insertPrinter)
        connection.commit()
        connection.close()

    return HttpResponseRedirect(reverse('main'))

def query1(request):
    outputOfQuery = [];
    with connection.cursor() as cursor:
        sqlQuery1 = "SELECT AVG(hd) FROM pc"
        cursor.execute(sqlQuery1)
        fetchResultQuery = cursor.fetchall()
    
    return render(request, 'myApp/query1.html', {"out": fetchResultQuery})

def query2(request):
    outputOfQuery = [];
    with connection.cursor() as cursor:
        sqlQuery2 = "SELECT maker, COUNT(laptop.model), AVG(speed)\
                FROM laptop, product\
                WHERE laptop.model = product.model\
                GROUP BY maker ORDER BY maker ASC"
                # Select p.maker, AVG(l.speed)
                # from product p
                # join laptop l
                # on p.model = l.model
                # group by p.maker
        cursor.execute(sqlQuery2)
        fetchResultQuery = cursor.fetchall()
        #print(len(fetchResultQuery))

    for temp in fetchResultQuery:
        eachRow = {'maker': temp[0], 'num': temp[1], 'avg': temp[2]}
        outputOfQuery.append(eachRow)
    
    return render(request, 'myApp/query3.html', {"out": outputOfQuery})

def query3(request):
    outputOfQuery = [];
    with connection.cursor() as cursor:
        sqlQuery3 = "SELECT l2.model, l2.price\
                    FROM laptop l2\
                    WHERE l2.model IN (\
                        SELECT p3.model\
                        FROM product p3\
                        WHERE p3.maker IN (\
                            SELECT p1.maker\
                            FROM product p1\
                            WHERE p1.type = 'laptop'\
                            GROUP BY p1.maker\
                            HAVING COUNT(p1.model) = 1\
                        )\
                    )"
        cursor.execute(sqlQuery3)
        fetchResultQuery = cursor.fetchall()

    for temp in fetchResultQuery:
        eachRow = {'model': temp[0], 'price': temp[1]}
        outputOfQuery.append(eachRow)
    
    return render(request, 'myApp/query3.html', {"out": outputOfQuery})
               
def query4(request):
    outputOfQuery = [];
    with connection.cursor() as cursor:
        # maker D는 최고 가격이 같음
        sqlQuery4 = "SELECT DISTINCT pr2.maker, p2.price, p2.model\
                    FROM (SELECT DISTINCT maker as m, max(p1.price) as mp\
                        FROM printer p1, product pr\
                        WHERE p1.model = pr.model\
                        group by maker) AS F,\
                        printer p2, product pr2\
                    WHERE F.mp = p2.price AND pr2.maker = F.m"
        cursor.execute(sqlQuery4)
        fetchResultQuery = cursor.fetchall()   
        
        for temp in fetchResultQuery:
            eachRow = {'maker': temp[0], 'price': temp[1], 'model': temp[2]}
            outputOfQuery.append(eachRow)

    return render(request, 'myApp/query4.html', {"out": outputOfQuery})


"""
sql queries for testing

sqlQuery3 = "SELECT maker, laptop.price\
            FROM laptop, product\
            WHERE laptop.model = product.model\
            GROUP BY maker \
            HAVING COUNT(maker) = 1\
            ORDER BY maker ASC"

sqlQuery3 = "SELECT MAX(DISTINCT l1.price)\
            FROM product p1\
            LEFT JOIN laptop l1\
            ON l1.model = p1.model\
            GROUP BY p1.maker\
            HAVING COUNT(p1.model) = 1\
            "
"""
        
        