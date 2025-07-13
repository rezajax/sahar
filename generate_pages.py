#!/usr/bin/env python3
import os

TEMPLATE_PATH = os.path.join('site', 'page_template.html')
OUTPUT_DIR = os.path.join('site')

pages = {
    'alphabet.html': ('Armenian Alphabet', 'armenian_alphabet.md'),
    'grammar.html': ('Grammar Basics', 'armenian_grammar_basics.md'),
    'vocabulary1.html': ('Vocabulary Part 1', 'armenian_vocabulary_part1.md'),
    'vocabulary2.html': ('Vocabulary Part 2', 'armenian_vocabulary_part2.md'),
    'conversation.html': ('Conversation Practice', 'armenian_conversation_practice.md'),
    'comprehension.html': ('Comprehension Resources', 'armenian_comprehension_resources.md'),
    'a2test.html': ('A2 Practice Test', 'armenian_a2_practice_test.md'),
}

def main():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    for output_file, (title, md_path) in pages.items():
        html = template.replace('{{TITLE}}', title).replace('{{MARKDOWN_PATH}}', md_path)
        out_path = os.path.join(OUTPUT_DIR, output_file)
        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(html)
        print('Generated', out_path)

if __name__ == '__main__':
    main()
