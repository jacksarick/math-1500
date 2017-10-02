-- Remade in Haskell
-- Damn this language is cool

-- Unoptomized
-- let f_r r n = foldl (\x y -> r * x * (1.0 - x)) 0.5 [1..n]

-- let f = f_r 1.5
-- map f [1..10]

-- Lazy Eval FTW!!!
-- f_r :: Double -> [Double]
f_r r = iterate (\x -> r * x * (1.0 - x)) 0.5

-- f :: [Double]
f = f_r 1.5

print $ take 10 f