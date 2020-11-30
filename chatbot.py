from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('Bot')

 # Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi ChatBot Here!",
    "What is Tecogno??",
    "Tecogno is a consulting firm.",
    "Tell me about Tecogno",
    "Tecogno is a consulting firm.",

]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)