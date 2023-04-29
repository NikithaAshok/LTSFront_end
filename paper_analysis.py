import transformers 
from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig 
import nltk 
nltk.download('punkt') 
from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize,word_tokenize 
from nltk.stem import PorterStemmer 
import string 
import pickle
from rouge_score import rouge_scorer

def split_text(text):
  words = word_tokenize(text)
  length = len(words)
  
  chunks = []
  current_chunk = words[0]
  for sentence in words[1:]:
    if len(current_chunk + " " + sentence) > (length/2):
      chunks.append(current_chunk)
      current_chunk = sentence
    
    else:
      current_chunk += " " + sentence
    
  chunks.append(current_chunk)
  return chunks


# Step 1: Load the model from the saved pickle file
with open("C:/Users/krithika/Downloads/bart_model.pkl", "rb") as f:
    model = pickle.load(f)  


with open('1195.txt', 'r') as file: 
      input_text = file.read()

# input_text = extracted_text.decode("utf-8")  # read and decode file contents
bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
final_summary = ""
chunks = []
chunks = split_text(input_text)
for chunk in chunks:
    bart_inputs = bart_tokenizer.encode(chunk,return_tensors='pt', max_length=1024, truncation=True)
    bart_summary_ids = bart_model.generate(bart_inputs, num_beams=4, max_length=400, early_stopping=True)
    bart_summary = bart_tokenizer.decode(bart_summary_ids[0],skip_special_tokens=True)
    final_summary += bart_summary


# print("\nGenerated summary:\n", final_summary)
#print('bart summary',final_summary)

reference_summary=' '
with open('ref1195.txt', 'r') as file:
    reference_summary = file.read()

# Calculate ROUGE scores
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
scores = scorer.score(str(bart_summary), reference_summary)
print(scores)