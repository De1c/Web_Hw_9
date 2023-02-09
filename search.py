import redis
from redis_lru import RedisLRU


from models import Quote
import connect

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def get_from_name(name):
    right_quotes = []
    quotes = Quote.objects()
    for quote in quotes:
        if quote.author.fullname.capitalize() == name.capitalize():
            author = quote.author.fullname
            right_quotes.append(quote.quote)
    else: 
        return f"Sorry, couldn't find author - {name}"
    return f"{author} quotes: {right_quotes}"


@cache
def get_from_tag(searched_tag):
    right_quotes = []
    quotes = Quote.objects()
    for quote in quotes:
        for tag in quote.tags:
            if tag in searched_tag.split(","):
                right_quotes.append(quote.quote)
        print(right_quotes)
    return right_quotes


def main():
    while True:
        inp = (input("Enter your command: ")).strip().split(":")
        command = inp[0]
        data = inp[-1]
        match command:
            case "name":
                print(get_from_name(data))
            case "tag" | "tags":
                print(get_from_tag(data))
            case "exit":
                print("Bye and have a nice day!")
                break
            case _:
                print("There is no such a command, Sorry!")


if __name__ == "__main__":
    main()