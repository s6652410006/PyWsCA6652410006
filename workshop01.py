def countwords(sentence):
    words = sentence.split()
    totalwords = len(words)
    uniquewords = set(words)

    dupliwordscount = totalwords - len(uniquewords)
    dupliwords = {word: words.count(word) for word in uniquewords if words.count(word) > 1}
    return totalwords, dupliwordscount, dupliwords

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
inputsentence = input("ป้อนข้อความ: ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

totalwords, dupliwordscount, dupliwords = countwords(inputsentence)
print(f"มีคำทั้งหมด {totalwords} คำ")
print(f"มีคำที่ซ้ำกัน {dupliwordscount} คำ คือ {', '.join(dupliwords.keys())}")

for word, count in dupliwords.items():
    print(f"คำว่า '{word}' ซ้ำกัน {count} ครั้ง")
    
try :
    inputsentence = input("ป้อนข้อความ: ")
    countwords(inputsentence)
except Exception as e :
    print(f"เกิดข้อผิดพลาด: {e}")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")