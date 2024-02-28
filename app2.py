from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uid

app = FastAPI()

posts = []

#post model
class Post(BaseModel):
    id:Optional[str]
    tilte:str
    autor:str
    content:Text
    date_at:datetime = datetime.now
    date_post:Optional[datetime] 
    public:bool = False

'''@app.get('/')
def root():
    return {"welcome": "primer contacto"}'''

@app.get('/dataveiws')
def dataviews():
    return posts

@app.post('/dataveiws')
def savedata(data: Post):
    Post.id = uid()
    posts.append(data.dict())
    return posts[-1]

@app.get('/dataveiws/{id}')
def dataview(id:str):
    for post in posts:
        if post["id"] == id:
            return post
    raise HTTPException(status_code=404, detail="post not found")

@app.delete('/dataveiws/{id}')
def datadelete(id:str):
    for index, post in enumerate(posts):
        if post["id"]== id:
            posts.pop(index)
            return {"message":"Post a sido eliminada"}
    raise HTTPException(status_code=404, detail="post not found")

@app.put('/dataveiws/{id}')
def dataupdate(id:str, postup:Post):
    for index, post in enumerate(posts):
        if post["id"]== id:
            posts[index]["tilte"] = postup.tilte
            posts[index]["autor"] = postup.autor
            posts[index]["content"] = postup.content
            return {"message":"Post a sido actualizo"}
    raise HTTPException(status_code=404, detail="post not found")
     

