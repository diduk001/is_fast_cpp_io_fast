# Small research on *⚡Blazing Fast⚡ C++ I/O* performance

Competitive programmers often use Fast I/O ([Codeforces Blog post #1](https://codeforces.com/blog/entry/6251), [Codeforces Blog post #2](https://codeforces.com/blog/entry/8080), [GeeksforGeeks' article](https://www.geeksforgeeks.org/fast-io-for-competitive-programming/)) by disabling C and C++ I/O buffer synchronization with `ios_base::sync_with_stdio(false)` and untying `cin` from `cout` with `cin.tie(0)`. So i tried to investigate on how significant is performance growth. 

> ⚠️ **Disclaimer: this research is made for having fun and learning technologies, it's not a scientific paper**

---

## Problem

Some code (including competitive programming sumbissions) must be really fast. Some methods make code faster with making faster algorithms or with making some technical stuff. Here we talk about C++-specific technical stuff.

In C++, there are two I/Os - old C's `printf/scanf` and *new* C++'s `cin/cout`. Each of them have its own buffer and by default synchronization betwenn C's buffer and C++'s buffer is enabled. So, each time when you put `cout` in your code, it automatically appends it into `printf` buffer. You may need this synchronization to mix C-style and C++-style I/O.

It is considered that disabling synchronization makes your code faster. Goal of this research is to study how the synchronization affects performance.

---

## Methodology

I wrote a target function:
```cpp
long long target_func(int arg) {
	long long res = 0;
	for (long long i = 1; i <= LOOP_ITERS; i++) {
		res += i ^ arg;
		res %= (i << 4 ^ 132) * arg;
	}
	return res;
```

And then called it a lot of times with different arguments measuring time with `std::chrono::high_resolution_clock::now();`. After that, I calculated average time for one function call, which is presented in the table.

I used two more parameters besides synchronization: output type (no output, C++'s `cout`, C's `printf`) and compiler's optimization level (O0, O2 and O3).

---

## Usage

1. Run `build.sh`. It creates "bin" directory and compiles source code
2. Run `run.sh`. It creates "outputs" directory, runs all binary files from "bin" and forwards output stream's last line to "outputs/$filename.out"
3. Run 'analysis.py' (it requires `matplotlib`). It shows you cool table 

---

## Results

After running it on my computer, I got this results:

*Average excution time, microseconds*

||sync_false|sync_true|
|---|-------|---------|
|no_io_O0|3564|3550|
|no_io_O2|0|0|
|no_io_O3|0|0|
|cout_O0|3553|3558|
|cout_O2|3553|3575|
|cout_O3|3557|3576|
|printf_O0|3571|3576|
|printf_O2|3560|3573|
|printf_O3|3555|3583|

**This results are strange.** I can explain, why O2 and O3 with no I/O is 0 microseconds (because O2 deletes unused code parts), but printf_O3 with synchronization on shouldn't be slower than printf_O2.

Some reasons, why this results might be strange:
- I use no input functions, just output
- <10 microseconds seems like an error
- It's too fast to measure

---

## TODO

✅ Make main part

✅ Make build and run shell scripts

⬜ Add comments

⬜ Pass `TEST_ITERS` and `LOOP_ITERS` through command line arguments

⬜ Add input

⬜ Rewrite building with [CMake](https://cmake.org)

⬜ Apply running in several threads

⬜ Make nicer results table

---

## P.S.

- I haven't included O1 optimization level because it's not really interesting for me. I don't know any cool O1 use case. 
- Some people say that C's I/O is faster than C++'s. That's why I included `cout` and `printf`.
- I will be happy if you contribute. Seriously,