choiceA = {"1Y","2Y","3Y","4N","5N","6Y","7Y","8N","9Y"}
choiceB = {"1N","2N","3Y","4Y","5Y","6N","7Y","9Y"}
choiceC = {"1N","2N","3Y","4Y","6N","7Y","8Y","9N"}
def similarity(setA:set,setB:set)-> float:
    return len(setA & setB) / max(len(setA),len(setB))
print(f"A和B的相似度为{format(similarity(choiceA,choiceB),'.2f')}")
print(f"A和C的相似度为{format(similarity(choiceA,choiceC),'.2f')}")
print(f"B和C的相似度为{format(similarity(choiceB,choiceC),'.2f')}")
