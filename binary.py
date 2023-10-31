def add_binary(a, b):
    carry = 0
    result = []
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    for i in range(max_len - 1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])
        bit_sum = bit_a + bit_b + carry
        carry = bit_sum // 2
        bit_sum = bit_sum % 2
        result.append(str(bit_sum))
    if carry:
        result.append('1')
    result = ''.join(result[::-1])
    return result
a = "11"
b = "1"
sum_binary = add_binary(a, b)
print(sum_binary) 
