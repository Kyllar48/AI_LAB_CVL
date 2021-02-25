import math

#cerinta 1
#
#Functie care returneaza ultimul cuvant dintr-un sir de caractere
#separate prin spatiu, dpdv lexicografic.
#Input:       -text=Un string, reprezinta sirul de caractere initial
#Output:      -ultimul cuvant al sirului de cuvinte din text, dpdv lexicografic.
#Complexitate timp:O(1)(O(logn) daca se ia in considerare si sort-ul)
#Complexitate spatiu:O(1)
def last_word(text):
    sir=text.split(' ')
    sir.sort(reverse=True)
    return sir[0]

#cerinta 2
#
#Functie care calculeaza distanta euclidiana dintre doua
#puncte, reprezentate prin perechile lor de coordonate (x,y)
#Input:(x1,y1),(x2,y2)-coordonatele celor 2 puncte in plan
#Output:nr-lungimea distantei cerute.
#Complexitate timp:O(1).
#Complexitate spatiu:O(1).
def distanta(x1,y1,x2,y2):
    return math.sqrt(((y2-y1)*(y2-y1)) + ((x2-x1)*(x2-x1)))

def test_cerinta1():
    assert last_word("Ana are mere rosii si galbene") == "si"
    assert last_word("De Mari la valoare") == "valoare"
    assert last_word("Merge treaba bine") == "treaba"
    assert last_word(" ") == ""

def test_cerinta2():
    assert distanta(1,5,4,1) == 5
    assert distanta(4,3,0,0) == 5
    assert distanta(5,12,11,4) == 10

def main():
    test_cerinta1()
    test_cerinta2()
    print("done")


main()
