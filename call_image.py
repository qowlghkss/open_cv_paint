import cv2 as cv
import numpy as np

# 1. cv.imread()를 사용하여 이미지 로드 
# (주의: 같은 폴더에 'sample.jpg' 파일이 있어야 합니다. 본인의 이미지 파일명으로 변경하세요)
img = cv.imread('/home/ji/Desktop/homework/1week/soccer.jpg')

if img is None:
    print("이미지를 불러올 수 없습니다. 파일 이름이나 경로를 확인해 주세요.")
else:
    # 🚨 [추가된 부분] 이미지 크기를 가로/세로 각각 절반(50%)으로 줄이기
   
    img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

    # 2. cv.cvtColor() 함수를 사용해 이미지를 그레이스케일로 변환
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


    # 🚨 [핵심 포인트] np.hstack()을 위한 차원 맞추기
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