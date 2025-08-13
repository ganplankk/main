# Build a full single-file Portfolio HTML from the uploaded PDF's content.
# - Creates a clean, responsive portfolio with sections for Profile, Education, Certifications, Core Skills, Experience, Project Timeline, and Documents.
# - Adds a profile photo slot (profile.jpg).
# - Links/embeds both PDFs in docs/.
#
# Inputs (uploaded by user):
#   /mnt/data/DevOps_지원자_방효성.pdf
#   /mnt/data/docs/NHN_SSL_PoC.pdf  (from previous step)
#
# Output:
#   /mnt/data/portfolio_full_from_pdf.html
#   /mnt/data/docs/DevOps_Resume.pdf
#
import os, shutil, textwrap

# Ensure docs directory
os.makedirs("/data", exist_ok=True)

# Copy DevOps resume PDF to docs URL-safe name
src_resume = "/data/GSLB솔루션교육자료.pdf"
dst_resume = "/data/HTTP2.0교육자료.pdf"
if os.path.exists(src_resume):
    shutil.copyfile(src_resume, dst_resume)

# Make sure the earlier PoC PDF exists (it should from previous step)
poC_pdf = "/datadocs/NHN_SSL_PoC.pdf"

html = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>방효성 | DevOps & ADC Engineer Portfolio</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand:#2962ff;
      --ink:#222;
      --muted:#6b7280;
      --bg:#f8fafc;
      --card:#ffffff;
    }
    *{box-sizing:border-box}
    body{margin:0;background:var(--bg);font-family:Poppins,system-ui,-apple-system,Segoe UI,Roboto,Apple Color Emoji,Noto Color Emoji,sans-serif;color:var(--ink);}
    header{position:sticky;top:0;z-index:10;background:var(--card);border-bottom:1px solid #eef2f7}
    .wrap{max-width:980px;margin:0 auto;padding:20px}
    .brand{display:flex;align-items:center;gap:14px}
    .brand h1{font-size:20px;margin:0;color:var(--brand);font-weight:700;}
    nav{display:flex;gap:16px;flex-wrap:wrap}
    nav a{color:var(--ink);text-decoration:none;font-weight:500;padding:8px 10px;border-radius:8px}
    nav a:hover{background:#eef2ff}
    main{max-width:980px;margin:28px auto;padding:0 20px 60px}
    section{background:var(--card);border:1px solid #eef2f7;border-radius:16px;padding:22px;margin-bottom:20px;box-shadow:0 2px 8px rgba(0,0,0,.03)}
    h2{margin:0 0 14px;font-size:20px;color:var(--brand)}
    .profile{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
    .avatar{width:120px;height:120px;border-radius:50%;object-fit:cover;border:3px solid var(--brand);background:#e5e7eb}
    .meta{color:var(--muted);font-size:14px}
    ul{margin:8px 0 0 18px}
    li{margin:6px 0}
    .grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
    .badge{display:inline-block;border:1px solid var(--brand);color:var(--brand);padding:4px 8px;border-radius:999px;font-size:12px;margin:2px 6px 0 0}
    .row{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}
    .role{font-weight:600}
    .period{color:var(--muted);font-size:13px}
    .btn{display:inline-block;padding:10px 14px;border-radius:10px;border:1px solid var(--brand);color:var(--brand);text-decoration:none;font-weight:600;margin-right:8px}
    .btn:hover{background:var(--brand);color:#fff}
    .pdf{width:100%;height:640px;border:1px solid #e5e7eb;border-radius:12px}
    details{border:1px dashed #e5e7eb;border-radius:12px;padding:12px;margin-top:10px;background:#fafbff}
    details>summary{cursor:pointer;font-weight:600;color:#374151}
    .tag{display:inline-block;padding:2px 8px;font-size:12px;background:#eef2ff;color:#334155;border-radius:999px;margin:2px 6px 0 0}
    footer{max-width:980px;margin:30px auto 60px;padding:0 20px;color:var(--muted);font-size:13px}
    @media (max-width:780px){.grid{grid-template-columns:1fr} .pdf{height:520px}}
  </style>
</head>
<body>
  <header>
    <div class="wrap row">
      <div class="brand"><h1>방효성 포트폴리오</h1></div>
      <nav>
        <a href="#profile">Profile</a>
        <a href="#education">Education</a>
        <a href="#certs">Certifications</a>
        <a href="#skills">Core Skills</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Project Timeline</a>
        <a href="#docs">Documents</a>
      </nav>
    </div>
  </header>

  <main>
    <section id="profile">
      <div class="profile">
        <img src="profile.jpg" alt="Resume Photo" class="avatar">
        <div>
          <h2>Profile</h2>
          <div class="role">DevOps 지향 네트워크/ADC 엔지니어</div>
          <div class="meta">문제 해결을 끝까지 밀어붙이는 실행력 · 컨테이너/리눅스/네트워크 전반 이해 · 자동화 스크립팅 능력</div>
          <div style="margin-top:8px;">
            <span class="badge">ADC/GSLB</span>
            <span class="badge">Kubernetes</span>
            <span class="badge">CI/CD</span>
            <span class="badge">Linux</span>
            <span class="badge">Troubleshooting</span>
          </div>
        </div>
      </div>
    </section>

    <section id="education">
      <h2>Education</h2>
      <div class="grid">
        <div>
          <div class="row">
            <div><strong>컴퓨터공학과 (학점은행제, 4년제)</strong></div>
            <div class="period">2019.04 ~ 2020.08</div>
          </div>
          <div class="meta">졸업</div>
        </div>
        <div>
          <div class="row">
            <div><strong>단국공업 고등학교</strong></div>
            <div class="period">2006.03 ~ 2009.02</div>
          </div>
          <div class="meta">졸업</div>
        </div>
      </div>
    </section>

    <section id="certs">
      <h2>Certifications & Awards</h2>
      <ul>
        <li>2024.07 · 파이오링크 사내포상 <strong>베스트 엔지니어상</strong></li>
        <li>2023.11 · <strong>CKA (Certified Kubernetes Administrator)</strong></li>
        <li>2021.04 · F5 Networks <strong>201, 101</strong> Certificate</li>
        <li>2020.12 · <strong>정보보안산업기사</strong></li>
        <li>2020.05 · <strong>리눅스마스터 1급</strong></li>
        <li>2018.11 · <strong>정보처리산업기사</strong></li>
      </ul>
    </section>

    <section id="skills">
      <h2>Core Skills</h2>
      <ul>
        <li>ADC/GSLB 구성 설계 및 구축</li>
        <li>Kubernetes 아키텍처 · 리눅스 운영체제 전반 이해</li>
        <li>반복 작업 자동화를 위한 스크립트 작성</li>
        <li>트러블슈팅 및 PoC/BMT 수행</li>
      </ul>
    </section>

    <section id="experience">
      <h2>Experience</h2>
      <div class="item">
        <div class="row">
          <div><strong>파이오링크</strong> · <span class="role">ADC 담당 기술지원</span></div>
        </div>
        <ul>
          <li>자사 ADC 제품 판매 촉진을 위한 신기술 조사 및 기능 개선 활동</li>
          <li>총판·파트너 엔지니어 기술 교육 자료 제작 및 교육 진행</li>
          <li>장애 상황 트러블슈팅 지원, BMT/PoC 단계 기술 지원</li>
          <li>GSLB 기능 분석·개선 주도 → F5 GSLB Winback 및 레퍼런스 확대</li>
        </ul>
      </div>
      <div class="item">
        <div class="row">
          <div><strong>아이티언</strong> · <span class="role">F5 보안 담당 기술지원</span></div>
        </div>
        <ul>
          <li>F5 L7 스위치, WAF, SSL‑VPN 구축 및 기술 지원</li>
          <li>장비 유지보수, BMT/PoC 지원, 고객사 교육</li>
        </ul>
      </div>
    </section>

    <section id="projects">
      <h2>Project Timeline (Selected)</h2>
      <details open>
        <summary>2024</summary>
        <ul>
          <li>상반기/하반기 <strong>GSLB 특화 교육</strong> (교육활동)</li>
          <li>신규 총판 파트너 ADC 엔지니어 교육 (교육활동)</li>
          <li>KT 혜화지사 HIoT WEB L4 노후화 장비 교체 (구축지원)</li>
          <li>가상화 ADC 특화 교육 (교육활동)</li>
          <li>LG CNS VDI 프록시 장비 PoC (PoC)</li>
          <li>KT L4 스위치 통합 구매사업 (BMT)</li>
          <li>주택도시보증공사 노후화 장비 대개체 (구축지원)</li>
          <li>정보사령부 TTA 성능 측정 검증 (BMT 지원)</li>
        </ul>
      </details>
      <details>
        <summary>2023</summary>
        <ul>
          <li>한국철도공사 예약발매 L4 스위치 구축지원</li>
          <li>NHN클라우드 코닉 TMS 연동 PoC (기술지원)</li>
          <li>모두투어 L4 도입사업 (구축지원)</li>
          <li><strong>NHN클라우드 SSL 암복호화 소프트웨어 성능 BMT</strong> (BMT)</li>
          <li>상반기 GSLB 특화 교육 (교육활동)</li>
        </ul>
      </details>
      <details>
        <summary>2022 ~ 2019</summary>
        <ul>
          <li>하나은행 대면녹취 GSLB L4 스위치 BMT (2023.02)</li>
          <li>카카오페이 VDI L4/L7 납품사 선정 사업 (2022.09, PoC)</li>
          <li>한국전력공사 VDI 프록시 PoC (2022.01)</li>
          <li>대전교육정보원 스쿨넷 4차사업 (2021.11, 구축지원)</li>
          <li>신한생명·오렌지라이프 IT통합 WAF 구축 (2021.06)</li>
          <li>LGU+ 신형셋탑 품질로그수집 L4 구축 (2021.05)</li>
          <li>하나은행 SSO OneSign L4 스위치 구축 (2021.03)</li>
          <li>우리금융그룹 정보보안통합관제 Aggregation SW 구축 (2021.02)</li>
          <li>KEB 하나은행 TBML 시스템 L4 스위치 구축 (2021.02)</li>
          <li>서초구청 웹 방화벽 구축 (2020.09)</li>
          <li>을지대 LMS 고도화 L4 구축 (2020.08)</li>
          <li>남동발전 여수본부 SSL‑VPN 구축 (2020.02)</li>
          <li>두성종이 SSL‑VPN 구축 (2020.01)</li>
          <li>대한항공 SSL‑VPN SAML 연동 (2019.12)</li>
          <li>제주항공 WAF 망 이전 (2019.11)</li>
          <li>ISE‑Commerce SSL‑VPN Google OTP 연동 (2019.10)</li>
          <li>제우스 SSL‑VPN 중국 PoC (2019.10)</li>
          <li>현대차그룹 DaaS(VDI) BMT (2019.09)</li>
          <li>선거관리위원회 SSL‑VPN 구축 (2019.09)</li>
          <li>대한항공 SSL‑VPN(상암, 청도) 구축 (2019.03)</li>
        </ul>
      </details>
    </section>

    <section id="docs">
      <h2>Documents</h2>
      <p class="meta">포트폴리오와 직접 연결된 PDF 자료입니다. 새 탭으로 열거나 페이지 내에서 바로 볼 수 있습니다.</p>
      <div style="margin:10px 0 14px">
        <a class="btn" href="docs/DevOps_Resume.pdf" target="_blank" rel="noopener">이력서 PDF 열기</a>
        <a class="btn" href="docs/DevOps_Resume.pdf" download>이력서 다운로드</a>
      </div>
      <iframe class="pdf" src="docs/DevOps_Resume.pdf"></iframe>

      <div style="height:20px"></div>

      <div style="margin:10px 0 14px">
        <a class="btn" href="docs/NHN_SSL_PoC.pdf" target="_blank" rel="noopener">NHN SSL PoC PDF 열기</a>
        <a class="btn" href="docs/NHN_SSL_PoC.pdf" download>NHN SSL PoC 다운로드</a>
      </div>
      <iframe class="pdf" src="docs/NHN_SSL_PoC.pdf"></iframe>
    </section>

    <section id="motivation">
      <h2>지원동기</h2>
      <p>인프라 기반 지식을 바탕으로 DevOps 엔지니어로의 도약을 준비하고 있습니다. 컨테이너 기술과 CI/CD 자동화, 모니터링·로깅 시스템까지 폭넓게 다루는 역량을 갖추기 위해 꾸준히 학습하고 있으며, 문제를 집요하게 파고드는 끈기와 협업을 통한 해결력으로 클라우드 시대의 인프라 자동화에 기여하겠습니다.</p>
    </section>
  </main>

  <footer>
    ※ 프로필 사진은 이 파일과 같은 위치에 <strong>profile.jpg</strong> 이름으로 업로드하면 표시됩니다.
  </footer>
</body>
</html>
"""

out_path = "/mnt/data/portfolio_full_from_pdf.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

# (out_path, dst_resume, poC_pdf if os.path.exists(poC_pdf) else None)
