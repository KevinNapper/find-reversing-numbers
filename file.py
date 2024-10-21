def reverse_number(n):
    return int(str(n)[::-1])

# Numbers to try multiplying
for num in range(10, 10000000):
    rev_num = reverse_number(num)
    # Numbers to try multiplying by
    for multiplier in range(2, 100):
        product = num * multiplier
        if product == reverse_number(num):
            print(f"{num} * {multiplier} = {product}")
