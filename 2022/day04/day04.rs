use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}


fn part1(input: &String) -> i32 {
    input.split('\n')
        .map(|l| {
            if l != "" {
                let intervals = l.split_once(',').unwrap();
                let (f1, s1) = intervals.0.split_once('-').unwrap();
                let (f2, s2) = intervals.1.split_once('-').unwrap();

                match ((f1.parse::<i32>().unwrap(),s1.parse::<i32>().unwrap()), (f2.parse::<i32>().unwrap(),s2.parse::<i32>().unwrap())) {
                    ((a,b),(c,d)) if a <= c && b >= d => 1,
                    ((a,b),(c,d)) if c <= a && d >= b => 1,
                    (_, _) => 0,
                }
            } else {0}
        })
        .sum()
}

fn part2(input: &String) -> i32 {
    input.split('\n')
        .map(|l| {
            if l != "" {
                let intervals = l.split_once(',').unwrap();
                let (f1, s1) = intervals.0.split_once('-').unwrap();
                let (f2, s2) = intervals.1.split_once('-').unwrap();

                match ((f1.parse::<i32>().unwrap(),s1.parse::<i32>().unwrap()), (f2.parse::<i32>().unwrap(),s2.parse::<i32>().unwrap())) {
                    ((a,b),(c,_d)) if a <= c && b >= c => 1,
                    ((a,b),(c,d)) if a >= c && b <= d => 1,
                    ((a,_b),(c,d)) if c <= a && d >= a => 1,
                    ((a,b),(c,d)) if c >= a && d <= b => 1,
                    ((a,b),(c,d)) if a <= c && b >= d => 1,
                    ((a,b),(c,d)) if c <= a && d >= b => 1,
 
                    (_, _) => 0,
                }
            } else {0}
        })
        .sum()

}


