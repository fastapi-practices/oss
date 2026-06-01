import oss2

from fastapi import UploadFile

from backend.common.exception import errors
from backend.common.log import log
from backend.core.conf import settings
from backend.utils.file_ops import build_filename


def get_oss_bucket() -> oss2.Bucket:
    """获取阿里云 oss bucket"""
    auth = oss2.Auth(settings.OSS_ACCESS_KEY, settings.OSS_SECRET_KEY)
    bucket = oss2.Bucket(auth, settings.OSS_ENDPOINT, settings.OSS_BUCKET_NAME)
    return bucket


def oss_put_object(file: UploadFile) -> str:
    """
    oss 简单上传（bytes）

    :param file: 上传的文件
    :return:
    """
    filename = build_filename(file)
    try:
        bucket = get_oss_bucket()

        if settings.OSS_USE_SIGNED_URL:
            res = bucket.put_object(filename, file.file)
        else:
            res = bucket.put_object(filename, file.file, headers={'x-oss-object-acl': 'public-read'})

        if settings.OSS_USE_SIGNED_URL:
            url = bucket.sign_url('GET', filename, settings.OSS_SIGNED_URL_EXPIRE_SECONDS)
        else:
            url = res.resp.response.url
    except Exception as e:
        log.error(f'上传文件 {filename} 失败：{e!s}')
        raise errors.RequestError(msg='上传文件失败')
    else:
        return url
