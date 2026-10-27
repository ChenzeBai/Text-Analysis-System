import os
import string
import matplotlib.pyplot as plt
import json

selected_file = None
selected_path = None
selected_file_path = None


#路径
def find_file(path):
    count = 1
    text_files = []
    if os.path.exists(path) and os.path.isdir(path):
        found = False
        print('Available text files:')
        files = os.listdir(path)
        for file in files:
            if file.endswith('.txt'):
                found = True
                text_files.append(file)
                print(f'{count}. {file}')
                count += 1
        if not found:
            print('No text documents found!')
    else:
        print('You entered a wrong folder path!')
    return text_files


#选文件
def correct_choose(result):
    while True:
        try:
            choose = int(input('Please enter your choice: '))
            choose -= 1
        except ValueError:
            print('Please enter an integer')
            continue

        if choose < 0 or choose >= len(result):
            print('Please enter a valid number')
            continue
        return choose


#case3 基础统计
def analyse_text_basic(selected_file_path):
    word_list = []
    letter_count = 0
    letter_count_space = 0
    line_count = 0
    word_length_count = 0

    with open(selected_file_path, 'r') as f:
        for line in f:
            line_count += 1
            words = line.split()
            letter_count_space += len(line.rstrip('\n'))
            letter_count += len(''.join(line.split()))

            for word in words:
                cleaned_word = word.lower().strip('.,!?;:"()[]{}\'')
                if cleaned_word != '':
                    word_list.append(cleaned_word)
                    word_length_count += len(cleaned_word)
        if line_count != 0:
            average_line_word = round(len(word_list) / line_count, 2)
        else:
            average_line_word = 0
            
        if len(word_list) != 0:
            average_line_letter = round(word_length_count / len(word_list), 2)
        else:
            average_line_letter = 0
        
    print(f'The number of words in the file is: {len(word_list)}')
    print(f'The number of characters(including spaces) in the file is: {letter_count_space}')
    print(f'The number of characters(NOT including spaces) in the file is: {letter_count}')
    print(f'The number of unique words is: {len(set(word_list))}')
    print(f'The average words in each line is {average_line_word}')
    print(f'The average letter in each word is {average_line_letter}')
    print(f'The number of lines in the file is: {line_count}')
    basic_stats = {
    'total_words': len(word_list),
    'total_characters_including_spaces': letter_count_space,
    'total_characters_excluding_whitespace': letter_count,
    'unique_words': len(set(word_list)),
    'average_words_per_line': average_line_word,
    'average_characters_per_word': average_line_letter,
    'total_lines': line_count
    }

    return basic_stats



