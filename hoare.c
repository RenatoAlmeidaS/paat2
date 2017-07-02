#include <stdio.h>

int h_partition(int *a,int p, int r) {
    int x=a[p],i=p-1,j=r, aux;
    while (1) {
        do  j--; while (a[j] > x);
        do  i++; while (a[i] < x);
        if  (i < j) {
            aux = a[i];
            a[i] = a[j];
            a[j] = aux;
        }
        else 
            return j+1;
    }
}


void quicksort_hoare(int *A,int lo,int hi){
    if (lo < hi){
        int p = h_partition(A, lo, hi);
        quicksort_hoare(A, lo, p - 1);
        quicksort_hoare(A, p + 1, hi);
    }
}

int main(int argc, char const *argv[])
{
    int vetor[5] = {3, 2, 1, 4, 5}, i;

    for (int i = 0; i < 5; ++i)

    {
        printf("%d ", vetor[i]);
    }

    printf("\nvai rodar em\n");

    quicksort_hoare(vetor, 0, 4);

    for ( i = 0; i < 5; ++i)
    
    {
        printf("%d ", vetor[i]);
    }

    printf("\n");

    return 0;
}