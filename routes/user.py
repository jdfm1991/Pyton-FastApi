from fastapi import APIRouter
from config.conect_db import connect
from models.user import users
from schemas.user import Users
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
user = APIRouter()


@user.get('/users')
def getdata():
    return connect.execute(users.select()).fetchall()

@user.post('/users')
def savedata(user: Users):
    new_user = user.dict()
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = connect.execute(users.insert().values(new_user))
    print(result)
    return "aqui"


'''@user.get('/dataveiws')
def dataviews():
    return posts

@user.post('/dataveiws')
def savedata(data: Post):
    Post.id = uid()
    posts.userend(data.dict())
    return posts[-1]

@user.get('/dataveiws/{id}')
def dataview(id:str):
    for post in posts:
        if post["id"] == id:
            return post
    raise HTTPException(status_code=404, detail="post not found")

@user.delete('/dataveiws/{id}')
def datadelete(id:str):
    for index, post in enumerate(posts):
        if post["id"]== id:
            posts.pop(index)
            return {"message":"Post a sido eliminada"}
    raise HTTPException(status_code=404, detail="post not found")

@user.put('/dataveiws/{id}')
def dataupdate(id:str, postup:Post):
    for index, post in enumerate(posts):
        if post["id"]== id:
            posts[index]["tilte"] = postup.tilte
            posts[index]["autor"] = postup.autor
            posts[index]["content"] = postup.content
            return {"message":"Post a sido actualizo"}
    raise HTTPException(status_code=404, detail="post not found")
     

'''