import os
import yaml

def generate_nav(docs_dir):
    nav = []
    for root, dirs, files in os.walk(docs_dir):
        if root == docs_dir:
            continue
        folder_name = os.path.basename(root)
        folder_nav = {folder_name: []}
        for file in files:
            if file.endswith('.md'):
                file_name = os.path.splitext(file)[0]
                folder_nav[folder_name].append(f"{folder_name}/{file_name}")
        nav.append(folder_nav)
    return nav

def update_mkdocs_yml(mkdocs_file, nav):
    try:
        with open(mkdocs_file, 'r', encoding='utf-8') as f:
            mkdocs_config = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: {mkdocs_file} not found.")
        return
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return

    mkdocs_config['nav'] = nav

    try:
        with open(mkdocs_file, 'w', encoding='utf-8') as f:
            yaml.dump(mkdocs_config, f, default_flow_style=False, allow_unicode=True)
    except Exception as e:
        print(f"Error writing to YAML file: {e}")

if __name__ == "__main__":
    docs_directory = 'docs'
    mkdocs_file_path = 'mkdocs.yml'
    
    nav = generate_nav(docs_directory)
    update_mkdocs_yml(mkdocs_file_path, nav)
