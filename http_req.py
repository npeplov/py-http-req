import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text:
    :param from_lang:
    :param to_lang:
    :return:
    """
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }
    response = requests.get(URL, params=params)
    json_res = response.json()
    return ''.join(json_res['text'])


def read_file(name):
    text_list = []
    with open(name, encoding="utf-8") as fi:
        for line in fi:
            text_list.append(line)
    return text_list


def write_file(name, result):
    with open(name, 'w', encoding="utf-8") as fo:
        fo.write(result)


if __name__ == '__main__':
    write_file('DE-RU.txt', translate_it(read_file('DE.txt'), 'de', 'ru'))
    write_file('ES-RU.txt', translate_it(read_file('ES.txt'), 'es', 'ru'))
    write_file('FR-RU.txt', translate_it(read_file('FR.txt'), 'fr', 'ru'))

