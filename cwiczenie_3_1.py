# one

shopping = {
    "castorama" : ['deska', 'gwoździe', 'taśma', 'młotek'],
    "ikea" : ['szafka', 'swieca', 'garnek'],
    "sklep modelarski" : ['model fiata 126p']
}
shopping["sklep papierniczy"] = ['ryza papieru']
all = 0

for shop in shopping:
    all = all + len(shopping[shop])
    print("Idę do", shop.capitalize(), "kupuję tu następujące rzeczy:", shopping[shop])


print(shopping.values())

print("W sumie kupuję", all, "produktów.")
