from mon_premier_projet.module1 import hello_module1
from mon_premier_projet.module2 import add, sub
from mon_premier_projet.utilitaires.convert import conversion
from mon_premier_projet.utilitaires.maths import multiply
from mon_premier_projet.utilitaires.texte import to_upper_case


def main():
    print("coucou!")
    print(hello_module1())
    print("2 + 3 = ", add(2,3))
    print("6 - 3 = ", sub(6,3))
    print("multiply(2,3) = ", multiply(2,3))
    print(to_upper_case("exemple de texte"))
    print("conversion euro/ dollar = 50 / 1.08", conversion(50,1.08) , " dollar = 50/1.08")

   
if __name__ == "__main__":
    main()
