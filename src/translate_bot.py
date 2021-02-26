from translate_db import TranslateDatabase
import discord
import re
from googletrans import Translator
import emoji
import config

# constants
KEYWORD_TRANSLATE = '!trans'
KEYWORD_HELP = 'help'
KEYWORD_LANGUAGE = 'lng'
KEYWORD_MAX_NUM = 3

# global variables
translate_db = TranslateDatabase()

class TranslateClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print('------')

    async def on_message(self, message):
        if not message.author.bot:
            msg = message.content

            keywords, text = text_analysis(msg, KEYWORD_MAX_NUM)
            if keywords[0] == KEYWORD_TRANSLATE:
                if keywords[1] == KEYWORD_HELP:
                    if keywords[2] == KEYWORD_LANGUAGE:
                        m = get_language_list_message()
                    else:
                        m = get_help_message()
                    try:
                        await message.channel.send(content=m)
                    except:
                        pass
                else:
                    if keywords[1] != '':
                        dst_language = keywords[1]
                    else:
                        dst_language = 'en'

                    if text != '':
                        text = replace_mention(text, message)
                        msg, src_language_id, dst_language_id, trans_text = translate(dst_language, text)
                        await send_trans_message(message.channel, message.author, msg, src_language_id, dst_language_id, text, trans_text)


    async def on_reaction_add(self, reaction, user):
        if not user.bot and not reaction.message.author.bot:
            if translate_db.is_country_flag(reaction.emoji):
                dst_language_id = translate_db.get_language_id_by_stamp(reaction.emoji)
                text = reaction.message.content
                text = replace_mention(text, reaction.message)
                if text != '':
                    msg, src_language_id, dst_language_id, trans_text = translate(dst_language_id, text)
                    await send_trans_message(reaction.message.channel, user, msg, src_language_id, dst_language_id, text, trans_text)


# functions
def translate(dst_language, text):
    msg = ''
    simple_text = remove_emoji(text)
    translator = Translator()

    # 翻訳元言語の特定
    src_language_id = translator.detect(remove_mention(simple_text)).lang   # メンションがあると正しく言語を判定できないため、削除して渡す

    # 翻訳先言語の特定
    if dst_language != '':
        if translate_db.exist_language_id(dst_language):
            dst_language_id = dst_language
        else:
            # IDとして存在しない場合は、フルネームでの検索をする
            dst_language_id = translate_db.get_language_id_by_full_name(dst_language)
            if dst_language_id == '':
                # どちらにも存在しない場合は、英語に翻訳する
                dst_language_id = 'en'
                msg = msg + '[Warning] The given sentence is automatically translated into English because the selected language is not supported.\n'
    else:
        dst_language_id = 'en'

    # 翻訳
    trans_text = translator.translate(src=src_language_id, dest=dst_language_id, text=simple_text).text

    return [msg, src_language_id, dst_language_id, trans_text]


async def send_trans_message(channel, request_author, msg, src_language_id, dst_language_id, original_text, trans_text):
    src_language_full_name = translate_db.get_language_full_name(src_language_id)
    dst_language_full_name = translate_db.get_language_full_name(dst_language_id)
    word_original = translate_db.get_language_word_original(dst_language_id)
    word_translation = translate_db.get_language_word_translation(dst_language_id)

    embed_msg = discord.Embed(title=src_language_full_name + ' -> ' + dst_language_full_name, colour=0x3498db)
    embed_msg.add_field(name='[' + word_original + ']', value=original_text, inline=False)
    embed_msg.add_field(name='[' + word_translation + ']', value=trans_text, inline=False)
    embed_msg.set_footer(text='<This translation is made by machine, which is thus not always correct.>')
    msg = request_author.mention + '\n' + msg
    try:
        await channel.send(content=msg, embed=embed_msg)
    except:
        msg = request_author.mention \
            + '\nSorry, but couldn\'t translate the given sentence.\n' \
            + 'That is probably because it is too long.'
        try:
            await channel.send(content=msg)
        except:
            pass


