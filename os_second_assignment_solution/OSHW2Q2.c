#include <stdio.h>
#include <stdlib.h>

#ifdef _OPENMP
#include <omp.h>
#endif

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: matrix.txt num_threads\n");
        return 1;
    }

    // Read the number of threads from the command-line arguments
    int num_threads = atoi(argv[2]);
    omp_set_num_threads(num_threads);

    // Read the matrix from the text file
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    int rows, cols;
    
    fscanf(file, "%d %d", &rows, &cols);
    int **matrix = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; j++) {
            fscanf(file, "%d", &matrix[i][j]);
        }
    }

    fclose(file);

    // Calculate the sum of matrix elements using OpenMP
    int total_sum = 0;
    
    //printf("%d",rows);
    
    #pragma omp parallel for reduction(+:total_sum)
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            //printf("%d", matrix[i][j]);
            total_sum += matrix[i][j];
        }
        //printf("\n");
    }


// Print the number of threads (for debugging)
    //printf("Number of threads: %d\n", omp_get_max_threads());


    // Print the result
    printf("Sum of matrix elements: %d\n", total_sum);

    // Free dynamically allocated memory
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
    
    return 0;
}
