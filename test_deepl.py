import deepl

auth_key = "49a435b1-7380-4a48-bf9d-11b5db85f42b:fx"
translator = deepl.Translator(auth_key)

try:
    result = translator.translate_text("Hello, world!", target_lang="RU")
    print(result.text)  # Ожидаемый вывод: Привет, мир!
except deepl.exceptions.AuthorizationException as e:
    print(f"Ошибка авторизации: {e}")
except Exception as e:
    print(f"Другая ошибка: {e}")