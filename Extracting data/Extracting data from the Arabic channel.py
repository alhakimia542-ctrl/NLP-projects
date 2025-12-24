import tweepy
import pandas as pd

# =========================
# ضع Bearer Token هنا
# =========================
BEARER_TOKEN = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"

# إنشاء عميل Twitter API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True
)

# اسم الحساب (العربية عاجل)
username = "AlArabiya_Brk"

# الحصول على ID الحساب
user = client.get_user(username=username)
user_id = user.data.id

# =========================
# جلب التغريدات
# =========================
tweets = client.get_users_tweets(
    id=user_id,
    max_results=100,                # أقصى عدد في الطلب الواحد (حتى 100)
    tweet_fields=["created_at", "lang"],
    exclude=["retweets", "replies"] # بدون ريتويت وردود
)

data = []

if tweets.data:
    for tweet in tweets.data:
        if tweet.lang == "ar":  # نأخذ العربي فقط
            data.append({
                "text": tweet.text,
                "created_at": tweet.created_at
            })

# تحويل إلى DataFrame
df = pd.DataFrame(data)

# حفظ الملف
df.to_csv("alarabiya_tweets.csv", index=False, encoding="utf-8-sig")

print("✅ تم تحميل وحفظ", len(df), "تغريدة عربية")
print(df.head())
