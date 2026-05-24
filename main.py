import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8647578768:AAEcZXhGUbjwNIUR3md8OoULC89ZknabJjw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐳 대왕고래 트레이딩에\n"
        "오신 것을 환영합니다!\n\n"
        "아래 메뉴를 선택하세요 👇\n\n"
        "/lite - 이지 2주 강의\n"
        "/premium - 추구이지스 강의\n"
        "/signal - 무료 시그널 채널\n"
        "/cafe - 네이버 카페\n"
        "/contact - 담당자 문의\n\n"
        "⚠️ 본 서비스의 모든 정보는\n"
        "교육 목적이며 투자 권유가\n"
        "아닙니다."
    )

async def lite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 BW 이지 2주 강의\n\n"
        "나스닥/골드/BTC 데이트레이딩\n"
        "기초 2주 무료 교육 채널입니다.\n\n"
        "👉 채널 입장:\n"
        "t.me/BW_EasyClass\n\n"
        "❓ 질문은 네이버 카페:\n"
        "https://cafe.naver.com/bluewhalestrading\n\n"
        "⚠️ 본 내용은 교육 목적이며\n"
        "투자 권유가 아닙니다."
    )

async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 추구이지스 교육 소통방\n\n"
        "고확률 진입/청산 심화 교육\n"
        "수강생+교육자 실시간 토론방\n\n"
        "📌 수강 문의\n"
        "담당자: @bluewhalestradingA\n\n"
        "결제 확인 후\n"
        "1회용 초대 링크 발송\n\n"
        "⚠️ 과거 실적은 미래 수익을\n"
        "보장하지 않습니다.\n"
        "모든 투자 결정은 본인 책임입니다."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 BW 무료 시그널 채널\n\n"
        "AI 기반 자동 진입/청산/추세 알람\n\n"
        "XAUUSD(골드)\n"
        "→ t.me/BW_XAUUSD_Alert\n\n"
        "BTCUSD(비트코인)\n"
        "→ t.me/BW_BTCUSD_Alter\n\n"
        "NAS100(나스닥)\n"
        "→ t.me/BW_NAS100_Alter\n\n"
        "USOUSD(원유)\n"
        "→ t.me/BW_USOUSD_Alter\n\n"
        "⚠️ 시그널은 교육 참고용이며\n"
        "투자 권유가 아닙니다."
    )

async def cafe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗂 대왕고래 트레이딩\n"
        "네이버 공식 카페\n\n"
        "강의 질문/토론/매매복기/매매자료 공유\n\n"
        "👉 https://cafe.naver.com/bluewhalestrading\n\n"
        "이지 2주 강의 관련 질문은\n"
        "카페 게시판을 이용해 주세요."
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 담당자 직접 문의\n\n"
        "텔레그램: @bluewhalestradingA\n\n"
        "운영시간\n"
        "평일 09:00 ~ 22:00\n"
        "주말/공휴일 순차 답변\n\n"
        "💬 문의 가능 내용\n"
        "- 유료 멤버십 가입\n"
        "- 결제 관련 문의\n"
        "- 채널 입장 문제\n"
        "- 기타 서비스 문의"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("lite", lite))
app.add_handler(CommandHandler("premium", premium))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("cafe", cafe))
app.add_handler(CommandHandler("contact", contact))

print("봇 시작됨")
app.run_polling()
