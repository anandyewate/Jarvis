# config.py - Indian Languages Configuration
import os

# API Keys
GEMINI_API_KEY = "AIzaSyCuJwU42RKcWToFkGRyxSQGfS5uyNzWpps"
NEWS_API_KEY = "d694d72b936e487db0303531e3f769fe"

# Speech Recognition Settings
ENERGY_THRESHOLD = 1000
LISTEN_TIMEOUT = 5
COMMAND_TIMEOUT = 10

# Indian Language Settings
DEFAULT_LANGUAGE = "en"  # English
SUPPORTED_LANGUAGES = {
    "en": {"name": "English", "gtts_lang": "en", "voice_index": 0},
    "hi": {"name": "Hindi", "gtts_lang": "hi", "voice_index": 1},
    "bn": {"name": "Bengali", "gtts_lang": "bn", "voice_index": 2},
    "ta": {"name": "Tamil", "gtts_lang": "ta", "voice_index": 3},
    "te": {"name": "Telugu", "gtts_lang": "te", "voice_index": 4},
    "mr": {"name": "Marathi", "gtts_lang": "mr", "voice_index": 5},
    "gu": {"name": "Gujarati", "gtts_lang": "gu", "voice_index": 6},
    "kn": {"name": "Kannada", "gtts_lang": "kn", "voice_index": 7},
    "ml": {"name": "Malayalam", "gtts_lang": "ml", "voice_index": 8},
    "pa": {"name": "Punjabi", "gtts_lang": "pa", "voice_index": 9},
    "or": {"name": "Odia", "gtts_lang": "or", "voice_index": 10},
    "ur": {"name": "Urdu", "gtts_lang": "ur", "voice_index": 11}
}

