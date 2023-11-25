from typing import Optional
from uuid import uuid4 as uuid
<<<<<<< HEAD
from fastapi import FastAPI, HTTPException 
=======
from fastapi import FastAPI
>>>>>>> 34bb45e2a7b9fb33de3293275f92ed8227689fe7
from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional [str]=None
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str

app= FastAPI()

productos= []

@app.get('/')
def index():
    return {'mensaje':'Bienvenidos a la API de productos'}

@app.get('/producto')
def obt_productos():
    return productos

@app.post('/producto')
def crear_producto(producto: Producto):
    producto.id= str(uuid())
    productos.append(producto)
    return {'mensaje':'Producto creado satisfactoriamente'}


@app.get('/producto/{producto_id}')
def obtener_producto_por_id(producto_id: str):
<<<<<<< HEAD
    resultado = list (filter(lambda p: p.id == producto_id, productos))

    if len(resultado):
        return resultado[0]
        
    raise HTTPException(status_code=404, detail=f'El producto con el ID {producto_id} no fue encontrado en el sistema.')
=======
    for p in productos:
        if p.id == producto_id:
            return p
        
    return {'mensaje': f'El producto con el ID {producto_id}no fue encontrado'}
>>>>>>> 34bb45e2a7b9fb33de3293275f92ed8227689fe7

