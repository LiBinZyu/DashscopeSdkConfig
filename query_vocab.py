import os
from os.path import defpath

from dashscope.audio.asr import *
from dashscope.common.logging import logger

def list_vocabularies(prefix, page_index, page_size)->None :
    if 'DASHSCOPE_API_KEY' not in os.environ:
        logger.error('错误：请先设置环境变量 DASHSCOPE_API_KEY')
        exit()

    try:
        service = VocabularyService()
        vocabulary_list = service.list_vocabularies(prefix, page_index, page_size)

        print("查询成功！找到以下热词表：")
        print("=" * 40)
        if not vocabulary_list:
            print("未找到任何已创建的热词表。")
        else:
            for vocab in vocabulary_list:
                vocab_id = vocab.get('vocabulary_id')
                print(f"  ID: {vocab_id}")
                print(f"  状态: {vocab.get('status')}")
                print(f"  创建时间: {vocab.get('gmt_create')}")
                print(f"  更新时间: {vocab.get('gmt_modified')}")
                print("-" * 20)
                # 查询并打印详细信息
                query_vocab(vocab_id)
                print("\n")

    except Exception as e:
        logger.error("调用SDK时发生异常: %s", e)

def query_vocab(vocabulary_id)->None :
    if 'DASHSCOPE_API_KEY' not in os.environ:
        logger.error('错误：请先设置环境变量 DASHSCOPE_API_KEY')
        exit()

    try:
        service = VocabularyService()
        vocabulary = service.query_vocabulary(vocabulary_id)
        print(f"  状态: {vocabulary.get('status')}")
        print(f"  目标模型: {vocabulary.get('target_model')}")
        print(f"  创建时间: {vocabulary.get('gmt_create')}")
        print(f"  更新时间: {vocabulary.get('gmt_modified')}")
        print("  词汇项:")
        print("  " + "-" * 20)
        for i, item in enumerate(vocabulary.get('vocabulary', [])):
            print(f"    {i+1:2d}. 文本: {item.get('text'):<10} 语言: {item.get('lang'):<2} 权重: {item.get('weight')}")

    except Exception as e:
        logger.error("调用SDK时发生异常: %s", e)

if __name__ == '__main__':
    list_vocabularies(None, 0, 10)