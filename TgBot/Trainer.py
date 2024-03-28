from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset, Dataset
from trl import SFTTrainer, DataCollatorForCompletionOnlyLM

dataset = load_dataset("lucasmccabe-lmi/CodeAlpaca-20k", split="train")

model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m")
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")

def formatting_prompts_func(example: list[dict]):
  result = []
  for feedback in example['feedbacks']:
    text = tokenizer.apply_chat_template(feedback, tokenize=False, add_generation_prompt=False)
    text = tokenizer.apply_chat_template(feedback, tokenize=False, add_generation_prompt=False)
    result.append(text)
  return result

instruction_template = "#### Отзыв:"
response_template = "#### Улучшение:"
collator = DataCollatorForCompletionOnlyLM(instruction_template=instruction_template, response_template=response_template, tokenizer=tokenizer, mlm=False)

trainer = SFTTrainer(
    model,
    train_dataset=ds,
    formatting_func=formatting_prompts_func,
    data_collator=collator,
)

trainer.train()