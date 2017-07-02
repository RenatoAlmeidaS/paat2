#include <stdio.h>

int l_partition(int *a, int l, int r)
{
    int i, j, p, t;

    p = a[r];
    i = l;

    for(j = l; j <= r-1; j++) {
        if(a[j] <= p) {
            t = a[j];
            a[j] = a[i];
            a[i] = t;

            i++;
        }
    }

    t = a[i];
    a[i] = a[r];
    a[r] = t;

    return i;

}

void quicksort_lomuto(int *A,int lo,int hi){
    if (lo < hi){
        int p = l_partition(A, lo, hi);
        quicksort_lomuto(A, lo, p - 1);
        quicksort_lomuto(A, p + 1, hi);
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

	quicksort_lomuto(vetor, 0, 4);

	for ( i = 0; i < 5; ++i)
	
	{
		printf("%d ", vetor[i]);
	}

	printf("\n");

	return 0;
}