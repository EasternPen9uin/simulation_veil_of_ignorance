###################
# 라이브러리
from tkinter import filedialog, Tk
import json
from datetime import datetime
###################
#함수
# 밀리초 단위의 타임스탬프를 년월일 시분초의 문자열로 변환
def timestamp_to_datestring(timestamp_ms):
    # 밀리초 단위의 타임스탬프를 초 단위로 변환
    timestamp_sec = timestamp_ms / 1000.0
    # datetime 객체로 변환
    dt = datetime.utcfromtimestamp(timestamp_sec)
    # '년-월-일' 형식으로 변환
    date_string = dt.strftime(f'%Y-%m-%d %H:%M:%S / {timestamp_ms}')
    return date_string
###################
#코드 로직
if __name__ == "__main__":
    print("파일을 선택해주세요:")
    root = Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(
        filetypes=(("Ai-town Message jsonl", "*.jsonl"),)
    )
    filename = filepath.replace('.jsonl', '') + ".md"
    a = open(filename, 'w', ); a.close()
    lines = None
    with open(filepath, 'r', encoding='UTF8') as f:
        lines = f.readlines()

    # 전체 메시지를 _creationTime기준으로 정렬
    objs = sorted(
        list(map(lambda x : json.loads(x), lines)),
        key=lambda obj : float(obj['_creationTime'])
    )

    # 이후 messagesDict내 _conversationId를 키로 설정, 리스트 형태로 저장
    messagesDict = {}
    # conversationId가 순서대로 나열된 리스트
    cvsIdList = []
    for msgbox in objs:
        cvsId = msgbox['conversationId']
        if cvsId not in messagesDict:
            messagesDict[cvsId] = []
            cvsIdList.append(cvsId)
        messagesDict[cvsId].append(msgbox)

    # 이후 markdown 문법에 맞춰 작성 시작
    for cvsIdIdx in range(len(cvsIdList)):
        cvsId = cvsIdList[cvsIdIdx]
        with open(filename, 'a', encoding='UTF8') as f:
            f.write(f"## {cvsIdIdx}\n")
            first_talker = messagesDict[cvsId][0]["author"]
            for msg in messagesDict[cvsId]:
                talker = msg["author"]
                timeString = timestamp_to_datestring(float(msg["_creationTime"]))
                text = msg["text"].replace('\n', ' ')
                textKOR = msg["textKOR"].replace('\n', ' ') if "textKOR" in msg else None
                if talker == first_talker:
                    f.write(f"* {talker}({timeString}):  \n")
                    f.write(f'{text}\n')
                    if "textKOR" in msg:
                        f.write(f'    * {textKOR}\n')
                else:
                    f.write(f'* <span style="color:orange;">{talker}({timeString}):</span>  \n')
                    f.write(f'{text}\n')
                    if "textKOR" in msg:
                        f.write(f'    * {textKOR}\n')    
            f.write("\n\n")    
    input("완료!")

