from fastapi import FastAPI
import models, database
from routers.user_router import router as user_router
from routers.blog_router import router as blog_router
from routers.login_router import router as login_router

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(router=login_router, prefix="/login", tags=["login"])
app.include_router(router=user_router, prefix="/user", tags=["user"])
app.include_router(router=blog_router, prefix="/blog", tags=["blog"])


@app.get("/", tags=["home"])
def home():
    return{"Welcome to our Blog"}

@app.get("/")
def home():
    return {"Welcome to our Blog"}


@app.get("/about")
def about():
    return {"About us page"}


@app.get("/contact")
def contact():
    return {"Contact us"}