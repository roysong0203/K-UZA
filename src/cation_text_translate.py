from google.cloud import translate

client = translate.TranslationServiceClient()
response = client.translate_text(
    parent=parent,
    contents=["안녕하세요"],
    mime_type='text/plain',  # mime types: text/plain, text/html
    source_language_code='ko',
    target_language_code='ja')

for translation in response.translations:
    print('Translated Text: {}'.format(translation))