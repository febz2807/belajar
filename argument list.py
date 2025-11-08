def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total)

list_angka, total = jumlahkan(10, 10, 10, 10, 10)

# Mengambil data total
print(f"Total {list_angka} = {total}")


# Belajar tipe data dictionary

customer = {"Name":"Eko", "Age":30, "Address":"Jakarta"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "x"
customer["Name"] = "Eko Kurniawan"

del customer["Address"]

for key, value in customer.items():
    print(f"{key}:{value}")


def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "heelo python", style="paragraf")
print(html)
html = create_html("a", "ini link", href="www.google.com", style="Link")
print(html)
html = create_html ("div", "ini div", style="contoh")
print(html)

# module


