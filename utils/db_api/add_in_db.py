def add_info(conn, raspisanie, date_text, first, first_office, second, second_office, third, third_office, fourth, fourth_office,
             additionally):


    result = raspisanie.select()


#######################НАДО ЗАХУЯРИТЬ ФУНКЦИЮ

    test1 = raspisanie.insert().values(date=date_text, first=first, first_office=first_office,
                                       second=second, second_office=second_office,
                                       third=third, third_office=third_office,
                                       fourth=fourth, fourth_office=fourth_office,
                                       additionally=additionally)
    conn.execute(test1)

    print(conn.execute(result).fetchall())
