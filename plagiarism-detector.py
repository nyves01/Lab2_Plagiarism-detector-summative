import os
import string

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print(f"Warning: {file_path} not found. Returning empty content.")
        return ""

def clean_text(raw_text):
    stop_words = ['a', 'an', 'the', 'is', 'in', 'of', 'and', 'to', 'for']
    text = raw_text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    clean_words = [w for w in words if w not in stop_words]
    return clean_words

def words_to_set(word_list):
    return set(word_list)

def search_word(word, text1, text2):
    word = word.lower()
    return text1.lower().split().count(word), text2.lower().split().count(word)

if __name__ == "__main__":
    essay1_path = "essays/essay1.txt"
    essay2_path = "essays/essay2.txt"

    # Read files
    essay1_raw = read_file(essay1_path)
    essay2_raw = read_file(essay2_path)

    # Clean text
    essay1_clean = clean_text(essay1_raw)
    essay2_clean = clean_text(essay2_raw)

    # Sets for unique words
    set1 = words_to_set(essay1_clean)
    set2 = words_to_set(essay2_clean)

    common_words = set1.intersection(set2)
    print("\nCommon words in both essays:")
    print(common_words)

    union_words = set1.union(set2)

    if len(union_words) == 0:
        similarity = 0
    else:
        similarity = (len(common_words) / len(union_words)) * 100

    print(f"\nPlagiarism (Jaccard Similarity): {similarity:.2f}%")

    if similarity >= 50:
        print("High similarity detected (possible plagiarism).")
    else:
        print("Similarity is low.")

    print("\n--- WORD SEARCH ---")
    word = input("Enter a word to search: ")
    count1, count2 = search_word(word, essay1_raw, essay2_raw)
    print(f"'{word}' appears {count1} times in Essay 1")
    print(f"'{word}' appears {count2} times in Essay 2")

    save = input("\nDo you want to save the similarity report? (y/n): ").lower()
    if save == 'y':
        with open("reports/similarity_report.txt", "w", encoding="utf-8") as f:
            f.write(f"Plagiarism Percentage: {similarity:.2f}%\n")
            f.write("Common Words:\n")
            for w in common_words:
                f.write(f"- {w}\n")
        print("Report saved successfully in reports/similarity_report.txt")
    else:
        print("Report not saved.")
