def main():
    alfavit = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ. ,!"
    key =     "GГRЕjIHЙКЛGD ПCGТУFХ#ЧШЩЪЫЬSЮЯАБ.A,!"  # Запутаем перехватчика данных, пусть зашифр сообщение начинается с осмысленного RSA 
    message = ""
    with open("Исходный_текст_1", mode="r", encoding="utf-8") as r_file:
        message = r_file.read()
    message = message.replace("\n", "")
    itog = ""
    for i in message.upper():
        tmp = alfavit.index(i)
        itog += key[tmp]
    with open("Ключ_к_тексту_1", mode="w+") as file:
        file.write(str(dict(zip(alfavit, key))))

    with open("Зашифрованный_текст_1", mode="w+") as file:
        file.write(itog)


if __name__ == "__main__":
    main()