import json

input_file = "packages.json"
output_file = "transformed_packages.json"


def transform_package(data):
    transformed = []
    for item in data:
        package = item.get("package", {})
        all_themes = []
        for phase in package.get("phases", []):
            for theme in phase.get("themes", []):
                all_questions = []
                theme_data = {
                    "name": theme.get("name"),
                }
                questions = theme.get("values", [])
                if questions is None:
                    continue
                for question in questions:
                    question_data = {
                        "comment": question.get("comment"),
                        "considered": question.get("considered"),
                    }
                    question_data.update(
                        {
                            "question": question.get("text"),
                            "answer": question.get("answer"),
                        }
                    )
                    all_questions.append(question_data)
                theme_data.update({"questions": all_questions})
            all_themes.append(theme_data)

        transformed_item = {
            "id": package.get("id"),
            "name": package.get("name"),
            "information": package.get("information"),
            "gameType": package.get("game", {}).get("id"),
            "editors": [
                editor.get("fullname") for editor in package.get("editors", [])
            ],
            "themes": all_themes,
        }
        transformed.append(transformed_item)
    return transformed


with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

transformed_data = transform_package(data)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(transformed_data, f, ensure_ascii=False, indent=4)

print(f"Succesfully finished: {output_file}")
