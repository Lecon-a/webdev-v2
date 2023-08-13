from sqlalchemy import create_engine, text
import os

connection_string = os.environ.get('DB_CONNECTION_STRING')
engine = create_engine(connection_string)

def load_data():
    data = []
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        for row in result:
            data.append(row._asdict())
    return data