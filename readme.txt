python -m venv venv  
venv\Scripts\activate
pip install fastapi
pip install uvicorn
pip list
pip freeze
pip freeze > requirements.txt
uvicorn app:app --reload

https://www.sqlalchemy.org/
https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/
https://docs.pydantic.dev/latest/
https://docs.python.org/3/library/uuid.html