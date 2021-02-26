class TranslateDatabase:
    LD_INDEX_FULL_NAME = 0
    LD_INDEX_WORD_ORIGINAL = 1
    LD_INDEX_WORD_TRANSLATION = 2
    LD_INDEX_IS_TYPICAL = 3
    LANGUAGE_DICT = {'af': ['afrikaans', 'oorspronklike', 'vertaling', True], \
                     'am': ['amharic', 'Original', 'Translation', False], \
                     'ar': ['arabic', 'Original', 'Translation', False], \
                     'az': ['azerbaijani', 'Original', 'Translation', False], \
                     'be': ['belarusian', 'Original', 'Translation', False], \
                     'bg': ['bulgarian', 'оригинал', 'превод', False], \
                     'bn': ['bengali', 'Original', 'Translation', False], \
                     'bs': ['bosnian', 'Original', 'Translation', False], \
                     'ca': ['catalan', 'Original', 'Translation', False], \
                     'ceb': ['cebuano', 'Orihinal', 'Paghubad', False], \
                     'co': ['corsican', 'Originale', 'Traduzione', False], \
                     'cs': ['czech', 'Original', 'Translation', False], \
                     'cy': ['welsh', 'Gwreiddiol', 'Cyfieithu', False], \
                     'da': ['danish', 'Original', 'Translation', False], \
                     'de': ['german', 'Original', 'Translation', True], \
                     'el': ['greeklanguage', 'Original', 'Translation', False], \
                     'en': ['english', 'Original', 'Translation', True], \
                     'eo': ['esperanto', 'Originala', 'Tradukado', False], \
                     'es': ['spanish', 'Original', 'Translation', True], \
                     'et': ['estonian', 'Original', 'Translation', False], \
                     'eu': ['basque', 'Original', 'Itzulpena', False], \
                     'fa': ['persian', 'Original', 'Translation', False], \
                     'fi': ['finnish', 'Original', 'Translation', False], \
                     'fr': ['french', 'Original', 'Traduction', True], \
                     'fy': ['frisian', 'Oarspronklik', 'Oersetting', False], \
                     'ga': ['irish', 'Original', 'Translation', False], \
                     'gd': ['scottish gaelic', 'Original', 'Eadar-theangachadh', False], \
                     'gl': ['galician', 'Original', 'Translation', False], \
                     'gu': ['gujarati', 'Original', 'Translation', False], \
                     'ha': ['hausa', 'Asali', 'Translation', False], \
                     'haw': ['hawaiian', 'Original', 'Translation', False], \
                     'he': ['hebrew', 'Original', 'Translation', False], \
                     'hi': ['hindi', 'Original', 'Translation', False], \
                     'hmn': ['monk', 'Thawj', 'Neeg txhais lus', False], \
                     'hr': ['croatian', 'original', 'prijevod', False], \
                     'ht': ['haitian', 'Original', 'Tradiksyon', False], \
                     'hu': ['hungarian', 'Original', 'Translation', False], \
                     'hy': ['armenian', 'Original', 'Translation', False], \
                     'id': ['indonesian', 'Asli', 'Terjemahan', True], \
                     'ig': ['igbo', 'Original', 'Translation', False], \
                     'is': ['icelandic', 'Original', 'Translation', False], \
                     'it': ['italian', 'originale', 'traduzione', False], \
                     'ja': ['japanese', '原文', '翻訳文', True], \
                     'jv': ['javanese', 'Original', 'Translation', False], \
                     'ka': ['georgian', 'Original', 'Translation', False], \
                     'kk': ['kazakh', 'Original', 'Translation', False], \
                     'km': ['khmer', 'Original', 'Translation', False], \
                     'kn': ['kannada', 'Original', 'Translation', False], \
                     'ko': ['korean', 'Original', 'Translation', True], \
                     'ku': ['kurdish', 'Original', 'Werger', False], \
                     'ky': ['kirghiz', 'Original', 'котормо', False], \
                     'la': ['latin', 'original', 'Latin Vulgate', False], \
                     'lb': ['luxembourgish', 'Original', 'Iwwersetzung', False], \
                     'lo': ['laotian', 'Original', 'Translation', False], \
                     'lt': ['lithuanian', 'Originalas', 'Vertimas', False], \
                     'lv': ['latvian', 'Original', 'Translation', False], \
                     'mg': ['malagasy', 'Original', 'Translation', False], \
                     'mi': ['maori', 'Tuhinga', 'Translation', False], \
                     'mk': ['macedonian', 'Оригинал', 'Превод', False], \
                     'ml': ['malayalam', 'Original', 'Translation', False], \
                     'mn': ['mongolian', 'Эх', 'Орчуулга', False], \
                     'mr': ['marathi', 'Original', 'Translation', False], \
                     'ms': ['malay', 'Asal', 'Terjemahan', False], \
                     'mt': ['maltese', 'Original', 'Translation', False], \
                     'my': ['myanmar', 'Original', 'Translation', False], \
                     'ne': ['nepali', 'Original', 'Translation', False], \
                     'nl': ['dutch', 'origineel', 'vertaling', False], \
                     'no': ['norwegian', 'original', 'oversettelse', False], \
                     'ny': ['chewa', 'Zachiyambi', 'Kutembenuzidwa', False], \
                     'pa': ['punjabi', 'Original', 'Translation', False], \
                     'pl': ['polish', 'Original', 'Translation', False], \
                     'ps': ['pushto', 'Original', 'Translation', False], \
                     'pt': ['portuguese', 'Original', 'Translation', False], \
                     'ro': ['romanian', 'original', 'traducere', False], \
                     'ru': ['russian', 'оригинал', 'перевод', True], \
                     'sd': ['sindhi', 'Original', 'Translation', False], \
                     'si': ['sinhala', 'Original', 'Translation', False], \
                     'sk': ['slovak', 'Original', 'Translation', False], \
                     'sl': ['slovenian', 'Original', 'Prevajanje', False], \
                     'sm': ['samoan', 'Original', 'Translation', False], \
                     'sn': ['shona', 'Pakutanga', 'Shanduro', False], \
                     'so': ['somali', 'Asalka', 'Turjubaan', False], \
                     'sq': ['albanian', 'Original', 'Translation', False], \
                     'sr': ['serbian', 'Оригинал', 'Превод', False], \
                     'su': ['sundanese', 'asli', 'tarjamahan', False], \
                     'sv': ['swedish', 'Original', 'Translation', False], \
                     'sw': ['swahili', 'Yaliyomo', 'Tafsiri', False], \
                     'sx': ['sotho', 'Original', 'Translation', False], \
                     'ta': ['tamil', 'Original', 'Translation', False], \
                     'te': ['telugu', 'Original', 'Translation', False], \
                     'tg': ['tajiki', 'Original', 'Translation', False], \
                     'th': ['thai', 'Original', 'Translation', False], \
                     'tl': ['tagalog', 'Orihinal', 'Pagsasalin', False], \
                     'tr': ['turkish', 'Original', 'Translation', False], \
                     'uk': ['ukrainian', 'Original', 'Translation', False], \
                     'ur': ['urdu', 'Original', 'Translation', False], \
                     'uz': ['uzbek', 'Original', 'Tarjima', False], \
                     'vi': ['vietnamese', 'Original', 'Translation', False], \
                     'xh': ['xosa', 'Okwangempela', 'Ukuguqulelwa', False], \
                     'yi': ['yiddish', 'Original', 'Translation', False], \
                     'yo': ['yoruba', 'Original', 'Translation', False], \
                     'zh-CN': ['chinese', 'Original', 'Translation', True], \
                     'zu': ['zulu', 'Okokuqala', 'Ukuhumusha', False]}

    LANGUAGE_STAMP_DICT = {'🇯🇵': 'ja', \
                           '🇺🇸': 'en', \
                           '🇩🇪': 'de', \
                           '🇷🇺': 'ru', \
                           '🇪🇸': 'es', \
                           '🇫🇷': 'fr', \
                           '🇨🇳': 'zh-CN', \
                           '🇮🇩': 'id', \
                           '🇬🇧': 'en', \
                           '🇰🇷': 'ko', \
                           '🇬🇭': 'en', \
                           '🇻🇪': 'es'}

    def __init__(self):
        pass

    def exist_language_id(self, language_id):
        return language_id in self.LANGUAGE_DICT

    def get_language_full_name(self, language_id):
        return self.LANGUAGE_DICT[language_id][self.LD_INDEX_FULL_NAME]

    def get_language_id_by_full_name(self, language_full_name):
        language_ids = [language_id for language_id, language_data in self.LANGUAGE_DICT.items() if language_data[self.LD_INDEX_FULL_NAME] == language_full_name]
        if language_ids:
            # 言語フルネームはユニークのはず。リストの先頭を使用する。
            language_id = language_ids[0]
        else:
            language_id = ''
        return language_id

    def get_language_word_original(self, language_id):
        return self.LANGUAGE_DICT[language_id][self.LD_INDEX_WORD_ORIGINAL]

    def get_language_word_translation(self, language_id):
        return self.LANGUAGE_DICT[language_id][self.LD_INDEX_WORD_TRANSLATION]

    def get_all_language_id_and_full_name(self):
        language_data_list = [[language_id, language_data[self.LD_INDEX_FULL_NAME]] for language_id, language_data in self.LANGUAGE_DICT.items()]
        return language_data_list

    def get_typical_language__id_and_full_name(self):
        language_data_list = [[language_id, language_data[self.LD_INDEX_FULL_NAME]] for language_id, language_data in self.LANGUAGE_DICT.items() if language_data[self.LD_INDEX_IS_TYPICAL]]
        return language_data_list

    def is_country_flag(self, stamp):
        return stamp in self.LANGUAGE_STAMP_DICT

    def get_language_id_by_stamp(self, stamp):
        return self.LANGUAGE_STAMP_DICT[stamp]

    def get_all_country_flag(self):
        country_flag_list = [[flag, language_id] for flag, language_id in self.LANGUAGE_STAMP_DICT.items()]
        return country_flag_list
