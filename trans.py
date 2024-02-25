
from googletrans import Translator, LANGUAGES


translator = Translator()
a = translator.translate('good evening', dest="uk")
print(a.text)

