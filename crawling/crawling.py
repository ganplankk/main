from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time

# 🛠️ 크롬 드라이버 설정 (같은 폴더에 있을 경우)
service = Service('http://robot.piolink.com/rc/1021/other/report.html#totals?all')
driver = webdriver.Chrome(service=service)

# 🔗 대상 URL 요청
url = "http://robot.piolink.com/rc/1021/other/report.html#totals?all"  # ← 여기에 실제 URL 입력
driver.get(url)

# ⏳ 렌더링 기다리기
time.sleep(3)  # 페이지와 JS 렌더링 시간 (필요시 늘릴 것)

# 🧲 테이블 행들 가져오기
rows = driver.find_elements(By.CSS_SELECTOR, "#test-details tbody tr")

# 📦 데이터 수집
data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 5:
        name = cols[0].text.strip()
        doc = cols[1].text.strip()
        status = cols[4].text.strip()
        data.append([name, doc, status])

# 📊 엑셀 저장
wb = Workbook()
ws = wb.active
ws.title = "테스트 결과"
ws.append(["Name", "Documentation", "Status"])

for item in data:
    ws.append(item)

wb.save("test_results.xlsx")
print("🎉 엑셀 저장 완료! 결과: test_results.xlsx")

# ✅ 브라우저 닫기
driver.quit()
