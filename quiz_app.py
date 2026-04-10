import random

quiz_data = {
"C++":[
{"q":"Who developed C++?","options":["A. Bjarne Stroustrup","B. Dennis Ritchie","C. James Gosling","D. Guido"],"ans":"A"},
{"q":"C++ is which type?","options":["A. High-level","B. Low-level","C. Machine","D. Assembly"],"ans":"A"},
{"q":"Symbol for comments?","options":["A. //","B. ##","C. **","D. !!"],"ans":"A"},
{"q":"C++ supports?","options":["A. OOP","B. Procedural","C. Both","D. None"],"ans":"C"},
{"q":"cin is used for?","options":["A. Output","B. Input","C. Loop","D. Class"],"ans":"B"},
{"q":"cout is used for?","options":["A. Input","B. Output","C. Loop","D. Class"],"ans":"B"},
{"q":"Header for I/O?","options":["A. iostream","B. stdio","C. conio","D. math"],"ans":"A"},
{"q":"Scope operator?","options":["A. ::","B. .","C. ->","D. #"],"ans":"A"},
{"q":"Loop types?","options":["A. for","B. while","C. do-while","D. All"],"ans":"D"},
{"q":"Supports inheritance?","options":["A. Yes","B. No","C. Maybe","D. None"],"ans":"A"}
],

"Java":[
{"q":"Java developed by?","options":["A. Sun Microsystems","B. Microsoft","C. Apple","D. IBM"],"ans":"A"},
{"q":"Java is?","options":["A. Platform dependent","B. Platform independent","C. Machine","D. None"],"ans":"B"},
{"q":"Keyword for class?","options":["A. class","B. define","C. struct","D. object"],"ans":"A"},
{"q":"Entry method?","options":["A. main()","B. start()","C. run()","D. init()"],"ans":"A"},
{"q":"Java supports OOP?","options":["A. Yes","B. No","C. Partial","D. None"],"ans":"A"},
{"q":"Statement ends with?","options":["A. ;","B. :","C. .","D. ,"],"ans":"A"},
{"q":"Not primitive type?","options":["A. int","B. float","C. string","D. char"],"ans":"C"},
{"q":"Inheritance keyword?","options":["A. extends","B. implements","C. inherit","D. super"],"ans":"A"},
{"q":"Uses bytecode?","options":["A. Yes","B. No","C. Partial","D. None"],"ans":"A"},
{"q":"JVM stands for?","options":["A. Java Virtual Machine","B. Java Variable Machine","C. Just VM","D. None"],"ans":"A"}
],

"Python":[
{"q":"Who developed Python?","options":["A. Guido","B. Elon","C. Gates","D. Jobs"],"ans":"A"},
{"q":"Python is?","options":["A. Low-level","B. High-level","C. Machine","D. None"],"ans":"B"},
{"q":"Keyword for function?","options":["A. def","B. func","C. define","D. fun"],"ans":"A"},
{"q":"Symbol for comment?","options":["A. #","B. //","C. **","D. !!"],"ans":"A"},
{"q":"List is?","options":["A. Mutable","B. Immutable","C. Both","D. None"],"ans":"A"},
{"q":"Tuple is?","options":["A. Mutable","B. Immutable","C. Both","D. None"],"ans":"B"},
{"q":"Loop types?","options":["A. for","B. while","C. Both","D. None"],"ans":"C"},
{"q":"Supports OOP?","options":["A. Yes","B. No","C. Partial","D. None"],"ans":"A"},
{"q":"Input function?","options":["A. input()","B. get()","C. read()","D. scan()"],"ans":"A"},
{"q":"Output function?","options":["A. print()","B. show()","C. write()","D. out()"],"ans":"A"}
],

"HTML":[
{"q":"HTML stands for?","options":["A. Hyper Text Markup Language","B. High Text ML","C. Hyper Tool ML","D. None"],"ans":"A"},
{"q":"HTML is?","options":["A. Programming","B. Markup","C. Machine","D. None"],"ans":"B"},
{"q":"Heading tag?","options":["A. <h1>","B. <p>","C. <div>","D. <span>"],"ans":"A"},
{"q":"Paragraph tag?","options":["A. <p>","B. <h1>","C. <br>","D. <hr>"],"ans":"A"},
{"q":"Link tag?","options":["A. <a>","B. <link>","C. <href>","D. <url>"],"ans":"A"},
{"q":"Link attribute?","options":["A. href","B. src","C. link","D. url"],"ans":"A"},
{"q":"File extension?","options":["A. .html","B. .ht","C. .xml","D. .txt"],"ans":"A"},
{"q":"Image tag?","options":["A. <img>","B. <pic>","C. <image>","D. <src>"],"ans":"A"},
{"q":"List tag?","options":["A. <ul>","B. <ol>","C. Both","D. None"],"ans":"C"},
{"q":"Case sensitive?","options":["A. Yes","B. No","C. Partial","D. None"],"ans":"B"}
]
}

def start_quiz():
    print("\nTopics:")
    for t in quiz_data:
        print("-", t)

    topic = input("Enter topic: ")

    if topic not in quiz_data:
        print("Invalid topic")
        return

    questions = quiz_data[topic]
    random.shuffle(questions)

    score = 0

    for q in questions:
        print("\n", q["q"])
        for opt in q["options"]:
            print(opt)

        try:
            ans = input("Answer: ").upper()
            if ans == q["ans"]:
                print("Correct")
                score += 1
            else:
                print("Wrong. Correct:", q["ans"])
        except:
            print("Error")

    print("Score:", score, "/", len(questions))

def main():
    while True:
        print("\n1.Start Quiz\n2.Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            start_quiz()
        elif ch == "2":
            break
        else:
            print("Invalid")

main()