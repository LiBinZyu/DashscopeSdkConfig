import os
from typing import List
from dashscope.audio.asr import VocabularyService
from dashscope.common.logging import logger

# 确保 API Key 在环境变量中
if 'DASHSCOPE_API_KEY' not in os.environ:
    logger.error('错误：请先设置环境变量 DASHSCOPE_API_KEY')
    exit(1)


def update_vocabulary(vocabulary_id: str, vocabulary: List[dict]) -> None:
    try:
        # 创建VocabularyService实例
        service = VocabularyService(api_key=os.environ['DASHSCOPE_API_KEY'])
        
        # 调用API更新热词表
        service.update_vocabulary(vocabulary_id=vocabulary_id, 
                                 vocabulary=vocabulary)
        
        logger.info(f'热词表 {vocabulary_id} 更新成功')
        
    except Exception as e:
        logger.error(f'更新热词表时发生异常: {str(e)}')
        raise


if __name__ == '__main__':
    # 在这里填入你的 vocabulary_id
    vocabulary_id = "vocab-prefix-92aff13df7de409c995a9faac61f0ff9"
    
    # 热词表数据
    my_vocabulary = [
        {"text": "动脉", "weight": 1, "lang": "zh"},
        {"text": "静脉", "weight": 1, "lang": "zh"},
        {"text": "气管", "weight": 1, "lang": "zh"},
        {"text": "胸壁", "weight": 1, "lang": "zh"},
        {"text": "结节", "weight": 1, "lang": "zh"},
        {"text": "上叶动脉", "weight": 1, "lang": "zh"},
        {"text": "上叶静脉", "weight": 1, "lang": "zh"},
        {"text": "上叶气管", "weight": 1, "lang": "zh"},
        {"text": "右肺上叶", "weight": 1, "lang": "zh"},
        {"text": "左肺中叶", "weight": 1, "lang": "zh"},
        {"text": "左肺下叶", "weight": 1, "lang": "zh"},
        {"text": "右肺中叶", "weight": 1, "lang": "zh"},
        {"text": "左肺上叶", "weight": 1, "lang": "zh"},
        {"text": "右肺下叶", "weight": 1, "lang": "zh"},
        {"text": "淋巴结", "weight": 1, "lang": "zh"},
    ]
    
    # 更新热词表
    update_vocabulary(vocabulary_id, my_vocabulary)