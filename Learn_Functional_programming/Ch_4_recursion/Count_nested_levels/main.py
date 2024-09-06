def count_nested_levels(nested_documents, target_document_id, level=1):
    for key,value in nested_documents.items():
        if key == target_document_id:
            return level
        target_level = count_nested_levels(value,target_document_id,level=level+1)
        if target_level !=-1:
            return target_level
    return -1
