def create_files_summup(files_names: list):
    read_files = []
    for file_name in files_names:
        file_lines = read_file(file_name)
        read_files.append((file_name, str(len(file_lines)), ''.join(file_lines)))
    
    read_files_sorted = sorted(read_files, key=lambda x: len(x[2]))

    summup_text = '\n'.join(['\n'.join(file) for file in read_files_sorted])

    write_file('filessum/summup.txt', summup_text)


def read_file(filename, encoding='UTF-8', as_lines=True):
    with open('filessum/' + filename, encoding=encoding) as file:
        if as_lines:
            return [line for line in file.readlines()]
        
        return file.read()


def write_file(filename, text, encoding='UTF-8'):
    with open(filename, 'w', encoding=encoding) as file:
        file.write(text)


print(create_files_summup(['1.txt', '2.txt', '3.txt']))