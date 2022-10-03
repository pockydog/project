import uvicorn
from app import create_app

app = create_app()
from controllers import *

app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)