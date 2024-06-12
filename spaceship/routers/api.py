from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('')
def hello_world() -> dict:
    matr1 = np.random.rand(10,10)
    matr2 = np.random.rand(10,10)
    res  = np.dot(matr1.matr2)

    return {'msg': 'Hello, World!', "\nmatr1": matr1.tolist(), "\nmatr2": matr2.tolist(), "res": res.tolist()}
