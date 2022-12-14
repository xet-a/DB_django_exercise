from django.shortcuts import render
from django.db import connection

def display(request):
    outputCategories = []
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQueryCategories = "SELECT categoryid, categoryname, categorydescription FROM categories;"
        cursor.execute(sqlQueryCategories)
        fetchResultCategories = cursor.fetchall()

        sqlQuery1 = "SELECT categoryname, categorydescription FROM categories WHERE categoryid=7;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultCategories:
            eachRow = {'categoryid': temp[0], 'categoryname': temp[1], 'categorydescription': temp[2]}
            outputCategories.append(eachRow)

        for temp in fetchResultQuery1:
            eachRow = {'categoryname': temp[0], 'categorydescription': temp[1]}
            outputOfQuery1.append(eachRow)

    return render(request, 'myApp/index.html',{"categories": outputCategories, "output1": outputOfQuery1})
