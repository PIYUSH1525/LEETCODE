/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let a = 0, b = 1;
    while (true) {
        yield a;     // yield current Fibonacci number
        [a, b] = [b, a + b]; // move forward in sequence
    }
};

/**
 * const gen = fibGenerator();
 * console.log(gen.next().value); // 0
 * console.log(gen.next().value); // 1
 * console.log(gen.next().value); // 1
 * console.log(gen.next().value); // 2
 * console.log(gen.next().value); // 3
 * // and so on...
 */