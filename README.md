# simulation_veil_of_ignorance

"ChatGPT, 로컬 언어모델로 수행하는 사회 시뮬레이션 가능성 검토"(가제) (2024 제8회 인문 페스티벌 제8회 인공지능인문학 대학생 학술논문 경연대회 제출용) 학술 논문에 사용된 코드 및 대화 로그 파일 입니다.

## 파일 설명
* /
    * gpt.pdf, mistral.pdf, openhermes.pdf : 각 모델 파일 별 대화 내역 pdf입니다.  
    * runOllama.ipynb : 두 로컬 모델(mistralai/Mistral-7B-Instruct-v0.2, teknium/OpenHermes-2.5-Mistral-7B) 구동시 colab상에서 사용한 코드입니다.  
* /Modelfiles  
    * Modelfile4AITownMistral : mistralai/Mistral-7B-Instruct-v0.2 모델을 ollama에서 create할 때 사용된 Modelfile입니다.  
    * Modelfile4AITownOpenHermes : teknium/OpenHermes-2.5-Mistral-7B 모델을 ollama에서 create할 때 사용된 Modelfile입니다.  
* /jsonl:  
    * util-translate.py : 대화 데이터 파일(messages/documents.jsonl)의 json 구조 내에 한국어 기계번역을 추가하는 코드입니다. 기계번역에는 [NHNDQ/nllb-finetuned-en2ko](https://huggingface.co/NHNDQ/nllb-finetuned-en2ko)모델이 사용합니다.  
    * util-jsonl2markdown : 대화 데이터 파일을 마크다운 파일(.md)로 변환하는 코드입니다.  
    * gpt.jsonl, mistral.jsonl, openhermes.jsonl : 대화 데이터 파일입니다. util-translate.py파일로 이미 전처리를 끝낸 파일입니다.  
    * reader.html : 대화 데이터 파일을 열람할 수 있는 간단한 리더입니다. 검색 및 번역 전환 기능을 제공합니다.  
* /ai-town:  
    * characters.ts, constants.ts, conversation.ts : a16z-infra/ai-town의 원본 코드에서 수정한 부분입니다. 