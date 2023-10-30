from embedding import Embedding
from command import Command

human_input = input("You: ")
embedding = Embedding(human_input)
embedding_command = embedding.embedding()
command = Command(embedding_command)
command.command_execute()
