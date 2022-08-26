from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)


def dost(mess):
    l1 = mess.split('.')
    results = model.predict(l1, k=2)

    l2 = []
    for message, sentiment in zip(l1, results):
        print(message, '->', sentiment)
        l2.append(sentiment)
    return l2
