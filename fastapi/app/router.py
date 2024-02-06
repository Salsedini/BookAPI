from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal, engine
from sqlalchemy.orm import Session 
from schemas import BookSchema, RequestBook, Response
import crud
import model

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@router.post('/create')
async def createBook(request: RequestBook, db: Session = Depends(get_db)):
    print(f"Book Information - Title: {request.parameter.title}, Description: {request.parameter.description}")
    crud.create_book(db, book = request.parameter)
    return Response(code = 200, status = "ok", message = "Book created succesfully").dict(exclude_none = True)

@router.get("/")
async def getBook(db: Session = Depends(get_db)):
    _book = crud.get_book(db, 0, 100)
    return Response(code = 200, status = "ok", message = "Book data received", result = _book).dict(exclude_none = True)

@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _book = crud.get_book_by_id(db, id)
    return Response(code = 200, status = "ok", message = "Book data received", result = _book).dict(exclude_none = True)

@router.post("/update")
async def updateBook(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(db, book_id = request.parameter.id, 
                            title = request.parameter.title, description = request.parameter.description) 
    return Response(code = 200, status = "ok", message = "Book updated succesfully").dict(exclude_none = True)

@router.delete("/{id}")
async def deleteBook(id: int, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id = id)
    return Response(code = 200, status = "ok", message = "Book deleted succesfully").dict(exclude_none = True)