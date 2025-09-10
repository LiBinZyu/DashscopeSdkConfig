import dashscope
from dashscope.audio.asr import *
import os


dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')
prefix = 'prefix'
target_model = "paraformer-realtime-v2"

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


# create a vocabulary
service = VocabularyService()
vocabulary_id = service.create_vocabulary(
      prefix=prefix,
      target_model=target_model,
      vocabulary=my_vocabulary)

print(f"your vocabulary id is {vocabulary_id}")