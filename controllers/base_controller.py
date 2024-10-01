from typing import List, Optional

from fastapi import HTTPException
from fastapi.requests import Request
from sqlalchemy.future import select

from core.database import get_session

class BaseController:
    def __init__(self, request: Request, model: object) -> None:
        self.request = request
        self.model = model	

    async def get_all_crud(self) -> Optional[List[object]]: 
        ## Retorna todos os registros do model
        async with self.request.app.state.engine.begin() as conn:
            result = await conn.execute(select(self.model))
            return result.scalars().all()
        
    async def get_one_crud(self, id_obj: int) -> Optional[object]:
        ## Retorna o objeto especificado pelo id_obj ou None
        async with self.request.app.state.engine.begin() as conn:
            result = await conn.execute(select(self.model).where(self.model.id == id_obj))
            return result.scalar_one

    async def post_crud(self) -> None:
        ## Cria um novo registro no model
        raise NotImplementedError("Você precisa implementar esse método.")

    async def put_crud(self, obj: object) -> None:
        ## Atualiza um registro no model
        raise NotImplementedError("Você precisa implementar esse método.")

    async def del_crud(self, id_obj: int) -> None:
        ## Deleta um registro no model
        async with get_session() as session:
            obj: self.model = await session.get(self.model, id_obj)
            if obj:
                session.delete(obj)
                await session.commit()
            else:
                raise HTTPException(status_code=404, detail="Registro não encontrado.")