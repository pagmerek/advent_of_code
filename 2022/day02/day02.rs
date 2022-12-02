use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    part1(&input);
    part2(&input);
}

fn calculate_score(x: &str, y: &str) -> i32 {
    match (x, y) {
        ("A", "X") => 4,
        ("A", "Y") => 8,
        ("A", "Z") => 3,
        ("B", "X") => 1,
        ("B", "Y") => 5,
        ("B", "Z") => 9,
        ("C", "X") => 7,
        ("C", "Y") => 2,
        ("C", "Z") => 6,
        (&_, _) => 0,
    }
}

fn part1(input: &String) {
    let result: i32 = input.split("\n")
        .map(|s| {
            match s.split_once(" ") {
                Some((fst, snd)) => calculate_score (fst,snd),
                None => 0,
            }
        })
        .sum();
    println!("part 1: {}", result);
}

fn calculate_strategy(x: &str, y: &str) -> i32 {
    match (x, y) {
        ("A", "X") => 0 + 3,
        ("A", "Y") => 3 + 1,
        ("A", "Z") => 6 + 2 ,
        ("B", "X") => 0 + 1,
        ("B", "Y") => 3 + 2,
        ("B", "Z") => 6 + 3,
        ("C", "X") => 0 + 2,
        ("C", "Y") => 3 + 3,
        ("C", "Z") => 6 + 1,
        (&_, _) => 0,
    }
}

fn part2(input: &String) {
    let result: i32 = input.split("\n")
        .map(|s| {
            match s.split_once(" ") {
                Some((fst, snd)) => calculate_strategy(fst,snd),
                None => 0,
            }
        })
        .sum();
    println!("part 2: {}", result);
}


