#include <iostream>

using namespace std;

void okretanjeRedoslijeda(int niz[], int velicinaNiza)
{
    int kraj = niz[velicinaNiza];

    for(int i = kraj; i >= 0; i--)
    {
        cout << niz[i] << " ";
    }
}

void zamjenaClanova(int niz[], int index1, int index2, int velicinaNiza)
{
    int temp1, temp2;

    temp1 = niz[index1];
    temp2 = niz[index2];

    niz[index1] = temp2;
    niz[index2] = temp1;

    for(int i = 0; i <= velicinaNiza; i++)
    {
        cout << niz[i] << " ";
    }
}

void sortiranje(int niz[], string nacinSortiranja, int velicinaNiza)
{
    if(nacinSortiranja == "uzlazno")
    {
        for(int i = 0; i <= velicinaNiza; i++)
        {
            for(int j = 0; j <= velicinaNiza; j++ )
            {
                if(niz[i] < niz[j])
                {
                    int temp = niz[i];
                    niz[i] = niz[j];
                    niz[j] = temp;
                }
            }
        }
    }
    else if(nacinSortiranja == "silazno")
    {
        for(int i = 0; i <= velicinaNiza; i++)
        {
            for(int j = 0; j <= velicinaNiza; j++ )
            {
                if(niz[i] > niz[j])
                {
                    int temp = niz[i];
                    niz[i] = niz[j];
                    niz[j] = temp;
                }
            }
        }
    } 
    for(int i = 0; i <= velicinaNiza; i++)
    {
        cout << niz[i] << " ";
    }
    
}

int main()
{
    int niz[100], a = 0, b = 10, brojac = 0, manji, veci;

    if(a > b)
    {
        manji = b;
        veci = a;
    }
    else
    {
        manji = a;
        veci = b;
    }

    for(int i = manji; i < veci; i++) {
        brojac++;
    }
    for(int i = 0; i <= brojac; i++)
    {
        niz[i] = manji + i;
    }

    cout << "Okrenut niz: ";
    okretanjeRedoslijeda(niz, brojac);
    cout << endl;

    cout << "Niz kojimu su zamijenjena mjesta dvama clanovima: ";
    zamjenaClanova(niz, 2, 8, brojac);
    cout << endl;

    cout << "Sortirani ni po velicini uzlazno/silazno: ";
    sortiranje(niz, "silazno", brojac);
    cout << endl;

    return 0;
}