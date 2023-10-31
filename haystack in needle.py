def strStr(haystack, needle):
    index = 0
    result = []
    
    while index < len(haystack):
        found_index = haystack.find(needle, index)
        if found_index == -1:
            break
        result.append(found_index)
        index = found_index + 1
    
    if not result:
        return -1
    
    return result
print(strStr('sadbutsad', 'sad')) 
