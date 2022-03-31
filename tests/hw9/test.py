import os
from pathlib import Path

import hw9
from tests.test_framework import *

TEST_DIR = Path(os.path.dirname(__file__))


def main():
    builder = TestBuilder("hw 9", 'hw9.py', linter_points=20, default_test_points=2)
    builder.add_items(build_get_words_test(10))
    builder.add_items(build_get_random_word_test(10))
    builder.add_items(build_letter_in_secret_word_test(10))
    builder.add_items(build_already_guessed_test(10))
    builder.add_items(build_make_hidden_secret_test(10))
    builder.add_items(build_won_test(10))
    builder.add_items(build_playing_test())
    builder.run()


def build_playing_test():
    test_name = 'play_command_line'
    section = Section(test_name)
    # secret word, guesses, outputs, is winner
    tests = [
        ('hello', ['h', 'e', 'l', 'o'], ['_ _ _ _ _', 'h _ _ _ _', 'h e _ _ _', 'h e l l _', 'hello'],
         True),
        ('walrus', ['w', 'a', 'e', 'o', 't', 'l', 's', 'u', 'r'],
         ['_ _ _ _ _ _', 'w _ _ _ _ _', 'w a _ _ _ _', 'w a _ _ _ _', 'w a _ _ _ _', 'w a _ _ _ _', 'w a l _ _ _',
          'w a l _ _ s', 'w a l _ u s', 'walrus'],
         True),
        ('abide', ['a', 'e', 'i', 'o', 'u', 'y', 's', 'u', 'v', 'r'],
         ['_ _ _ _ _', 'a _ _ _ _', 'a _ _ _ e', 'a _ i _ e', 'a _ i _ e', 'a _ i _ e', 'a _ i _ e', 'a _ i _ e',
          'a _ i _ e', 'a _ i _ e'],
         False),
        ('register', ['r', 'e', 'e', 'n', 'u', 'y', 's', 'u', 'v', 'r', 'j', 'k'],
         ['_ _ _ _ _ _ _ _', 'r _ _ _ _ _ _ r', 'r e _ _ _ _ e r', 'r e _ _ _ _ e r', 'r e _ _ _ _ e r',
          'r e _ _ _ _ e r', 'r e _ _ _ _ e r', 'r e _ _ s _ e r', 'r e _ _ s _ e r', 'r e _ _ s _ e r',
          'r e _ _ s _ e r', 'r e _ _ s _ e r'],
         False),
        ('lebowski', ['r', 's', 't', 'l', 'n', 'e', 'b', 'j', 'k', 'v', 'o', 'w', 'i'],
         ['_ _ _ _ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _ _ _ s _ _', '_ _ _ _ _ s _ _', 'l _ _ _ _ s _ _',
          'l _ _ _ _ s _ _', 'l e _ _ _ s _ _', 'l e b _ _ s _ _', 'l e b _ _ s _ _', 'l e b _ _ s k _',
          'l e b _ _ s k _', 'l e b o _ s k _', 'l e b o w s k _', 'lebowski'],
         True),
    ]
    for i, test in enumerate(tests):
        word = test[0]
        input = test[1]
        expected_progress = test[2]
        did_win = test[3]
        output, returned, errors = get_IO(lambda: hw9.play_command_line(word), input)
        if errors:
            section.add_items(
                Test(f'{test_name}_{i + 1}', True, False, show_actual_expected=False, exception_message=errors,
                     points=2))
        elif not output:
            section.add_items(
                Test(f'{test_name}_{i + 1}', True, False, show_actual_expected=False, exception_message='No output',
                     points=2))
        else:
            hidden_progress = [x for x in output if x.find('_') >= 0 or x.replace(' ', '') == word]
            if did_win and hidden_progress:
                last: str = hidden_progress[-1]
                hidden_progress = hidden_progress[:-1]
                hidden_progress.append(last.replace(' ', ''))
            section.add_items(Test(f'{test_name}_progress_{i + 1}', hidden_progress, expected_progress,
                                   data=[f'guessed letters: {input}', f'expected progression: {expected_progress}',
                                         f'actual progression: {hidden_progress}'], show_actual_expected=False))
            section.add_items(Test(f'{test_name}_winner_{i + 1}', ''.join(output).find('winner') >= 0, did_win,
                                   data=[f'guessed letters: {input}', f'expected progression: {expected_progress}',
                                         f'actual progression: {hidden_progress}'], show_actual_expected=False))
    return section


def build_won_test(n):
    test_name = 'won'
    section = Section(test_name)
    odds = [True, True, True, True, False]
    hidden_secrets = []
    results = []
    secret_words = []
    for i in range(n):
        secret_word = get_random_string().lower()
        secret_words.append(secret_word)
        hidden_secret = ''
        won = True
        for letter in secret_word:
            if random.choice(odds):
                hidden_secret += letter + ' '
            else:
                hidden_secret += '_ '
                won = False
        hidden_secret = hidden_secret[:-1]
        hidden_secrets.append(hidden_secret)
        results.append(won)
    hidden_secrets_gen = gen(hidden_secrets)
    results_gen = gen(results)
    secret_word_gen = gen(secret_words)
    for i in range(n):
        section.add_items(Test(f'{test_name}_{i + 1}', lambda: hw9.won(next(hidden_secrets_gen)), next(results_gen),
                               data=[f'guessed: {next(hidden_secrets_gen)}, secret word: {next(secret_word_gen)}']))
    return section


def build_make_hidden_secret_test(n):
    test_name = 'make_hidden_secret'
    section = Section(test_name)
    odds = [True, True, True, False]
    secret_words = []
    hidden_secrets = []
    guesses = []
    for i in range(n):
        secret_word = get_random_string().lower()
        secret_words.append(secret_word)
        hidden_secret = ''
        guessed_letters = []
        already_hidden_letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                hidden_secret += letter + ' '
            elif random.choice(odds) and letter not in already_hidden_letters:
                hidden_secret += letter + ' '
                if letter not in guessed_letters:
                    guessed_letters.append(letter)
            else:
                hidden_secret += '_ '
                already_hidden_letters.append(letter)
        hidden_secret = hidden_secret[:-1]
        hidden_secrets.append(hidden_secret)
        extra_guesses = random.randint(0, 5)
        j = 0
        while j < extra_guesses:
            letter = get_random_letter().lower()
            if letter not in secret_word and letter not in guessed_letters:
                guessed_letters.append(letter)
                j += 1
        guesses.append(guessed_letters)
    secret_words_gen = gen(secret_words)
    hidden_secrets_gen = gen(hidden_secrets)
    guesses_gen = gen(guesses)
    for i in range(n):
        section.add_items(
            Test(f'{test_name}_{i + 1}', lambda: hw9.make_hidden_secret(next(secret_words_gen), next(guesses_gen)),
                 next(hidden_secrets_gen),
                 data=[f'secret word: {next(secret_words_gen)}', f'guesses: {next(guesses_gen)}']))
    return section


def build_already_guessed_test(n):
    test_name = 'already_guessed'
    section = Section(test_name)
    guesses = []
    unguesses = []
    i = 0
    while i < n:
        random_letter = get_random_letter().lower()
        if random_letter not in guesses:
            guesses.append(random_letter)
            i += 1
    i = 0
    while i < n:
        random_letter = get_random_letter().lower()
        if random_letter not in guesses:
            unguesses.append(random_letter)
            i += 1
    letter_gen = gen(random.sample(guesses, n // 2))
    for i in range(n // 2):
        section.add_items(Test(f'{test_name}_{i + 1}', lambda: hw9.already_guessed(next(letter_gen), guesses), True,
                               data=[f'letter: {next(letter_gen)}, guesses: {guesses}']))
    unletter_gen = gen(random.sample(unguesses, n // 2))
    for i in range(n // 2):
        section.add_items(
            Test(f'{test_name}_{i + n // 2 + 1}', lambda: hw9.already_guessed(next(unletter_gen), guesses), False,
                 data=[f'letter: {next(unletter_gen)}, guesses: {guesses}']))
    return section


def build_letter_in_secret_word_test(n):
    test_name = 'letter_in_secret_word'
    section = Section(test_name)
    word = get_random_string(n // 2, n // 2)
    letter_gen = gen(list(word))
    for i in range(len(word)):
        section.add_items(Test(f'{test_name}_{i + 1}', lambda: hw9.letter_in_secret_word(next(letter_gen), word), True,
                               data=[f'letter: {next(letter_gen)}, word: {word}']))
    j = 0
    un_letters = []
    while j < n // 2:
        un_letter = get_random_letter()
        if un_letter not in word:
            un_letters.append(un_letter)
            j += 1
    unletter_gen = gen(un_letters)
    for k in range(len(un_letters)):
        section.add_items(
            Test(f'{test_name}_{k + n // 2 + 1}', lambda: hw9.letter_in_secret_word(next(unletter_gen), word),
                 False,
                 data=[f'letter: {next(unletter_gen)}, word: {word}']))
    return section


def build_get_random_word_test(n):
    section = Section('get_random_word')
    words = []
    for i in range(n):
        number_of_words = random.randint(1, 5)
        word_list = []
        for j in range(number_of_words):
            word = get_random_string()
            word_list.append(word + '\n')
        words.append(word_list)
    word_gen = gen(words)
    for i in range(n):
        word_list = next(word_gen)
        wl_no_newline = [x[:-1] for x in word_list]
        wl = [x[:-1] for x in word_list]
        removed = []
        error = None
        for j in range(500):
            outcome, result = run_safe(lambda: hw9.get_random_word(word_list))
            if not outcome:
                error = result
                break
            if result not in removed:
                try:
                    wl.remove(result)
                    removed.append(result)
                except ValueError:
                    error = f'returned result {result.encode("unicode_escape").decode("utf-8")} not in expected list {wl_no_newline}'
                    break
            if len(wl) == 0:
                break
        if error:
            data = [error]
        else:
            data = [f'words input: {word_list}', f'words not returned: {wl}']
        section.add_items(Test(f'get_random_word_{i + 1}', len(wl) == 0, True, data=data, show_actual_expected=False))
    return section


def build_get_words_test(n):
    section = Section('get_words')
    words = []
    file_names = []
    for i in range(n):
        file_name = f'get_words_test_{i}'
        file_names.append(TEST_DIR / file_name)
        file = open(TEST_DIR / f'{file_name}', 'w')
        word_count = random.randint(1, 5)
        word_list = []
        for j in range(word_count):
            word = get_random_string()
            print(word, file=file)
            word_list.append(word + '\n')
        words.append(word_list)
    file_name_gen = gen(file_names)
    word_gen = gen(words)
    for i in range(n):
        section.add_items(Test(f'get_words_{i + 1}', lambda: hw9.get_words(next(file_name_gen)), next(word_gen)))

    return section
