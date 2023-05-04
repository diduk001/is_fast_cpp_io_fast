#include <chrono>
#include <cstdio>
#include <ios>
#include <iostream>

const int TEST_ITERS = 1000;
const int LOOP_ITERS = 1e6;

long long target_func(int arg) {
	long long res = 0;
	for (long long i = 1; i <= LOOP_ITERS; i++) {
		res += i ^ arg;
		res %= (i << 4 ^ 132) * arg;
	}
	return res;
}

int main() {
	auto start = std::chrono::high_resolution_clock::now();
	for (int i = 0; i < TEST_ITERS; i++) {
		int res = target_func(i + 1);
		printf("%d\n", res);
	}
	auto end = std::chrono::high_resolution_clock::now();
	auto duration =
		std::chrono::duration_cast<std::chrono::microseconds>(end - start);

	int average = duration.count() / TEST_ITERS;
	printf("%d microseconds\n", average);
}