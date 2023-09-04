def is_anagrama(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        return False
    return sorted(word1) == sorted(word2)

print(is_anagrama("Amor", "Roma"))