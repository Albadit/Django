import glob, sys


def read_lines_from_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as file_obj:
        return [line.strip() for line in file_obj if line.strip()]


def edit_html_file(file_basename: str, file_path: str) -> None:
    if file_basename not in read_lines_from_file(file_path):
        with open(file_path, 'w') as file_obj:
            file_obj.write(
                f"{{% extends 'base/base.html' %}}\n\n"
                f"{{% block title %}}\n{' ' * 4}{file_basename.capitalize()}\n{{% endblock title %}}\n\n"
                f"{{% block csslinks %}}\n{{% endblock csslinks %}}\n\n"
                f"{{% block content %}}\n{{% endblock content %}}\n"
            )


def add_urls_to_file(file_basename: str, urls_filename: str) -> None:
    text_context = read_lines_from_file(urls_filename)
    if not [element for element in text_context if file_basename in element]:
        with open(urls_filename, 'r', encoding='utf8') as file_obj:
            context = file_obj.readlines()
            context.insert(-1, f"{' ' * 4}path('{file_basename}/', views.{file_basename}, name='{file_basename}'),\n")
            with open(urls_filename, 'w') as file_obj:
                file_obj.writelines(context)


def add_view_to_file(file_basename: str, views_filename: str) -> None:
    if not [element for element in read_lines_from_file(views_filename) if file_basename in element]:
        with open(views_filename, 'a') as file_obj:
            file_obj.write(
                f"\n\ndef {file_basename}(request):\n"
                f"{' ' * 4}context = {{}}\n"
                f"{' ' * 4}return render(request, 'base/{file_basename}.html', context)\n"
            )


def edit_files( no_edit: list[str], head_folder: str, base_path: str) -> None:
    views_filename = f"{base_path}/{head_folder}/views.py"
    urls_filename = f"{base_path}/{head_folder}/urls.py"

    for file_path in glob.glob(f"{base_path}/**/*", recursive=True):
        file_basename = file_path.split('\\')[-1].split('.')[0]

        if file_path.endswith('.html') and file_basename not in no_edit:
            edit_html_file(file_basename, file_path)
            add_view_to_file(file_basename, views_filename)
            add_urls_to_file(file_basename, urls_filename)

if __name__ == '__main__':
    no_edit = ['base', 'navbar']
    base_path = sys.path[0]
    head_folder = 'base'

    edit_files(no_edit, head_folder, base_path)