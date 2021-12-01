import Text.Printf (printf)

inputPath = "inputdata"

countIncreases1 :: [Int] -> Int
countIncreases1 [] = 0
countIncreases1 [x] = 0
countIncreases1 (x:xs) = if x < head xs then 1 + countIncreases1 xs else 0 + countIncreases1 xs

countIncreases2 :: [Int] -> Int
countIncreases2 [] = 0
countIncreases2 [x] = 0
countIncreases2 (x:xs) = if sum(x:take 2 xs) < sum(take 3 xs) then 1 + countIncreases2 xs else 0 + countIncreases2 xs 

main :: IO ()
main = do 
    input <- map read.lines <$> readFile "inputdata"
    printf "First\t%d\n" $ countIncreases1 input
    printf "Second\t%d\n" $ countIncreases2 input
