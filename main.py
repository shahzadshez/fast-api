from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get('/')
def index():
    return {
        'data': {
            'name': "shahzad"
        }
    }


@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blog/unpublished')
def unpublished_blog():
    return {
        'data': 'unpublished'
    }

@app.get('/blogs')
def about(num_blogs, published: bool, sort: Optional[bool] = None):
    list1 = [1,4,5,2,7]
    if not published:
        print(published)
        return 'None published'
    elif sort:
        return sorted(list1)
    else:
        return {'data': f'blog number that are published {num_blogs}'}


@app.get('/blog/{blog_id}')
def about(blog_id: int):
    return {'data': f'blog number {blog_id}'}


@app.get('/blog/{blog_id}/comments')
def about(blog_id: int):
    return {'data': f' comments of blog id  {blog_id}',
            'Comments': 'your comment'}

# blogs = []

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/create')
def create_blog(request: Blog):
    return {'data':f'request is created with title {request.title}'}

