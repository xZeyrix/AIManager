from fastapi import FastAPI, Path, Query, Body, Header

app = FastAPI(title='KAKOI TO SHOP')

@app.get('/')
def status() -> dict[str, bool]:
    return {'status': True}



