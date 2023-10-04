compare_string1 = "EER239W-1 EER238W MER240W-1 MER241SS MER243W MER245W-1 MER245SS"
compare_array1 = compare_string1.split(" ")
result_array1 = []
for item in compare_array1:
    result_array1.append(item)

for item in compare_array1:
    item1 = item + '-RTV'
    result_array1.append(item1)

print(result_array1)


# input_string = "'ER82W', 'ER82SS', 'ER99SS', 'ER99W', 'ERR82BL-1', 'EFF100W', 'EFF104W', 'MFF100W', 'MFF104W', 'MFF120W', 'MFF122W', 'MFF120SS', 'MFF122SS', 'ER82W-RTV', 'ER82SS-RTV', 'ER99SS-RTV', 'ER99W-RTV', 'ERR82BL-1-RTV', 'EFF100W-RTV', 'EFF104W-RTV', 'MFF100W-RTV', 'MFF104W-RTV', 'MFF120W-RTV', 'MFF122W-RTV', 'MFF120SS-RTV', 'MFF122SS-RTV'"
# input_string = input_string.replace("'", "")
# result_array2 = input_string.split(", ")

# diff_array = []
