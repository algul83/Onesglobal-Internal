// Streamlit Cloud 앱 keep-alive — 헤드리스 Chromium으로 실제 JS 실행.
// curl은 React shell HTML만 받기 때문에 sleep을 깨우지 못함. WebSocket
// 연결까지 가야 컨테이너에 traffic 발생하고 sleep 타이머 리셋.
// sleep 페이지면 "Yes, get this app back up!" 버튼 자동 클릭.

const { chromium } = require('playwright');

const URLS = [
  'https://onesglobal-recruit.streamlit.app',
  'https://onesglobal-accounting.streamlit.app',
  'https://connectdi-dashboard.streamlit.app',
  'https://onesglobal.streamlit.app',
];

const PAGE_TIMEOUT_MS = 90_000;   // 페이지 로드 + 컨테이너 부팅 여유
const POST_LOAD_WAIT_MS = 8_000;  // 렌더 안정화

async function pingOne(browser, url) {
  const context = await browser.newContext();
  const page = await context.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: PAGE_TIMEOUT_MS });
    await page.waitForTimeout(POST_LOAD_WAIT_MS);

    // sleep 페이지면 wake 버튼 클릭
    const wakeBtn = page.getByRole('button', { name: /get this app back up/i });
    const sleepDetected = await wakeBtn.isVisible({ timeout: 2000 }).catch(() => false);

    if (sleepDetected) {
      console.log(`💤 SLEEP — ${url} : wake 버튼 클릭`);
      await wakeBtn.click();
      // 컨테이너 부팅 대기 (Streamlit 메인 UI 등장)
      await page.waitForSelector('[data-testid="stAppViewContainer"], iframe, .stApp', {
        timeout: PAGE_TIMEOUT_MS,
      }).catch(() => {});
      await page.waitForTimeout(5000);
      console.log(`⏰ AWAKE — ${url}`);
    } else {
      console.log(`✅ AWAKE — ${url}`);
    }
    return true;
  } catch (e) {
    console.log(`❌ FAIL  — ${url} : ${e.message}`);
    return false;
  } finally {
    await context.close();
  }
}

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  let failures = 0;
  for (const url of URLS) {
    const ok = await pingOne(browser, url);
    if (!ok) failures++;
  }
  await browser.close();
  if (failures > 0) {
    console.log(`\n⚠️ ${failures}/${URLS.length} 실패`);
    process.exit(1);
  }
  console.log(`\n✅ 4/4 컨테이너 awake 보장`);
})();
