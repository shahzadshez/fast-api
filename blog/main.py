from fastapi import FastAPI


app = FastAPI()

@app.get('/health')
def health_check():
    return 'Healthy'


@app.post(/create)
def create_blog():
    pass
