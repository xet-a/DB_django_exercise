from django.shortcuts import render
from django.db import connection

def display(request):
    outputOfQuery1 = []; outputOfQuery2 = []; outputOfQuery3 = []; outputOfQuery4 = []; 
    with connection.cursor() as cursor:
        sqlQuery1 = "SELECT AVG(hd) FROM pc"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()
        
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
        fetchResultQuery2 = cursor.fetchall()
        #print(len(fetchResultQuery2))
        
        """
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
        fetchResultQuery3 = cursor.fetchall()
        #print(fetchResultQuery3)
        
        # maker D는 최고 가격이 같음
        sqlQuery4 = "SELECT DISTINCT pr2.maker, p2.price, p2.model\
                    FROM (SELECT DISTINCT maker as m, max(p1.price) as mp\
                        FROM printer p1, product pr\
                        WHERE p1.model = pr.model\
                        group by maker) AS F,\
                        printer p2, product pr2\
                    WHERE F.mp = p2.price AND pr2.maker = F.m"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery2:
            eachRow = {'maker': temp[0], 'num': temp[1], 'avg': temp[2]}
            outputOfQuery2.append(eachRow)
        
        for temp in fetchResultQuery3:
            eachRow = {'model': temp[0], 'price': temp[1]}
            outputOfQuery3.append(eachRow)

        for temp in fetchResultQuery4:
            eachRow = {'maker': temp[0], 'price': temp[1], 'model': temp[2]}
            outputOfQuery4.append(eachRow)

    return render(request, 'myApp/index.html',\
        {"out1": fetchResultQuery1, "out2": outputOfQuery2, "out3": outputOfQuery3, "out4": outputOfQuery4})
