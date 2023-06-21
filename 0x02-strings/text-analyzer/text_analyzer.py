#!/usr/bin/python3


import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def calculate_statistics(text):
    # Count the number of characters by removing whitespaces
    num_characters = len(text.replace(" ", ""))
    
    # Count the number of words using regular expression pattern matching
    num_words = len(re.findall(r'\b\w+\b', text))
    
    # Count the number of sentences using punctuation marks
    num_sentences = len(re.findall(r'[.!?]+', text))
    
    # Count the number of paragraphs using empty lines
    num_paragraphs = len(re.findall(r'\n\s*\n', text))
    
    return num_characters, num_words, num_sentences, num_paragraphs

def find_most_frequent_words(text, num_words):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Return the most frequent words
    return word_counts.most_common(num_words)

def generate_word_cloud(text):
    # Generate word cloud visualization
    wordcloud = WordCloud().generate(text)
    
    # Display the word cloud image
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def main():
    print("== Text Analyzer ==")
    text = input("Enter the text to analyze:\n")

    # Calculate statistics
    num_characters, num_words, num_sentences, num_paragraphs = calculate_statistics(text)
    print("\n== Statistics ==")
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")
    print(f"Number of sentences: {num_sentences}")
    print(f"Number of paragraphs: {num_paragraphs}")

    # Find most frequent words
    freq_word_option = input("\nDo you want to find the most frequent words? (y/n): ")
    if freq_word_option.lower() == 'y':
        try:
            num_freq_words = int(input("Enter the number of most frequent words to display: "))
            frequent_words = find_most_frequent_words(text, num_freq_words)
            print("\n== Most Frequent Words ==")
            for word, count in frequent_words:
                print(f"{word}: {count}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate word cloud
    word_cloud_option = input("\nDo you want to generate a word cloud? (y/n): ")
    if word_cloud_option.lower() == 'y':
        filename = input("Enter the filename to save the word cloud image: ")
        generate_word_cloud(text)
        plt.savefig(filename)
        print(f"Word cloud generated and saved as {filename}.")

if __name__ == "__main__":
    main()
