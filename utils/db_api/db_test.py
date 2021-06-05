from sqlalchemy import create_engine, select, Table, Column, String, MetaData, ForeignKey, Date
import datetime
meta = MetaData()

raspisanie = Table('Raspisanie', meta,
                   Column('date', Date, primary_key=True),
                   Column('first', String(10), nullable=False), Column('first_office', String(10)),
                   Column('second', String(10), nullable=False), Column('second_office', String(10)),
                   Column('third', String(10), nullable=False), Column('third_office', String(10)),
                   Column('fourth', String(10), nullable=False), Column('fourth_office', String(10)),
                   Column('additionally', String(100)),
                   )

print(raspisanie.c)

engine = create_engine('sqlite:///databese_test.db', echo=True)
meta.create_all(engine)

conn = engine.connect()

test1 = raspisanie.insert().values(date=datetime.date(2021, 3, 29), first='СУБД', first_office='219-5',
                                   second='МЛТА', second_office='219-5',
                                   third='сампо', third_office='',
                                   fourth='ВПР', fourth_office='228',
                                   additionally='На Субд 3 практика')
conn.execute(test1)

s = select([raspisanie]).where(raspisanie.c.date == datetime.date(2021, 3, 29))
result = conn.execute(s)
print(result)
