def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    return {
        "categories" : [
            {
                "id" : "category-" + categoryData["id"],
                "text" : categoryData["name"],
                "items" : [{
                    "id": id,
                    "text": mapping["roles"][id]["name"]
                } 
                for id in categoryData["roleIds"]]
            } 
            for categoryData in
            [ mapping["categories"][categoryId] for categoryId in mapping["categoryIdsSorted"]]
        ]
    }
    pass
