#  [과제 1] 이미지 로드 및 흑백(Grayscale) 변환 출력

##  프로젝트 개요
OpenCV를 활용하여 원본 이미지(`soccer.jpg`)를 불러오고, 화면 크기에 맞게 리사이징한 뒤, 흑백 이미지로 변환하여 원본과 나란히 비교 출력하는 프로그램입니다.


##  주요 코드 해석 (Key Code Analysis)

### 1. 이미지 해상도 최적화 (`cv.resize`)
```python
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
```
* **설명:** 고해상도 이미지를 그대로 띄울 경우 화면을 벗어나는 문제를 방지하기 위해, `fx`와 `fy` 옵션을 0.5로 주어 이미지의 가로/세로 길이를 각각 50%로 축소했습니다.

### 2. 채널(Channel) 차원 일치 및 가로 병합 (`np.hstack`)
```python
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_img_3c = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)
combined_img = np.hstack((img, gray_img_3c))
```
* **설명 (핵심 포인트):** Numpy의 `hstack` 배열 병합 기능을 사용하려면 두 이미지의 형태(Shape)가 완전히 동일해야 합니다. 원본 `img`는 3채널(B,G,R)이지만, 흑백으로 변환된 `gray_img`는 1채널이므로 그대로 병합하면 차원 에러가 발생합니다. 이를 해결하기 위해 `cv.COLOR_GRAY2BGR`을 사용하여 흑백의 시각적 상태는 유지한 채 데이터 구조만 3채널로 변환한 뒤 안전하게 병합을 수행했습니다.

##  실행 방법
```bash
python call_image.py
```
* 창이 열리면 임의의 키보드 버튼을 눌러 프로그램을 종료할 수 있습니다.

##  실행 결과 화면
![실행결과](./call_image/call_image.png)
![실행결과2](./call_image/call_image2.png)
![실행결과3](./call_image/call_image3.png)
*원본 이미지(좌)와 흑백 변환 이미지(우)를 가로로 병합하여 출력한 모습*

## 전체 코드
```python
import cv2 as cv
import numpy as np

# 1. cv.imread()를 사용하여 이미지 로드 
# (주의: 같은 폴더에 'sample.jpg' 파일이 있어야 합니다. 본인의 이미지 파일명으로 변경하세요)
img = cv.imread('/home/ji/Desktop/homework/1week/soccer.jpg')

if img is None:
    print("이미지를 불러올 수 없습니다. 파일 이름이나 경로를 확인해 주세요.")
else:
    #  [추가된 부분] 이미지 크기를 가로/세로 각각 절반(50%)으로 줄이기
   
    img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

    # 2. cv.cvtColor() 함수를 사용해 이미지를 그레이스케일로 변환
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


    #  [핵심 포인트] np.hstack()을 위한 차원 맞추기
    # 원본(img)은 3채널(B,G,R)이고, 변환된 gray_img는 1채널(흑백)입니다.
    # 두 이미지의 모양(shape)이 다르면 np.hstack()으로 붙일 때 에러가 발생합니다.
    # 따라서 흑백 이미지를 시각적인 변화 없이 형태만 3채널로 변환해 줍니다.
    gray_img_3c = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)

    # 3. np.hstack() 함수를 이용해 원본 이미지와 그레이스케일 이미지를 가로로 연결
    combined_img = np.hstack((img, gray_img_3c))

    # 4. cv.imshow()와 cv.waitKey()를 사용해 결과를 화면에 표시
    cv.imshow('Original vs Grayscale', combined_img)
    
    # 아무 키나 누를 때까지 무한정 대기 (0)
    cv.waitKey(0)
    
    # 키가 눌리면 모든 창 닫기
    cv.destroyAllWindows()

```