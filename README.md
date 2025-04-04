제목 : 안전모착용 인원 탐지 AI구현(YOLOv8 사용)


개요 : 본 프로젝트는 산업 현장에서 촬영된 사진을 분석하여, 작업자의 안전모 착용여부를
       탐지하는 AI 시스템을 개발합니다.
       
      Roboflow 플랫폼을 활용한 데이터셋 구축 및 관리, Google Colab 환경에서의 
      YOLOv8 모델 학습, 그리고 Django 프레임워크를 이용한 웹 기반의 사용자 
      인터페이스 및  API 구축을 통해 실용적인 안전 관리 솔루션을 제공하고자 합니다.

프로젝트 기간 : 25.04.14 ~ 25.04.23 ( 10일 )

개발 인원 및 본인 역할 : 1인 개발로 진행되었으며, 기획부터 개발 전 과정 수행

주요 기술 : Python,HTML,CRUD,Django, 딥러닝및데이터전처리,데이터증강,데이터라벨링

개발 환경 : roboflow.com, Goolgle Colab,Django Framework,Oracle 21C, YOLOv8, 캡처도구

기대효과 : 이미지기반의 자동화된 안전모착용여부 감시로 효율적 안전관리를 가능하게 합니다.

           1.사고예방기여 : 안전모 미착용 작업자를 신속하게 파악하고 경고함으로써 안전사고
             발생 위험을 감소시킵니다.
           2.객관적인 안전 데이터 확보 : 분석 결과를 데이터베이스에 저장하여 안전 관리 현황
             을 객관적으로 파악하고, 데이터 기반의 안전 정책 수립에 활용할 수 있습니다.


1. roboflow.com 이용하여 데이터 확보하기
   
  [1] 관련 데이터셋 확보하기
  
  [2] app.roboflow.com/majustory 나의 계정을 통하여 내가 만든 데이터를 가지고 증강 작업후 라벨링 만들기
  
  [3] roboflow 데이터셋 + 나의 데이터셋(majustory)으로 훈련데이터 확보하기             

![image](https://github.com/user-attachments/assets/d71cd1f0-aed2-4440-bf86-dcdd4fb78442)
![image](https://github.com/user-attachments/assets/54701544-b0f4-4bba-9357-f197b7b3fad8)


2.Goolgle Colab 이용하여 데이터 훈련하기

[1] 가져온 데이터를 이용하여 model 만들기

[2] hardhat_model.pt로 저장하기

![image](https://github.com/user-attachments/assets/c1d2f5af-d705-49ef-a74c-8b0c28e2764d)

![yolo11](https://github.com/user-attachments/assets/3451a1dc-4762-486f-b469-4daa7b8c8eac)



3. 장고 프레임워크을 이용한 훈련하기
   
 [1] 안전모 사진을  hardhat_model.pt 모델을 이용하여 안전모 착용유무와 인원수를 파악한다.
 
 [2] 신뢰는 0.3 이상으로 추출탐지 설정하여 진행함
 
 [3] 오른쪽 결과 이미지는 4명의 안전모착용자가 나타남

![image](https://github.com/user-attachments/assets/79a130c8-76b6-426e-8c6f-c1a63c563a29)

![yolo12](https://github.com/user-attachments/assets/c18e1009-30bb-4411-88e2-9201989c564f)
![yolo13](https://github.com/user-attachments/assets/fe194f1e-75f3-4563-ab04-2a982b4bd4f2)

4. 장고프레임워크( Gemini-2.0 flask )
   
   [1] 이미지 분석전 : 기본에 분석한 결과가 출력된다
   
   [2] 이미지 분석후 : 이미지 입력후 “이미지 분석”  을 누루면 이미지에 대한 설명이 나타난다

![yolo14](https://github.com/user-attachments/assets/2ac4146b-c66d-48ec-9f0f-7a4899d29c42)


* gemini-2-flask 모델을 이용한 이미지 분석
  
1) 폼의 값을 받아 온다

2) 이미지를 파일화 한다

3) 모델에 요청사항을 추가한다

3) 분석한 결과를 테이블에 저장한다

4) 분석한 결과와 테이블값을 context에 넣는다.

5) 화면으로 넘긴다

![yolo15](https://github.com/user-attachments/assets/98611efb-c291-4e38-b9ae-8a3ccdb24845)

* 테이블 구성

![yolo16](https://github.com/user-attachments/assets/434e39d0-0c89-4c02-85ca-8f1ddcc1e3be)

-- 이상 --






