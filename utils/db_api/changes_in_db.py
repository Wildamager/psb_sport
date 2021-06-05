def change(date_text, first, first_office, second, second_office, third, third_office, fourth, fourth_office,
             additionally):
    from sqlalchemy import create_engine, Table, MetaData

    engine = create_engine('sqlite:///utils//db_api//databese_test.db', echo=True)
    meta = MetaData(engine)

    raspisanie = Table('Raspisanie', meta, autoload=True)

    conn = engine.connect()
    result = raspisanie.select()
    update_info = raspisanie.update().where(raspisanie.c.date == date_text).values(
        first=first, first_office=first_office,
        second=second, second_office=second_office,
        third=third, third_office=third_office,
        fourth=fourth, fourth_office=fourth_office,
        additionally=additionally)

    conn.execute(update_info)

    print(conn.execute(result).fetchall())
