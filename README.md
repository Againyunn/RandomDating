# First_Project_Individual

본 1차 개인 프로젝트는 Django 와 Html, css, js, bootstrap 일부를 차용하여 제작하였습니다.
실제 웹사이트 구동 캡쳐 영상은 "   https://blog.naver.com/rangyun    " 개인 블로그를 통해 확인하실 수 있습니다.
  *기본적으로 mvt(model > views > templates )구조로 구성되어 있으며, 
  *실제 웹 사이트 운용코드는 templates 파일 내의 html 파일과
  *벡엔드 단의 운용코드는 views.py 파일 참고 부탁드립니다.


# 프로젝트 구조
  프로젝트 명: jaeyun 
    > 세부 프로젝트: 
        first 
        novel 
        lottos  
        project
 
 
# 세부 파일 별 코드 및 내용물 
 
jaeyun 파일
  프로젝트 통제 파일

project 파일 >> 국비지원 프로그램 시 최종 개인 프로젝트로 제출했던 프로젝트
  프로젝트 명 : random date 추천 웹 사이트
  
  templates
    random.html : 첫화면
    데이트추천 명.html : 랜덤으로 출력될 화면 (총 40개 추천목록)
    certification.html : 웹사이트 사용 설명 제공
  
  views.py
    random 함수 이용
   
   실제 구동 모습은 개인 블로그 통하여 확인 가능합니다.
   "   https://blog.naver.com/rangyun    "
   
   

first 파일
  templates
    worksheet.html >> 월별 스케쥴 관리가 가능한 웹 사이트
    login2.html >> 로그인 첫 창 구현
    test.html >> h1 헤드 출력 테스트용 
    a.html >> h1 헤드 출력 테스트용 


lottos 파일 (template없이 views에서 간단한 문자 출력만 하도록 코드 구축)
  views.py
    로또 번호를 랜덤으로 출력해주는 웹 사이트


novel 파일
  templates
    novel.html >> 웹 주소 창에 이름을 입력하면 해당 이름이 웹 사이트 내에 출력되는 웹 사이트
    


