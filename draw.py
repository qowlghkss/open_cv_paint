import cv2 as cv
import numpy as np
import sys

# 1. 초기 붓 크기 설정
brush_size = 5

# 2. 마우스 이벤트 처리 콜백 함수
def draw_brush(event, x, y, flags, param):
    global brush_size
    
    # [좌클릭 및 드래그 처리 - 파란색 붓]
    if event == cv.EVENT_LBUTTONDOWN or (event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON)):
        cv.circle(img, (x, y), brush_size, (255, 0, 0), -1)
        
    # [우클릭 및 드래그 처리 - 빨간색 붓]
    elif event == cv.EVENT_RBUTTONDOWN or (event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_RBUTTON)):
        cv.circle(img, (x, y), brush_size, (0, 0, 255), -1)

# ---------------------------------------------------------
# 3. 캔버스 준비 (빈 도화지 대신 이미지 불러오기)
# ---------------------------------------------------------
# 여러분의 이미지 파일 경로와 이름으로 변경해 주세요 (예: 'my_photo.png')
image_path = '/home/ji/Desktop/homework/1week/girl_laughing.jpg'
img = cv.imread(image_path)

# 이미지를 제대로 불러왔는지 확인 (파일이 없으면 프로그램 종료)
if img is None:
    print(f" '{image_path}' 이미지를 불러올 수 없습니다. 파일 이름과 위치를 확인해 주세요!")
    sys.exit()

# 4. 윈도우 창 설정 (우클릭 메뉴 방지를 위해 WINDOW_GUI_NORMAL 사용)
cv.namedWindow('Paint', cv.WINDOW_GUI_NORMAL)
cv.setMouseCallback('Paint', draw_brush)

print("  이미지 위에 그림 그리기를 시작합니다.")
print(" - 좌클릭 + 드래그 : 파란색 붓")
print(" - 우클릭 + 드래그 : 빨간색 붓")
print(" - [+] 키 : 붓 크기 증가 (최대 15)")
print(" - [-] 키 : 붓 크기 감소 (최소 1)")
print(" - [q] 키 : 프로그램 종료\n")

# 5. 메인 무한 루프
while True:
    cv.imshow('Paint', img)
    
    key = cv.waitKey(1) & 0xFF
    
    # [종료]
    if key == ord('q'):  
        print("프로그램을 종료합니다.")
        break            
        
    # [붓 크기 증가] + 또는 = 키
    elif key == ord('+') or key == ord('='):
        if brush_size < 15:  
            brush_size += 1
            print(f"현재 붓 크기: {brush_size} (증가)")
            
    # [붓 크기 감소] - 키
    elif key == ord('-'):  
        if brush_size > 1:   
            brush_size -= 1
            print(f"현재 붓 크기: {brush_size} (감소)")

cv.destroyAllWindows()