# Language-specific responses
LANGUAGE_RESPONSES = {
    "en": {
        "welcome": "Jarvis is ready. Say Jarvis to begin.",
        "listening": "Yes, what can I do for you?",
        "timeout": "I didn't hear anything.",
        "unclear": "Please speak more clearly.",
        "goodbye": "Goodbye!",
        "ai_unavailable": "AI features are currently unavailable.",
        "news_fetching": "Getting the latest news",
        "news_finished": "That's the latest news",
        "no_news": "No news articles found",
        "news_unavailable": "News service unavailable",
        "song_not_found": "Song not found",
        "playing": "Playing",
        "opening": "Opening",
        "hello": "Hello! How can I help you?",
        "language_changed": "Language changed to",
        "current_language": "Current language is",
        "available_languages": "Available languages: English, Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Odia, Urdu"
    },
    "hi": {
        "welcome": "जार्विस तैयार है। जार्विस कहकर शुरू करें।",
        "listening": "हाँ, मैं आपकी क्या मदद कर सकता हूँ?",
        "timeout": "मैंने कुछ नहीं सुना।",
        "unclear": "कृपया स्पष्ट बोलें।",
        "goodbye": "अलविदा!",
        "ai_unavailable": "AI सुविधाएं वर्तमान में उपलब्ध नहीं हैं।",
        "news_fetching": "ताज़ा खबरें प्राप्त कर रहा हूँ",
        "news_finished": "यह ताज़ा खबरें थीं",
        "no_news": "कोई खबरें नहीं मिलीं",
        "news_unavailable": "खबर सेवा उपलब्ध नहीं है",
        "song_not_found": "गाना नहीं मिला",
        "playing": "चल रहा है",
        "opening": "खोल रहा हूँ",
        "hello": "नमस्ते! मैं आपकी क्या मदद कर सकता हूँ?",
        "language_changed": "भाषा बदल गई है",
        "current_language": "वर्तमान भाषा है",
        "available_languages": "उपलब्ध भाषाएँ: अंग्रेजी, हिंदी, तमिल, तेलुगु, बंगाली, मराठी, गुजराती, कन्नड़, मलयालम, पंजाबी, ओडिया, उर्दू"
    },
    "ta": {
        "welcome": "ஜார்விஸ் தயார். ஜார்விஸ் என்று சொல்லி தொடங்கவும்.",
        "listening": "ஆமாம், நான் உங்களுக்கு என்ன உதவி செய்ய முடியும்?",
        "timeout": "நான் எதுவும் கேட்கவில்லை.",
        "unclear": "தயவு செய்து தெளிவாக பேசுங்கள்.",
        "goodbye": "பிரியாவிடை!",
        "ai_unavailable": "AI அம்சங்கள் தற்போது கிடைக்கவில்லை.",
        "news_fetching": "சமீபத்திய செய்திகளைப் பெறுகிறேன்",
        "news_finished": "அவை சமீபத்திய செய்திகள்",
        "no_news": "செய்திகள் எதுவும் கிடைக்கவில்லை",
        "news_unavailable": "செய்தி சேவை கிடைக்கவில்லை",
        "song_not_found": "பாடல் கிடைக்கவில்லை",
        "playing": "இயங்குகிறது",
        "opening": "திறக்கிறது",
        "hello": "வணக்கம்! நான் உங்களுக்கு என்ன உதவி செய்ய முடியும்?",
        "language_changed": "மொழி மாற்றப்பட்டது",
        "current_language": "தற்போதைய மொழி",
        "available_languages": "கிடைக்கும் மொழிகள்: ஆங்கிலம், இந்தி, தமிழ், தெலுங்கு, வங்காளம், மராத்தி, குஜராத்தி, கன்னடம், மலையாளம், பஞ்சாபி, ஓடியா, உருது"
    },
    "te": {
        "welcome": "జార్విస్ సిద్ధంగా ఉంది. జార్విస్ అని చెప్పి ప్రారంభించండి.",
        "listening": "అవును, నేను మీకు ఏమి సహాయం చేయగలను?",
        "timeout": "నేను ఏమీ వినలేదు.",
        "unclear": "దయచేసి స్పష్టంగా మాట్లాడండి.",
        "goodbye": "వీడ్కోలు!",
        "ai_unavailable": "AI సౌలభ్యాలు ప్రస్తుతం అందుబాటులో లేవు.",
        "news_fetching": "తాజా వార్తలను పొందుతున్నాను",
        "news_finished": "అవి తాజా వార్తలు",
        "no_news": "వార్తలు ఏవీ లభించలేదు",
        "news_unavailable": "వార్తల సేవ అందుబాటులో లేదు",
        "song_not_found": "పాట లభించలేదు",
        "playing": "ప్లే అవుతుంది",
        "opening": "తెరుస్తుంది",
        "hello": "నమస్కారం! నేను మీకు ఏమి సహాయం చేయగలను?",
        "language_changed": "భాష మార్చబడింది",
        "current_language": "ప్రస్తుత భాష",
        "available_languages": "అందుబాటులో ఉన్న భాషలు: ఆంగ్లం, హిందీ, తమిళం, తెలుగు, బెంగాలీ, మరాఠీ, గుజరాతీ, కన్నడ, మలయాళం, పంజాబీ, ఒడియా, ఉర్దూ"
    },
    "bn": {
        "welcome": "জারভিস প্রস্তুত। জারভিস বলে শুরু করুন।",
        "listening": "হ্যাঁ, আমি আপনাকে কীভাবে সাহায্য করতে পারি?",
        "timeout": "আমি কিছু শুনিনি।",
        "unclear": "দয়া করে স্পষ্টভাবে বলুন।",
        "goodbye": "বিদায়!",
        "ai_unavailable": "AI বৈশিষ্ট্য বর্তমানে unavailable.",
        "news_fetching": "সর্বশেষ খবর পাওয়া হচ্ছে",
        "news_finished": "এগুলো ছিল সর্বশেষ খবর",
        "no_news": "কোনো খবর পাওয়া যায়নি",
        "news_unavailable": "খবর পরিষেবা unavailable",
        "song_not_found": "গান পাওয়া যায়নি",
        "playing": "চলছে",
        "opening": "খোলা হচ্ছে",
        "hello": "নমস্কার! আমি আপনাকে কীভাবে সাহায্য করতে পারি?",
        "language_changed": "ভাষা পরিবর্তন করা হয়েছে",
        "current_language": "বর্তমান ভাষা",
        "available_languages": "উপলব্ধ ভাষা: ইংরেজি, হিন্দি, তামিল, তেলেগু, বাংলা, মারাঠি, গুজরাটি, কন্নড়, মালয়ালম, পাঞ্জাবি, ওড়িয়া, উর্দু"
    }
}

# Language detection keywords
LANGUAGE_KEYWORDS = {
    "english": "en", "angrezi": "en", "इंग्लिश": "en", "ஆங்கிலம்": "en", "ఆంగ్లం": "en", "ইংরেজি": "en",
    "hindi": "hi", "हिंदी": "hi", "ஹிந்தி": "hi", "హిందీ": "hi", "হিন্দি": "hi",
    "tamil": "ta", "तमिल": "ta", "தமிழ்": "ta", "తమిళం": "ta", "তামিল": "ta",
    "telugu": "te", "तेलुगु": "te", "தெலுங்கு": "te", "తెలుగు": "te", "তেলেগু": "te",
    "bengali": "bn", "बंगाली": "bn", "வங்காளம்": "bn", "బెంగాలీ": "bn", "বাংলা": "bn",
    "marathi": "mr", "मराठी": "mr", "மராத்தி": "mr", "మరాఠీ": "mr", "মারাঠি": "mr",
    "gujarati": "gu", "गुजराती": "gu", "குஜராத்தி": "gu", "గుజరాతీ": "gu", "গুজরাটি": "gu",
    "kannada": "kn", "कन्नड़": "kn", "கன்னடம்": "kn", "కన్నడ": "kn", "কন্নড়": "kn",
    "malayalam": "ml", "मलयालम": "ml", "மலையாளம்": "ml", "మలయాళం": "ml", "মলয়ালম": "ml",
    "punjabi": "pa", "पंजाबी": "pa", "பஞ்சாபி": "pa", "పంజాబీ": "pa", "পাঞ্জাবি": "pa"
}