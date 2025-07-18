import os
from dashscope.audio.asr import *
from dashscope.common.logging import logger

# 确保 API Key 在环境变量中
if 'DASHSCOPE_API_KEY' not in os.environ:
    logger.error('错误：请先设置环境变量 DASHSCOPE_API_KEY')
    exit()

try:
    # 初始化服务
    service = VocabularyService()

    # 调用 list_vocabularies 方法查询
    # 文档中提到，默认查询第0页，每页10条记录
    vocabulary_list = service.list_vocabularies()

    print("查询成功！找到以下热词表：")
    print("=" * 40)
    if not vocabulary_list:
        print("未找到任何已创建的热词表。")
    else:
        for vocab in vocabulary_list:
            print(f"  ID: {vocab.get('vocabulary_id')}")
            print(f"  状态: {vocab.get('status')}")
            print(f"  创建时间: {vocab.get('gmt_create')}")
            print("-" * 20)

except Exception as e:
    logger.error("调用SDK时发生异常: %s", e)