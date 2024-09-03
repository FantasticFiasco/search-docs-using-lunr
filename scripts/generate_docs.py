from faker import Faker
import os

fake = Faker()

chapters_num = 89
for chapter in range(chapters_num):
    dir = os.path.join("..", "docs", f"chapter-{chapter + 1}")

    # os.makedirs(dir, exist_ok=True)

    # document_num = 10
    # for document in range(document_num):
    #     title = f"# {fake.city()}\n\n"
    #     content = fake.paragraph(nb_sentences=50)

    #     filename = os.path.join(dir, f"document-{document + 1}.md")

    #     with open(filename, 'w') as file:
    #         file.write(title)
    #         file.write(content)

    files = os.listdir(dir)

    for file_name in files:
        # Construct the full file path
        filename = os.path.join(dir, file_name)
        
        # Check if it's a file and not a directory
        if os.path.isfile(filename):
            for i in range(20):
                title = f"\n\n## {fake.city()}\n\n"
                content = fake.paragraph(nb_sentences=50)

                with open(filename, 'a') as file:
                    file.write(title)
                    file.write(content)
