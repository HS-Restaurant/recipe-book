# 가상환경 생성
python3 -m venv venv

# 가상환경 실행
source venv/bin/activate

# 가상환경 종료
deactivate

# 패키지 정보 저장
pip freeze > requirements.txt

# 패키지 설치
pip install -r requirements.txt
