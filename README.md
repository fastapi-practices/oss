# OSS

阿里云 OSS 文件上传插件，支持文件上传、删除和访问地址生成

## 插件类型

- 应用级插件

## 配置说明

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

在 `backend/.env` 中添加以下内容：

```env
# [ Plugin ] oss
OSS_ACCESS_KEY=''
OSS_SECRET_KEY=''
```

插件目录下 `plugin.toml` 的 `[settings]` 中包含以下内容：

```toml
[settings]
OSS_BUCKET_NAME = 'fba-test'
OSS_ENDPOINT = 'https://oss-cn-hangzhou.aliyuncs.com'
OSS_USE_SIGNED_URL = true
OSS_SIGNED_URL_EXPIRE_SECONDS = 300
```

## 使用方式

1. 安装并启用插件后，重启后端服务
2. 配置阿里云 OSS AccessKey、SecretKey、Bucket 和 Endpoint
3. 通过文件接口上传或删除文件
4. 启用签名地址后，文件访问 URL 会带有过期时间

## 卸载说明

- 卸载插件后，建议同步移除 OSS 相关环境变量和插件基础配置
- 如业务中保存了 OSS 文件引用，请按业务需要清理远端文件或引用数据

## 联系方式

- 作者：`wu-clan`
- 反馈方式：提交 Issue 或 PR
