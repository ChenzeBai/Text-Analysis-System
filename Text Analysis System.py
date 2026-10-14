import os

selected_file = None
selected_path = None
selected_file_path = None


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


def analyse_text_basic(selected_file_path):
    word_list = []
    letter_count = 0
    with open(selected_file_path, 'r') as f:
        for line in f:
            words = line.split()
            letter_count += len(line.rstrip('\n'))
            for word in words:
                cleaned_word = word.lower().strip('.,!?;:"()[]{}')
                if cleaned_word != '':
                    word_list.append(cleaned_word)

        print(f'The number of words in the file is: {len(word_list)}')
        print(f'The number of characters(including spaces and punctuation) in the file is: {letter_count}')
        print(f'The number of unique words is: {len(set(word_list))}')


def analyse_text_word(selected_file_path):
    word_count = {}

    with open(selected_file_path, 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                word_cleaned = word.lower().strip('.,!?;:"()[]{}')

                if word_cleaned != '':
                    if word_cleaned in word_count:
                        word_count[word_cleaned] += 1
                    else:
                        word_count[word_cleaned] = 1
    
    first_count = 0
    second_count = 0
    third_count = 0

    for word in word_count:
        if word_count[word] > first_count:
            first_count = word_count[word]

    for word in word_count:
        if word_count[word] < first_count and word_count[word] > second_count:
            second_count = word_count[word]

    for word in word_count:
        if word_count[word] < second_count and word_count[word] > third_count:
            third_count = word_count[word]

    first_words = []
    second_words = []
    third_words = []

    for word in word_count:
        if word_count[word] == first_count:
            first_words.append(word)

        elif word_count[word] == second_count:
            second_words.append(word)

        elif word_count[word] == third_count:
            third_words.append(word)

    print('The most common words in the file are:')

    if first_words:
        print(f"1. {', '.join(first_words)} (appears {first_count} times)")

    if second_words:
        print(f"2. {', '.join(second_words)} (appears {second_count} times)")

    if third_words:
        print(f"3. {', '.join(third_words)} (appears {third_count} times)")


def file_path_detector(selected_file_path):
    if not selected_file_path:
        selected_file_path = input('Please enter your document path that you want to analysis')
    while not os.path.isfile(selected_file_path) or not selected_file_path.lower().endswith('.txt'):
        print('File does not exist. Please enter a valid file path enns with .txt')
        selected_file_path = input(
            'Please enter your document path: '
        )

    return selected_file_path


def sentence_analysis(selected_file_path);
    sentences = []
    with open(selected_file_path, 'r') as f:
        for line in f:
            sentence = line.split('.?!:')
            sentences.append(sentence)
    
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
=============================
                        ''')
            analyse_text_word(selected_file_path)



        case 5:
