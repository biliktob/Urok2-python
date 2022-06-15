names = ["игорь", "maxim", "german", 120, 12.4, tuple("обычная строка"), set("babulya"), frozenset("babulka"), dict(key_1="дед1", key_2="дед2"), bool(20), ("текст".encode("utf-8")), bytearray(b"st"), type(None)]
for name in names:
    print(name)
    print(type(name))
