from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ----------------- কনফিগারেশন -----------------
BOT_TOKEN = "7660197234:AAHJ6TWtSXwPC3uHVIhPK_JKIdrA8qqKCtY"
CHANNEL_LINK = "https://t.me/viral_video_mal"
CHANNEL_NAME = "📢 Join Our Main Channel"

# ফাইল আইডিগুলো
MEDIA_FILES = {
    "photo": "AgACAgEAAxkBAAEkZ_tq8pR8N9uqAbaQA4l-TfC6X-O_1wACNgxrG_zzoETWlfTDxD1iZwEAAwIAA3gAAz0E",
    "video1": "BAACAgEAAxkBAAEkZ_xq8pR84M2h-bM1r_qkqTEkDGQpOAACCggAAvzzoETfoLg3y5ZmeD0E",
    "video2": "BAACAgEAAxkBAAEkZ_1q8pR8ch9jNdFjx5O7MtVlNF6vqwACCwgAAvzzoER1Y8ef1nl9Oz0E"
}
# --------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name
    args = context.args
    
    keyboard = [
        [InlineKeyboardButton(CHANNEL_NAME, url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if args and args[0] == "all_videos":
        media_group = [
            InputMediaPhoto(
                media=MEDIA_FILES["photo"], 
                caption="🔥 **Exclusive Viral Content (3 Videos/Photos)**\n\n⚠️ **সতর্কবার্তা:** ১০ মিনিটের মধ্যে ফরওয়ার্ড করে রাখুন!"
            ),
            InputMediaVideo(media=MEDIA_FILES["video1"]),
            InputMediaVideo(media=MEDIA_FILES["video2"])
        ]
        
        await update.message.reply_media_group(media=media_group)
        await update.message.reply_text(
            text="👇 নিচের লিংকে ক্লিক করে আমাদের মূল চ্যানেলে জয়েন করুন:",
            reply_markup=reply_markup
        )
    else:
        welcome_text = f"হ্যালো {user_name}! 👋\n\nভিডিওগুলো পেতে সঠিক লিংকে প্রবেশ করুন।"
        await update.message.reply_text(text=welcome_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running smoothly...")
    app.run_polling()