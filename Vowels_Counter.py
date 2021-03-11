x = input("Enter the Sentence :")
string = x.lower()
print(string)
Vowel_counts = {}
for Vowel in "aeiou" :
    count = x.count(Vowel)
    Vowel_counts[Vowel] = count

print(Vowel_counts)