#include <omp.h>
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glib.h>
#include "prototype.h"

Result* ompDecrypt(int maxKey, int fromKey, int keyLen, char* inputData, size_t inputLen, GHashTable *wordSet) {
	int threadId;
	int i;
	char *key, *decrypted;

	// Allocate memory for result struct
	Result *result = (Result*) malloc(sizeof(Result));
	result->key = NULL;
	result->plaintext = NULL;

	// Set number of threads to use for work
	omp_set_num_threads(NUM_OF_THREADS);

	// Loop over all possible keys for given range
	#pragma omp parallel for
	for (i = fromKey; i < maxKey; i++) {
		// Get binary string representation fo key
		key = decimalToBinary(i, keyLen);
		// Try to decrypt the cipher with the current key
		decrypted = encryptDecrypt(key, keyLen, inputData, inputLen);
		// Check if the decrypted plaintext makes sense by matching it with the known words text
		if (validate(decrypted, wordSet)) {
			// Allocate memory for encryption key & plaintext
			result->key = (char*) malloc(keyLen * sizeof(char));
			result->plaintext = (char*) malloc(MAX_TEXT_LENGTH * sizeof(char));

			// Save encryption key & plaintext
			strcpy(result->key, key);
			strcpy(result->plaintext, decrypted);
		}
	}
	return result;
}
