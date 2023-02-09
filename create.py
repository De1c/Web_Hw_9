import json

from models import Author, Quote
import connect


with open("authors.json", "r", encoding="utf-8") as f:
    au_data = json.load(f)

with open("quotes.json", "r", encoding="utf-8") as f:
    quote_data = json.load(f)

for au in au_data:
    rec = Author(
        fullname=au["fullname"],
        born_date=au["born_date"],
        born_location=au["born_location"],
        bio=au["bio"],
    )
    rec.save()


def author_id(name):
    authors = Author.objects()
    for author in authors:
        if author.fullname == name:
            return author.id
    return name


for e_quote in quote_data:
    rec = Quote(
        tags=e_quote["tags"],
        author=author_id(e_quote["author"]),
        quote=e_quote["quote"],
    )
    rec.save()
