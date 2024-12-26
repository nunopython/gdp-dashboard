import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Nanum Gothic 폰트 경로 설정
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
font_prop = fm.FontProperties(fname=font_path)  # 폰트 속성 생성

# matplotlib에 폰트 설정
plt.rcParams['font.family'] = font_prop.get_name()  # 폰트 이름 가져오기
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 현재 설정된 폰트 이름 출력 (디버깅용)
print(f"현재 설정된 폰트: {font_prop.get_name()}")



# Title and description
st.title("상권 분석 대시보드")
st.markdown("""
    이 대시보드는 상권 데이터를 분석하여 시각화하고,
    다양한 조건에 따라 데이터를 탐색할 수 있도록 합니다.
""")

# Sidebar for file upload
st.sidebar.header("데이터 업로드")
uploaded_file = st.sidebar.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding='cp949')
    st.sidebar.success("파일이 업로드되었습니다.")
    
    # Show uploaded data
    if st.checkbox("데이터 보기"):
        st.write(data)

    # Select analysis type
    analysis_type = st.sidebar.selectbox(
        "분석 유형 선택", 
        ["전체 점포 수", "개업/폐업 점포 수", "상권 활력도", "3년 내 폐업 비율"]
    )

    # 전체 점포 수 분석
    if analysis_type == "전체 점포 수":
        st.subheader("전체 점포 수 분석")
        plt.figure(figsize=(10, 6), dpi=300)
        plt.plot(data['기간'], data['전체점포수'], marker='o', label='전체 점포 수')
        plt.title('기간에 따른 전체 점포 수')
        plt.xlabel('기간')
        plt.ylabel('점포 수')
        plt.grid(True)
        plt.legend()

        # X축 간격 조정 (3개월 단위)
        xticks_interval = 3  # 3개월 간격
        xticks = range(0, len(data['기간']), xticks_interval)
        plt.xticks(xticks, [data['기간'][i] for i in xticks], rotation=45)

        st.pyplot(plt)

    # 개업/폐업 점포 수 분석
    elif analysis_type == "개업/폐업 점포 수":
        st.subheader("개업 및 폐업 점포 수 분석")
        plt.figure(figsize=(10, 6), dpi=300)
        plt.plot(data['기간'], data['개업점포'], marker='o', label='개업 점포 수', color='blue')
        plt.plot(data['기간'], data['폐업점포'], marker='o', label='폐업 점포 수', color='red')
        plt.title('기간에 따른 개업 및 폐업 점포 수')
        plt.xlabel('기간')
        plt.ylabel('점포 수')
        plt.grid(True)
        plt.legend()

        # X축 간격 조정 (3개월 단위)
        xticks_interval = 3  # 3개월 간격
        xticks = range(0, len(data['기간']), xticks_interval)
        plt.xticks(xticks, [data['기간'][i] for i in xticks], rotation=45)

        st.pyplot(plt)

    # 상권 활력도 분석
    elif analysis_type == "상권 활력도":
        st.subheader("상권 활력도 분석")
        plt.figure(figsize=(10, 6), dpi=300)
        plt.plot(data['기간'], data['상권활력정도'], marker='o', color='green')
        plt.title('기간에 따른 상권 활력도')
        plt.xlabel('기간')
        plt.ylabel('상권 활력도')
        plt.grid(True)

        # X축 간격 조정 (3개월 단위)
        xticks_interval = 3  # 3개월 간격
        xticks = range(0, len(data['기간']), xticks_interval)
        plt.xticks(xticks, [data['기간'][i] for i in xticks], rotation=45)

        st.pyplot(plt)

    # 3년 내 폐업 비율 분석
    elif analysis_type == "3년 내 폐업 비율":
        st.subheader("3년 내 폐업 비율 분석")
        valid_data = data[data['3년내폐업비율(%)'].notnull()]
        plt.figure(figsize=(10, 6), dpi=300)
        plt.plot(valid_data['기간'], valid_data['3년내폐업비율(%)'], marker='o', color='purple')
        plt.title('기간에 따른 3년 내 폐업 비율')
        plt.xlabel('기간')
        plt.ylabel('폐업 비율 (%)')
        plt.grid(True)

        # X축 간격 조정 (3개월 단위)
        xticks_interval = 3  # 3개월 간격
        xticks = range(0, len(valid_data['기간']), xticks_interval)
        plt.xticks(xticks, [valid_data['기간'].iloc[i] for i in xticks], rotation=45)

        st.pyplot(plt)

else:
    st.sidebar.warning("CSV 파일을 업로드해주세요.")
