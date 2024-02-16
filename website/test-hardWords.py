from uTranscribe import *
from openai import OpenAI


def getHardWords(inputText, gradeLevel = "undergraduate", courseType="scientific"):
    print("OpenAI:", inputText)
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a note-taking assistant to a {gradeLevel} student that only returns a list of {courseType} terms that they might not know, with their definitions in word:definition JSON format."},
            {"role": "user", "content": f"give me definitions of the {courseType} words in the following passage that a gifted {gradeLevel} student would find difficult: {inputText}"}
        ]
    )
    try:
        termList = completion.choices[0].message.content
        print()
        print("TermList")
        print(termList)
        print()
        termListA = json.loads(termList)
        n = 0
        for term, definition in termListA.items():
            n+=1
            print(f"  {n}: {term}: {definition}")
            myTranscriber.hardWordsDict[term] = definition
        return termList
    except:
        return {}
    
if __name__ == "__main__":
    txt = "Time dilation is when time passes slower for an observer."
    # txt = " observer who is moving relative to somebody who is stationary and it's measure anything."
    output = getHardWords(txt, "college")
    print(output)