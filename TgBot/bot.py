import telebot
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from trl import SFTTrainer, DataCollatorForCompletionOnlyLM

TOKEN = '6831302361:AAFz2fFXh5hx6mi8_l_lRXNDUMUiJDgMH-4'

bot = telebot.TeleBot(TOKEN)

model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m")
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")
tokenizer.chat_template = "{% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{% for message in messages %}{% if message['content'] == 'Отзыв' %}{{ '#### Отзыв' + ':\n' +  message['text'] + '\n' }}{% elif message['content'] ==  'Улучшение' %}{{ '#### Улучшение' + ':\n' + message['text'] + '\n' }}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '#### Отзыв:\n' }}{% endif %}"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет!".format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(content_types=['text'])
def message(message):
    inputs = tokenizer(message.text, return_tensors='pt')
    out = model.generate(inputs['input_ids'])
    bot.send_message(message.chat.id, tokenizer.decode(out[0]))
#Запуск
bot.polling(none_stop=True`)`



