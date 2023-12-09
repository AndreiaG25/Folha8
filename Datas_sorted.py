import re

def extract_count_save_dates(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        date_indices = [match.start() for match in re.finditer(r'#DATE', content)]

        if date_indices:
            date_counts = {}
            for index in date_indices:
                text_after_date_tag = content[index:]
                match = re.search(r'#DATE.*?(\d{1,2}\s+de\s+[A-Za-zçã]+\s+de\s+\d{4})', text_after_date_tag)
                if match:
                    date = match.group(1)
                    date_counts[date] = date_counts.get(date, 0) + 1
            sorted_dates = dict(sorted(date_counts.items(), key=lambda item: item[1], reverse=True))

            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                for date, count in sorted_dates.items():
                    output_file.write(f"{date}: {count}\n")
                print(f"Extraction completed. Results saved in '{output_file_path}'.")
        else:
            print("No #DATE tags found.")

file_path = "folha8.OUT.txt"
output_file_path = "Datas_sorted.txt"
extract_count_save_dates(file_path, output_file_path)
