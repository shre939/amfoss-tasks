function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

const n = parseInt(prompt("Enter a number:"));
const primes = [];
for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
        primes.push(i);
    }
}
console.log(`Prime numbers up to ${n} are: ${primes}`);

