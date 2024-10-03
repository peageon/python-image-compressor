import os
from PIL import Image

# 이미지 크기 조정 및 압축 함수
def resize_images(input_folder, output_folder, new_width, new_height, quality):
    # 출력 폴더가 존재하는지 확인
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 썸네일 폴더 생성
    if not os.path.exists(os.path.join(output_folder, 'thumbnails')):
        os.makedirs(os.path.join(output_folder, 'thumbnails'))
    

    # 입력 폴더 모든 파일 반복 수행
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            # img = img.convert('RGBA')  # 이미지 모드 변경 (RGBA: 색상, 투명도)

            # 썸네일 이미지 생성
            thumbnail = img.copy()
            thumbnail.thumbnail((400,300))

            # 썸네일 이미지 저장
            thumbnail.save(os.path.join(output_folder, 'thumbnails', filename.split('.')[0] + '_thumbnail.' + filename.split('.')[1]))
            
            # 이미지 크기 조정
            img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # 출력 경로 정의
            output_path = os.path.join(output_folder, filename)

            # JPEG 파일의 경우 압축하여 저장
            if filename.endswith(('.jpg', '.jpeg')):
                img_resized.save(output_path, quality=quality, optimize=True)  # 품질 조정 (1-100)
            else:
                # PNG의 경우 투명성을 비활성화하여 크기를 줄일 수 있음
                img_resized.save(output_path, optimize=True)

            print(f"{filename} 파일을 {output_folder} 폴더로 압축, 크기 조정 완료하고 저장했습니다.")

# 사용자 입력을 받아 크기 조정 함수를 호출하는 메인 함수
if __name__ == '__main__':
    # 입력 폴더 경로 요청
    input_folder = input("인풋 폴더 PATH: ")

    # 출력 폴더 경로 요청
    output_folder = input("아웃풋 폴더 PATH: ")

    # 이미지 너비 요청
    try:
        new_width = int(input("새로운 이미지 넓이: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        exit(1)

    # 이미지 높이 요청
    try:
        new_height = int(input("새로운 이미지 높이: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        exit(1)

    # 이미지 품질 요청
    try:
        quality = int(input("이미지 퀄리티 (1~100): "))
        if quality < 1 or quality > 100:
            raise ValueError
    except ValueError:
        print("1과 100중에서 숫자를 입력해주세요.")
        exit(1)

    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        exit(1)

    # 이미지 크기 조정 함수 호출
    resize_images(input_folder, output_folder, new_width, new_height, quality)