#case4 前十单词
def analyse_text_word(selected_file_path):
    word_count = {}

    with open(selected_file_path, 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                word_cleaned = word.lower().strip('.,!?;:"()[]{}\'')

                if word_cleaned != '':
                    if word_cleaned in word_count:
                        word_count[word_cleaned] += 1
                    else:
                        word_count[word_cleaned] = 1
    
        sorted_words = sorted(word_count, key=word_count.get, reverse=True)
        top_words = sorted_words[:10]

        print('The most common words in the file are:')

        for i in range(len(top_words)):
            word = top_words[i]
            print(f"{i + 1}. {word} (appears {word_count[word]} times)")

    return word_count

#case4 不重复单词以及只出现一次单词数
def unique_word_analysis(selected_file_path):
    word_lst = {}
    count = 0
    with open(selected_file_path,'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                cleaned_word = word.strip('.,!?;:"()[]{}\'').lower()
                if cleaned_word != '':
                    if cleaned_word in word_lst:
                        word_lst[cleaned_word] += 1
                    else:
                        word_lst[cleaned_word] = 1
    for word in word_lst:    
        if word_lst[word] == 1:
            count += 1
    print(f'The number of unique word is {len(word_lst)}')
    print(f'The number of words appearing only once is {count}')
    return {
    'unique_words': len(word_lst),
    'words_appearing_once': count
    }

#路径查找
def file_path_detector(selected_file_path):
    if not selected_file_path:
        selected_file_path = input('Please enter your document path that you want to analysis')
    while not os.path.isfile(selected_file_path) or not selected_file_path.lower().endswith('.txt'):
        print('File does not exist. Please enter a valid file path enns with .txt')
        selected_file_path = input(
            'Please enter your document path: '
        )

    return selected_file_path


#case4 单词长度分布
def word_length_distribution(selected_file_path):
    word_length = {}

    with open(selected_file_path, 'r') as f:
        for line in f:
            words = line.split()

            for word in words:
                word = word.lower().strip('.,!?;:"()[]{}\'')
                
                if word != '':
                    length = len(word)

                    if length in word_length:
                        word_length[length] += 1
                    else:
                        word_length[length] = 1

    for length in sorted(word_length):
        print(f'There are {word_length[length]} words with length {length}')
    return word_length

#case5 句子查找
def analyse_text_sentence(selected_file_path):
    sentences = []
    sentence = ''
    with open(selected_file_path, 'r') as f:
        for line in f:
            for text in line:
                if text == '.' or text == '?' or text == '!':
                    if sentence.strip() != '': 
                        sentences.append(sentence.strip())
                    sentence = ''
                else:
                    sentence += text

        if sentence.strip() != '':
            sentences.append(sentence.strip())

    print(f'The number of sentences is {len(sentences)}')
    return sentences

#case5 最长/短句子
def longest_shortest_sentence(selected_file_path):
    sentence_list = []
    longest_length = 0
    longest_sentence = ''
    shortest_sentence = ''
    with open(selected_file_path,'r') as f:
        for line in f:
            sentence = ''
            for char in line:
                if char == '.' or char == '?' or char == '!':
                    if sentence.strip() != ''and any(char.isalnum() for char in sentence):
                        sentence_list.append(sentence.strip())
                    sentence = ''
                else:
                    sentence += char
            if sentence.strip() != '':
                sentence_list.append(sentence.strip())

        if len(sentence_list) == 0:
                print('No sentences')
                return
        shortest_length = 99999
        for sentence in sentence_list:
            if len(sentence) > longest_length:
                    longest_length = len(sentence)
                    longest_sentence = sentence
            if len(sentence) < shortest_length:
                    shortest_length = len(sentence)
                    shortest_sentence = sentence
    print(f'The longest sentence is: {longest_sentence} for {longest_length} characters')
    print(f'The shortest sentence is {shortest_sentence} for {shortest_length} characters')
    return {
    'longest_sentence': longest_sentence,
    'longest_sentence_length': longest_length,
    'shortest_sentence': shortest_sentence,
    'shortest_sentence_length': shortest_length
}


#case6 字符分析
def character_analysis(selected_file_path):
    library_basic = {}
    library_upper = {}
    library_punctuation = {}

    with open(selected_file_path, 'r') as f:
        for line in f:
            for char in line:
                if char.isalpha():
                    if char == char.lower():
                        if char in library_basic:
                            library_basic[char] += 1
                        else:
                            library_basic[char] = 1

                    elif char == char.upper():
                        if char in library_upper:
                            library_upper[char] += 1
                        else:
                            library_upper[char] = 1
                elif char in string.punctuation:
                    if char in library_punctuation:
                        library_punctuation[char] += 1
                    else:
                        library_punctuation[char] = 1

    for char in sorted(library_basic):
        print(f'Letter {char}: {library_basic[char]}')
    for char in sorted(library_upper):
        print(f'Letter {char}: {library_upper[char]}')
    print(f'There are {sum(library_punctuation.values())} punctuations')
    return {
    'lowercase_letters': library_basic,
    'uppercase_letters': library_upper,
    'punctuation': library_punctuation
}


#case7 图表
def visualise_statistics(selected_file_path):
    word_count = analyse_text_word(selected_file_path)
    length_count = word_length_distribution(selected_file_path)

    #前十单词
    sorted_words = sorted(
        word_count,
        key=word_count.get,
        reverse=True
    )

    top_words = sorted_words[:10]
    top_counts = []

    for word in top_words:
        top_counts.append(word_count[word])

    plt.figure(figsize=(10, 5))
    plt.bar(top_words, top_counts)
    plt.title('Top 10 Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    #长度
    lengths = sorted(length_count)
    counts = []

    for length in lengths:
        counts.append(length_count[length])

    plt.figure(figsize=(10, 5))
    plt.bar(lengths, counts)
    plt.title('Word Length Distribution')
    plt.xlabel('Word Length')
    plt.ylabel('Number of Words')
    plt.tight_layout()
    plt.show()


#case8 json
def export_statistics(selected_file_path):
    basic_stats = analyse_text_basic(selected_file_path)
    word_count = analyse_text_word(selected_file_path)
    length_count = word_length_distribution(selected_file_path)
    character_stats = character_analysis(selected_file_path)
    unique_stats = unique_word_analysis(selected_file_path)
    sentences = analyse_text_sentence(selected_file_path)
    sentence_stats = longest_shortest_sentence(selected_file_path)

    statistics = {
    'basic_statistics': basic_stats,
    'word_frequency': word_count,
    'word_length_distribution': length_count,
    'character_analysis': character_stats,
    'unique_word_analysis': unique_stats,
    'sentence_count': len(sentences),
    'sentence_analysis': sentence_stats
}

    output_path = os.path.splitext(selected_file_path)[0] + '_statistics.json'

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(statistics, f, indent=4, ensure_ascii=False)

    print(f'Statistics exported successfully to: {output_path}')


print('''
===========================================
    Welcome to The Text Analysis System!
===========================================
''')

while True:
    print('''
1. List available text files
2. Select and analyse a text file
3. Show basic statistics
4. Show word analysis
5. Show sentence analysis
6. Show character analysis
7. Visualise statistics
8. Export statistics
9. Exit
''')
    try:
        case = int(input('Enter your choice: '))

    except ValueError:
        print('Please enter an integer from 1 to 9')
        continue
    
    if case < 1 or case > 9:
        print('Please enter an integer from 1 to 9')
        continue


    match case:
        case 1:
    
            print('Your choice: List available text files')
            path = input('Please enter the folder path: ')
            result = find_file(path)
            if not result:
                continue
            else:
                selected_file = None
                selected_file_path = None
                selected_path = path


        case 2:

            if selected_path:
                path = selected_path
            else:
                path = input('Please enter the folder path: ')

            result = find_file(path)
            if not result:
                continue

            choose = correct_choose(result)

            print(f'Your choice is {result[choose]}')
            selected_file = result[choose]
            selected_file_path = os.path.join(path, selected_file)
            print('File selected successfully!')


        case 3:

            selected_file_path = file_path_detector(selected_file_path)
            print('''
Basic Satatistics
============================
            ''')
            analyse_text_basic(selected_file_path)
            


        case 4:
            
            selected_file_path = file_path_detector(selected_file_path)
            print('''
word analysis
============================
            ''')
            analyse_text_word(selected_file_path)
            unique_word_analysis(selected_file_path)
            word_length_distribution(selected_file_path)



        case 5:

            selected_file_path = file_path_detector(selected_file_path)
            print('''
sentence analysis
=============================
            ''')
            analyse_text_sentence(selected_file_path)
            longest_shortest_sentence(selected_file_path)


        case 6:
            selected_file_path = file_path_detector(selected_file_path)
            print('''
character analysis
=============================
            ''')
            character_analysis(selected_file_path)


        case 7:
            selected_file_path = file_path_detector(selected_file_path)
            print('''
visualise_statistics
=============================
            ''')
            visualise_statistics(selected_file_path)


        case 8:
            selected_file_path = file_path_detector(selected_file_path)
            print('''
Saving...
=============================
            ''')
            export_statistics(selected_file_path)


        case 9:
            print('Exiting, Goodbye!')
            break
