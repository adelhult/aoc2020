main :: IO ()
main = do
    file <- readFile "input.txt"
    let ns = map read $ lines file :: [Int]
    print $ head [a * b | a <- ns, b <- ns, a + b == 2020]
    print $ head [a * b * c | a <- ns, b <- ns, c <- ns, a + b + c == 2020]