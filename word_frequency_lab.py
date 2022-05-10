p = "This is a story about Bob. Bob was a normal fellow, with dark brown hair and brown eyes, average looking, and not super athletic. Bob worked in the marketing department for a corporation called LifeTech."
pgrLs = p.lower().replace(".", "").split(" ")


while True:
    f = 0
    r = input("What word would you like to know the frequency of? - ")
    for i in range(len(pgrLs)):
        if r == pgrLs[i]:
            f += 1
    if f == 1:
        print(f"{r} appeared {f} time")
    elif f > 1:
        print(f"{r} appeared {f} times")
    else:
        print(f"{r} does not appear in the story")