def text_analysis(string, max_keyword_num):
    keywords = []
    text = ''

    split_text = string.split('\n', 1)
    if split_text:
        keywords = re.sub('\s+', ' ', split_text[0].strip(' ')).split(' ')
        if len(split_text) > 1:
            text = split_text[1]

    empty_list = [''] * max_keyword_num
    keywords.extend(empty_list)

    return keywords, text


def get_help_message():
    m = 'Format :\n' \
        + '```\n' \
        + '!trans [Translation language]\n' \
        + '[text]\n' \
        + '```\n' \
        + 'Example :\n' \
        + '```\n' \
        + '!trans ja\n' \
        + 'I love VIPSTARCOIN!!\n' \
        + '```\n' \
        + 'List of available languages :\n' \
        + '```\n'

    language_data_list = translate_db.get_typical_language__id_and_full_name()

    for i, language_data in enumerate(language_data_list):
        add_str = language_data[1] + ': ' + language_data[0]
        m = m + add_str
        if (i + 1) % 3 == 0:
            m = m + '\n'
        else:
            m = m + ' ' * (21 - len(add_str))
    if m[-1:] != '\n':
        m = m + '\n'
    m = m + '\nNot all of the available languages are shown here. ' \
        + 'If you want to see all of them, you can type \'' + KEYWORD_TRANSLATE + ' ' + KEYWORD_HELP + ' ' + KEYWORD_LANGUAGE + '\'.\n```\n'

    m = m + 'Another way :\n' \
        + '  You can also use national flag reactions in order to translate a message into a language relevant to a country you\'ve picked.\n'
    flag_data_list = translate_db.get_all_country_flag()
    for i, flag_data in enumerate(flag_data_list):
        language_full_name = translate_db.get_language_full_name(flag_data[1])
        add_str = flag_data[0] + ': ' + language_full_name
        if (i + 1) % 3 == 0:
            m = m + add_str + '\n'
        elif (i + 1) % 3 == 1:
            m = m + '    ' + add_str + ' ' * (21 - len(language_full_name))
        else:
            m = m + add_str + ' ' * (21 - len(language_full_name))

    return m


def get_language_list_message():
    m = 'List of all the available languages :\n' \
        + '```\n'

    language_data_list = translate_db.get_all_language_id_and_full_name()
    for i, language_data in enumerate(language_data_list):
        add_str = language_data[1] + ': ' + language_data[0]
        m = m + add_str
        if (i + 1) % 4 == 0:
            m = m + '\n'
        else:
            m = m + ' ' * (21 - len(add_str))
    if m[-1:] != '\n':
        m = m + '\n'
    m = m + '```\n'

    return m


def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)


def replace_mention(src_str, message):
    replaced_str = src_str

    for mention in message.mentions:
        replaced_str = replaced_str.replace('<@' + mention.id + '>', '`@' + mention.name + '`')

    for role_mention in message.role_mentions:
        replaced_str = replaced_str.replace('<@&' + role_mention.id + '>', '`@' + role_mention.name + '`')

    replaced_str = replaced_str.replace('@everyone', '`everyone`')
    replaced_str = replaced_str.replace('@here', '`here`')

    for channel_mention in message.channel_mentions:
        replaced_str = replaced_str.replace('<#' + channel_mention.id + '>', '`#' + channel_mention.name + '`')

    return replaced_str


# 制約： replace_mention で変換した文字列を渡すこと
def remove_mention(src_str):
    removed_str = src_str
    
    removed_str = re.sub(r'`[@#].+`', '', removed_str)
    removed_str = re.sub(r'`everyone`', '', removed_str)
    removed_str = re.sub(r'`here`', '', removed_str)

    return removed_str


if __name__ == '__main__':
    client = TranslateClient()
    client.run(config.DISCORD_TOKEN)
