from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', chatbot=chatbot)

if __name__ == "__main__":
    # Give a name to the chatbot “corona bot”
    # and assign a trainer component.
    chatbot=ChatBot('heart bot')
    
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    
    # Now let us train our bot with multiple corpus
    trainer.train("chatterbot.corpus.custom.cardiovascular_training")

    app.run(debug=True)
    