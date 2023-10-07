greeting = input("Greeting: ").strip()
if greeting.__len__() >= 5 and greeting[0:5].lower() == "hello":
    print("$0")
elif greeting.__len__() > 0 and greeting[0:1].lower()=="h":
    print("$20")
else:
    print("$100")
