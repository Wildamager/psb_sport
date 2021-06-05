


def prosmotr_raspisaniya(day):
    from sqlalchemy import create_engine, Table, MetaData, select

    engine = create_engine('sqlite:///utils//db_api//databese_test.db', echo=True)
    conn = engine.connect()
    meta = MetaData(engine)
    raspisanie = Table('Raspisanie', meta, autoload=True)
    s = select([raspisanie]).where(raspisanie.c.date == day)

    result1 = conn.execute(s).fetchall()
    print('#####################################################')
    print(result1[0])
    return result1
