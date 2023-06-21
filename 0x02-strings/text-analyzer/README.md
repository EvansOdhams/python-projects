# Text Analyzer

This README provides an overview of the Text Analyzer program, which analyzes a given text input and provides various statistics such as the number of characters, words, sentences, and paragraphs. Additionally, it demonstrates the implementation of features like finding the most frequent words and generating word clouds.

## Features

### 1. Text Statistics:
	Number of characters: Calculates the total number of characters in the text, excluding whitespaces.
	Number of words: Splits the text into words and counts the total number of words.
	Number of sentences: Splits the text into sentences based on punctuation marks (. ! ?) and counts the total number of sentences.
	Number of paragraphs: Splits the text based on empty lines and counts the total number of paragraphs.

### 2. Additional Features:
	Most frequent words: Identifies and displays the top N most frequent words in the text.
	Word clouds: Generates a word cloud visualization to represent the most frequent words in the text.

## Getting Started

To use the Text Analyzer program, follow these steps:

	Clone the repository or download the source code files.

	Install the required dependencies, such as the wordcloud library, by running the following command:

#####	pip install wordcloud

	Run the program and provide the text input for analysis.

	View the displayed statistics, including the number of characters, words, sentences, and paragraphs.

	Optionally, explore additional features like finding the most frequent words and generating word clouds.

## Usage
	To use the Text Analyzer program, execute the main script, text_analyzer.py, and follow the on-screen prompts. Here's an example usage:

	$ python text_analyzer.py

	== Text Analyzer ==

	Enter the text to analyze:
	Lorem ipsum dolor sit amet, consectetur adipiscing elit.

	== Statistics ==
	Number of characters: 42
	Number of words: 5
	Number of sentences: 1
	Number of paragraphs: 1

	Do you want to find the most frequent words? (y/n): y
	Enter the number of most frequent words to display: 3

	== Most Frequent Words ==
	1. lorem
	2. ipsum
	3. dolor

	Do you want to generate a word cloud? (y/n): y
	Enter the filename to save the word cloud image: word_cloud.png

	Word cloud generated and saved as word_cloud.png.


## Dependencies

	== The Text Analyzer program requires the following dependencies: ==
	wordcloud: Used for generating word cloud visualizations. Install it using the command mentioned in the "Getting Started" section.

## Contributing
	Contributions to the Text Analyzer program are welcome! If you have any suggestions, improvements, or new features to propose, please create an issue or submit a pull request.

## License
	The Text Analyzer program is licensed under the MIT License. Feel free to modify and use the code for your own projects.
