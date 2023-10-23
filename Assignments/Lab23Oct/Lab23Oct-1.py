# count vowels and constants in a string
str1='Ambiguity'
str1=str1.lower()
print(str1)
vowel_count=0
consonant_count=0
for x in str1:
    if x in ('a','e','i','o','u'):
        vowel_count=vowel_count+1
    else:
        consonant_count= consonant_count + 1
print(f"vowel count is {vowel_count}")
print(f"consonant count is {consonant_count}")
