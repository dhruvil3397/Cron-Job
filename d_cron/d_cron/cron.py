def hello():
    print("Hello")
    with open('a.txt', 'w') as f:
        f.write('hi')
