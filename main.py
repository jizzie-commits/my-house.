import math

def get_valid_float(prompt, min_val=0.0, max_val=10000.0):
    """
    [평가 요소 6] 입력 오류 및 런타임 에러 방지를 위한 예외 처리 함수
    """
    while True:
        try:
            val = float(input(prompt))
            if val < min_val or val > max_val:
                print(f"[경고] {min_val} 이상 {max_val} 이하의 수치를 입력해주세요.")
                continue
            return val
        except ValueError:
            print("[에러] 문자가 입력되었습니다. 숫자만 정확히 입력해주세요.")

def main():
    print("=" * 60)
    print(" GeoPersona Arch - 아기자기 맞춤형 소형 건축 설계 프로그램")
    print("=" * 60)

    # 1. 귀여운 취향 데이터 입력
    print("\n[1] 원하는 아기자기한 건축 스타일을 선택하세요:")
    print("  1) 동화 속 오두막 스타일 (뾰족 지붕 + 원목 감성)")
    print("  2) 아기자기 버섯/큐브 스타일 (동글동글 형태 + 파스텔 컬러)")
    style_choice = input("선택 (1 또는 2): ").strip()
    if style_choice not in ['1', '2']:
        print("[안내] 잘못된 입력으로 기본값(1번 동화 오두막)으로 설정됩니다.")
        style_choice = '1'

    # 2. 기후 및 지형 데이터 입력
    print("\n[2] 설치할 장소의 기후 및 지형 정보 입력:")
    snow = get_valid_float("  - 연중 최대 적설량 (cm): ", 0, 500)
    wind = get_valid_float("  - 최대 풍속 (m/s): ", 0, 100)
    slope = get_valid_float("  - 대지 경사도 (도, °): ", 0, 90)
    sunlight = get_valid_float("  - 일일 평균 일조시간 (시간): ", 1, 24)
    area = get_valid_float("  - 희망 건축 면적 (평, 3~10평 권장): ", 1, 30)

    # 3. 건축 알고리즘 처리
    # (1) 지붕 형태 계산 (디자인 감성 + 기후 대응)
    if snow >= 50:
        roof_type = "동화 속 삼각 뾰족지붕 (Gable Roof, 60°)"
        roof_detail = "눈이 쏟아져 내리는 안전함과 빨간 기와 포인트의 귀여운 느낌"
    else:
        if style_choice == '2':
            roof_type = "아기자기 버섯형 돔 지붕 (Mushroom Dome)"
            roof_detail = "동글동글한 모서리로 바람 저항을 줄이고 장난감 같은 감성 연출"
        else:
            roof_type = "아담한 외경사 파스텔 지붕 (15°)"
            roof_detail = "빗물 배수가 원활하고 조그만 다락방 공간 확보 가능"

    # (2) 기초 및 외장재 추천
    foundation = "트리하우스 느낌의 오두막 기둥 기초 (Stilt)" if slope >= 15 else "아담한 단층 매트 기초"
    facade = "내후성 파스텔 톤 스틸 판넬 (강풍 방지)" if wind >= 25 else "크림아이보리 원목 파판 & 민트 포인트 외장재"

    # (3) 디테일 창호 설계
    window_spec = "동그란 격자 창문 & 미니 아치형 도어" if style_choice == '2' else "삼각 다락 창문 & 작은 코너 창"

    # (4) 오프그리드 태양광 패널 수 계산
    solar_panels = math.ceil((area * 1.5) / sunlight)

    # 4. 결과 리포트 출력
    print("\n" + "=" * 60)
    print(" [GeoPersona Arch] 귀여운 소형 건축물 최종 추천 브리프")
    print("=" * 60)
    print(f"■ 건축 컵셉 디자인 : {'동화 오두막' if style_choice == '1' else '버섯 큐브 하우스'}")
    print(f"■ 추천 지붕 형태   : {roof_type}")
    print(f"   └ 디자인 특징   : {roof_detail}")
    print(f"■ 대지 기초 구조   : {foundation} (경사도: {slope}°)")
    print(f"■ 권장 파스텔 자재 : {facade}")
    print(f"■ 아기자기 창호   : {window_spec}")
    print(f"■ 미니 태양광 패널 : {solar_panels}개 (일조시간 {sunlight}시간 기준)")
    print("=" * 60)

if __name__ == "__main__":
    main()
