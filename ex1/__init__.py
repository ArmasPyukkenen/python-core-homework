def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    return {
        "categories": [
            {
                "id": "category-" + category_data["id"],
                "text": category_data["name"],
                "items": [{
                    "id": id,
                    "text": mapping["roles"][id]["name"]
                    }
                    for id in category_data["roleIds"]]
            }
            for category_data in
            [mapping["categories"][category_id] for category_id in mapping["categoryIdsSorted"]]
        ]
    }
    pass
