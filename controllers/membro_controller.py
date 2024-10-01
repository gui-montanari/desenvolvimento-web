from fastapi.requests import Request
from fastapi import Uploadfile

from aiofile import async_open


from uuid import uuid4

from core.configs import settings
from core.database import get_session
from models.membro_model import MembroModel
from controllers.base_controller import BaseController

class MembroController(BaseController):

    def __init__(self, request: Request) -> None:
        super().__init__(request, MembroModel)

    async def post_crud(self) -> None:
        ## Recebe dados do form
        form = await self.request.form()
        ## Cria um objeto do model
        nome: str = form.get('nome')
        funcao: str = form.get('funcao')
        imagem: Uploadfile = form.get('imagem')

        ## nome aleatorio para a imagem
        arquivo_ext: str = imagem.filename.split('.')[-1]
        novo_nome: str = f'{uuid4()}.{arquivo_ext}'

        ## instanciar o objeto
        membro: MembroModel = MembroModel(nome=nome, funcao=funcao, imagem=novo_nome)

        ##Fazer upload do arquivo
        async with async_open(f"{settings.MEDIA}/{novo_nome}", "wb") as file:
            content = await imagem.read()
            await file.write(content)

        ## Salvar no banco de dados
        async with get_session() as session:
            session.add(membro)
            await session.commit()

    async def put_crud(self, obj: object) -> None:
        ## verifica se existe o obj no banco de dados
        async with get_session() as session:
            membro: MembroModel = await session.get(self.model, obj.id)

            if membro:
                #recebe os dados do form
                form = await self.request.form

                nome: str = form.get('nome')
                funcao: str = form.get('funcao')
                imagem: Uploadfile = form.get('imagem')

                if nome and nome != membro.nome:
                    membro.nome = nome

                if funcao and funcao != membro.funcao:
                    membro.funcao = funcao

                if imagem.filename:
                    arquivo_ext: str = imagem.filename.split('.')[-1]
                    novo_nome: str = f'{uuid4()}.{arquivo_ext}'

                    membro.imagem = novo_nome

                    async with async_open(f"{settings.MEDIA}/{novo_nome}", "wb") as file:
                        content = await imagem.read()
                        await file.write(content)
                session.add(membro)
                await session.commit()