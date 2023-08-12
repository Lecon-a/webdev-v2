from sqlalchemy import create_engine, text
from db_info import params

connection_string = f"mysql+pymysql://{params['username']}:{params['password']}@localhost:3306/{params['dbname']}?charset=utf8mb4"

engine = create_engine(connection_string)

def load_data():
    data = []
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        for row in result:
            data.append(row._asdict())
    return data