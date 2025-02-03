def rev_sent(sent):
    a=sent.split()
    a.reverse()
    newsent=""
    for x in a:
        newsent+=x+" "
    return newsent
sent=str(input())
print(rev_sent(sent))
