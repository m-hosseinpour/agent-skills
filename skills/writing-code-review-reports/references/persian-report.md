# Persian Review Reports

Open when preparing Persian output or selecting consistent labels. `SKILL.md` owns reporting mode,
severity, evidence, and readiness rules. This reference provides language choices and a handoff template,
not a reason to change engineering judgments or force a new structure on a faithful translation.

## Labels

Translate headings and classifications; preserve identifiers, paths, commands, and relevant log text.
Keep the sentences natural and explain the concrete point before technical detail.

| English | Persian | Use |
| --- | --- | --- |
| Ready | آماده | Supported readiness for the stated scope |
| Not ready | آماده نیست | Confirmed issue prevents merge/delivery |
| Cannot determine | قابل‌تعیین نیست | Material uncertainty prevents a readiness conclusion |
| Blocking | مانع ادغام | Must resolve before merge |
| Important | مهم | Material issue worth fixing |
| Nit / Minor | کم‌اهمیت | Ordinary low-impact polish, included by default under نکات کم‌اهمیت (اختیاری); not a merge condition |
| Nit — scope mismatch | کم‌اهمیت — خارج از دامنه | Confirmed low-risk extra |
| Suggestion | پیشنهاد اختیاری | Optional advice, not a defect |
| Met | محقق‌شده | Reachable behavior matches the requirement |
| Partial | ناقص | Incorrect or incomplete implementation |
| Missing | تحقق‌نیافته | Confirmed absence or unreachable behavior |
| Ambiguous | مبهم | Unresolved multiple readings |
| Unverified | راستی‌آزمایی‌نشده | Required evidence unavailable |
| Respected | رعایت‌شده | Non-goal/scope constraint stays out |
| Violated | نقض‌شده | Non-goal/scope constraint violated |
| Reportedly resolved | رفع‌شده طبق گزارش | Resolution claimed at a stated revision; qualify evidence |

Undefined P1/P2 labels remain P1/P2 with an explanation that their meaning was not supplied; do not
invent Persian severity equivalents. When faithfully translating a report, preserve its original
classification, including optional suggestions and an attributed verdict. State material contradictions
separately, without rewriting the source as if the reviewer had reached a different conclusion.

## Adaptable Handoff Template

Use only sections that earn their space. Omit Requirements without supplied requirements, Out of
scope without confirmed extras, Minor points without relevant supplied minor findings/suggestions,
and Confirmed behavior without useful supporting evidence. Keep
scope, material limits, findings, and verification even in a short report. A translation may preserve
the source's structure instead. Do not fill placeholders with invented facts or claim checks ran
because a test appears in the source.

```markdown
# [موضوع کوتاه: چه تغییری بازبینی شد]

**حکم:** [آماده / آماده نیست / قابل‌تعیین نیست] — [دلیل اصلی؛ محدودیت دامنه و ابهام مهم در صورت وجود]

**دامنه:** [نسخهٔ مبنا و نسخهٔ بررسی‌شده، یا دامنهٔ تغییرات محلی؛ موارد مهم بررسی‌نشده]

## الزامات

| الزام یا محدودیت دامنه | وضعیت | شواهد و محدودیت‌ها |
| --- | --- | --- |
| [معیار] | [وضعیت از جدول بالا] | [مسیر:خط یا نماد، نسخه، شاهد یا اطلاعات در دسترس‌نبوده] |

## یافته‌ها

### [مانع ادغام / مهم] — [عنوان کوتاه]

- **مشکل:** [محل دقیق و شرایطی که رفتار نادرست رخ می‌دهد]
- **چرا مهم است:** [پیامد یا هزینهٔ مشخص]
- **اقدام:** [اصلاح/بررسی بعدیِ پشتیبانی‌شده؛ اگر برنامهٔ اصلاح ارائه نشده، همین کمبود را روشن کنید]

### موارد خارج از دامنه

#### [مانع ادغام / مهم / کم‌اهمیت — خارج از دامنه] — [عنوان کوتاه]

- **مشکل:** [رفتار اضافه، محل و نسخهٔ آن، و دلیل خارج‌بودن از توافق]
- **چرا مهم است:** [ریسک/هزینهٔ مشخص، یا اینکه مورد کم‌خطر است]
- **اقدام:** [حذف، جداسازی، یا تأیید صریح دامنه]

### نکات کم‌اهمیت (اختیاری)

- **[کم‌اهمیت / پیشنهاد] — [عنوان کوتاه]:** [محل دقیق، ایراد جزئی یا فایدهٔ مشخص، و اقدام اختیاریِ ارائه‌شده در نتایج بازبینی]

## شواهد بررسی و محدودیت‌ها

- [دستور/سناریو، نتیجه، نسخه و محیط مرتبط؛ مشخص کنید بازبین اجرا کرده یا نتیجه از منبع دیگری نقل شده است]
- [مسیر یا رفتار بررسی‌نشده، تعارض حل‌نشده، و اطلاعات لازم برای تعیین تکلیف]

## رفتار تأییدشده

- [رفتار مهمی که شواهد موجود درستی آن را پشتیبانی می‌کنند؛ محدودیت بررسی ایستا یا اجرا را نگه دارید]
```

Include relevant supplied ordinary nits and useful suggestions by default under **نکات کم‌اهمیت
(اختیاری)**; the parentheses make it clear that addressing this category is optional. Keep minor
defects distinguishable from suggestions, and do not promote them to مهم merely to fit the template.
Keep confirmed extras under **موارد خارج از دامنه**, even when low-risk; a required gap or hard
scope-constraint violation must not be hidden as optional polish. Faithful translations preserve the
source's requested structure and classifications instead of forcing this handoff template.

If only optional points remain, say **در دامنهٔ بررسی‌شده، مورد مانع ادغام یا مهم گزارش نشده است؛
نکات کم‌اهمیت (اختیاری) در ادامه آمده‌اند**. For an empty findings list with no suggestions, say
**در دامنهٔ بررسی‌شده، ایراد قابل‌اقدامی گزارش نشده است**. Neither statement means every path was
verified or the whole change is ready; optional points alone do not prevent a supported آماده verdict.

## Short Example: No Findings, Incomplete Coverage

```markdown
**موضوع:** بازبینی بخش API در نسخهٔ H1

**حکم:** آمادگی کل تغییر قابل‌تعیین نیست؛ در بخش API ایراد قابل‌اقدامی گزارش نشده، اما مسیر احراز هویت و عرضهٔ تغییر بررسی نشده‌اند.

**دامنه:** بخش API، از `aaa` تا `bbb`؛ مسیر احراز هویت و عرضهٔ تغییر بررسی نشده‌اند.

**شواهد:** بازبین موفقیت `npm test -- api` را در H1 گزارش کرده است. برای تعیین آمادگی کل تغییر، شواهد بازبینی مسیرهای بررسی‌نشده لازم است؛ در مرحلهٔ گزارش‌نویسی آزمونی اجرا نشده است.
```

The example uses supplied results only. Do not add a requirement table, praise, or a stronger verdict
merely because the template offers a heading for it.
