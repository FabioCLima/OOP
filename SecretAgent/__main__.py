# __main__.py

from src.secretagent import SecretAgent
from src.secretagent import Message

mouse = SecretAgent("Mouse")
armadillo = SecretAgent("Armadillo")
fox = SecretAgent("Fox")
weasel = SecretAgent("Weasel")

SecretAgent._codeword = "Parmesan"
print(armadillo._codeword)

mouse._codeword = "Cheese"
print(mouse._codeword)

msg = Message()
# print(msg.__format)  # AttributeError - name mangling

print(msg._Message__format)
