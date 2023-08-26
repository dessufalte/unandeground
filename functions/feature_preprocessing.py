
def pprc_thread(input_text):
    lines = input_text.split('\n')
    title = None
    tags = []
    content = []

    for index, line in enumerate(lines):
        stripped_line = line.strip()
        if index == 0:
            title = f"{stripped_line}"
        elif stripped_line.startswith('#'):
            tags.append(stripped_line[1:])
        else:
            content.append(stripped_line)

    content_html = '<br>'.join(content)
    
    return title, tags, content_html
