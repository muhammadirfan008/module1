import moduleAzizi
import moduleIrfan
import moduleSufiah


def main():

    moduleIrfan.moduleIrfan("irfan")


    a = moduleIrfan.person1["age"]
    print(a)

    moduleSufiah.moduleSufiah("Sufiah")

    a = moduleSufiah.person2["age"]
    print(a)

    moduleAzizi.moduleAzizi("Azizi")
    a = moduleAzizi.person3["age"]
    print(a)

if __name__ == '__main__':
    main()