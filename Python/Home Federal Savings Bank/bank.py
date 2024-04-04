hello = "hello"

answer = input("Greeting: ").lstrip().lower()

if hello in answer:
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")
