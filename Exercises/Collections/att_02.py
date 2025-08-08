store_01 = {'Galaxy S24FE', 'iPhone 15', 'Pixel 8', 'OnePlus 11T', 'Xiaomi 13T'}

store_02 = {'Motorola Edge 40', 'iPhone 14', 'Pixel 8', 'Redmi Note 13 Pro', 'iPhone 15'}

models = store_01.union(store_02)

print(f'Available in the stores: {models}')

print(f'Available models in both stores: {store_01.intersection(store_02)}')