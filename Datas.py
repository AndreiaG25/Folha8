import re

def extract_and_save_dates(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        date_indices = [match.start() for match in re.finditer(r'#DATE', content)]

        if date_indices:
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for index in date_indices:
                    text_after_date_tag = content[index:]

                    match = re.search(r'#DATE.*?(\d{1,2}\s+de\s+[A-Za-zçã]+\s+de\s+\d{4})', text_after_date_tag)

                    if match:
                        first_date = match.group(1)

                        output_file.write(f"{first_date}\n")
                        print(f"Datas saved in'{output_file_path}'")
                    else:
                        print("No date found after #DATE in the newspaper.")
        else:
            print("No #DATE tags found in the newspaper.")

file_path = "folha8.OUT.txt"
output_file_path = "Datas.txt"
extract_and_save_dates(file_path, output_file_path)
