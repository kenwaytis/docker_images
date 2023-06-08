from typing import Union

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[
    Union[str, None],
    Query(max_length=50)
    ] = None
    ):
    """
    FastAPI will now: FastAPI 现在将：

    Validate the data making sure that the max length is 50 characters
    验证数据确保最大长度为 50 个字符
    Show a clear error for the client when the data is not valid
    当数据无效时向客户端显示一个明确的错误
    Document the parameter in the OpenAPI schema path operation (so it will show up in the automatic docs UI)
    在 OpenAPI 架构路径操作中记录参数（因此它将显示在自动文档 UI 中）
    
    Notice that the default value is still None, so the parameter is still optional.
    请注意，默认值仍然是 None ，因此该参数仍然是可选的。
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
