population = {"Uk": 35, "usa": 45, "uae": 10, "ussr": 65}


def add():
    country = input("entry country name to add :")
    country=country.lower()
    if country in population:
        print("country already in our xx data. Terminating")
        return
    p=input(f"Enter the population for {country}")
    p = float(p)
    population[country] = p
    print_all()

def remove():
    country = input("entry country name to remove :")
    country=country.lower()
    if country not in population:
        print("country doesn't existin our xx data. Terminating")
        del population[country]
        return

def qwery():
    country = input("entry country name to qwery :")
    country=country.lower()
    if country in population:
        print("country already doesn't exists in our xx data. Terminating")
        return
    print(f"population of {country} is: {population[country]}millions")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op = input("Enter operation(add, remove,qwery or print")
    if op.lower()=="add":
        add()
    elif op.lower()=="remove":
        remove()
    elif op.lower()=="qwery":
        qwery()
    elif op.lower()=="print":
        print()

if __name__ =="__main__":
   main()
