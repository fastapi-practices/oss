# OSS

阿里云 OSS 文件上传插件

## 全局配置

在 `backend/core/conf.py` 中添加以下内容：

```python
##################################################
# [ Plugin ] oss
##################################################
# .env
OSS_ACCESS_KEY: str
OSS_SECRET_KEY: str

# 基础配置（in plugin.toml）
OSS_BUCKET_NAME: str
OSS_ENDPOINT: str
OSS_USE_SIGNED_URL: bool
OSS_SIGNED_URL_EXPIRE_SECONDS: int
```
