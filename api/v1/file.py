from typing import Annotated

from fastapi import APIRouter, File, UploadFile
from starlette.concurrency import run_in_threadpool

from backend.common.dataclasses import UploadUrl
from backend.common.response.response_schema import ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.plugin.oss.utils.file_ops import oss_put_object
from backend.utils.file_ops import upload_file_verify

router = APIRouter()


@router.post('/upload', summary='OSS 文件上传', dependencies=[DependsJwtAuth])
async def oss_upload_files(file: Annotated[UploadFile, File()]) -> ResponseSchemaModel[UploadUrl]:
    upload_file_verify(file)
    url = await run_in_threadpool(oss_put_object, file)
    return response_base.success(data=UploadUrl(url=url))
