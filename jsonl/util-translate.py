MODEL = "NHNDQ/nllb-finetuned-en2ko"
###################
# 라이브러리
import os; os.environ['TRANSFORMERS_CACHE'] = './cache'
from transformers import pipeline
from tkinter import filedialog, Tk
import json
###################
# 전역변수
translator = pipeline(
    'translation', model=MODEL, device=0,
    src_lang='eng_Latn', tgt_lang='kor_Hang',
    max_length=512
)
###################
# 함수
def translate(kortxt):
    output = translator(kortxt, max_length=512)
    return output[0]['translation_text']
def translateSeveralLines(kortxt):
    translated_lists = []
    for txt in map(lambda x : x + ".", (kortxt+" ").split(". ")[:-1]):
        translated_lists.append(translate(txt))
    return " ".join(translated_lists)
###################
#코드 로직
if __name__ == "__main__":
    print("파일을 선택해주세요:")
    root = Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(
        filetypes=(("Ai-town Message jsonl", "*.jsonl"),)
    )
    a = open("./output.jsonl", 'w', ); a.close()
    lines = None
    with open(filepath, 'r', encoding='UTF8') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        print(f"진행중... ({i+1}/{len(lines)})")
        obj = json.loads(lines[i])
        obj['textKOR'] = translateSeveralLines(obj['text'])
        with open("./output.jsonl", 'a', encoding='utf-8') as a:
            a.write(json.dumps(obj, ensure_ascii=False))
            a.write('\n')
    input("완료!")
