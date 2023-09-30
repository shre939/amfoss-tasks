isPrime :: Int -> Bool
isPrime num
    | num < 2 = False
    | otherwise = all (\i -> num `mod` i /= 0) [2..isqrt]
    where isqrt = floor (sqrt (fromIntegral num))

findPrimes :: Int -> [Int]
findPrimes n = [x | x <- [2..n], isPrime x]

main :: IO ()
main = do
    putStrLn "Enter a number: "
    n <- readLn
    let primes = findPrimes n
    putStrLn $ "Prime numbers up to " ++ show n ++ " are: " ++ show primes

