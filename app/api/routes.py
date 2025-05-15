from fastapi import APIRouter, Query, HTTPException
from app.services.operations import add, subtract, multiply, divide

router = APIRouter()


@router.get("/add")
def add_numbers(a: float = Query(...), b: float = Query(...)):
    return {"result": add(a, b)}


@router.get("/subtract")
def subtract_numbers(a: float = Query(...), b: float = Query(...)):
    return {"result": subtract(a, b)}


@router.get("/multiply")
def multiply_numbers(a: float = Query(...), b: float = Query(...)):
    return {"result": multiply(a, b)}


@router.get("/divide")
def divide_numbers(a: float = Query(...), b: float = Query(...)):
    try:
        return {"result": divide(a, b)}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by 0 issue")
