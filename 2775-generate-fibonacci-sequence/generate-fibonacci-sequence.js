function* fibGenerator() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];  // Move to the next Fibonacci number
    }
}