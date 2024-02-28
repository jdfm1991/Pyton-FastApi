from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://sa:GconfiSql.2022..@localhost:3306/fastapi")
meta= MetaData()

connect = engine.connect()