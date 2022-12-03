use std::fs;
use itertools::Itertools;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

fn calculate_priority(n: i32) -> i32 {
    if n - 96 > 0 {
        n - 96
    } else {
        n - 64 + 26
    }
}

fn part1(input: &String) -> i32 {
    input.split("\n")
        .map(|line| {
            let (l, r) = line.split_at(line.len()/2);
            let k = l.chars()
                .filter(|c| r.contains(&c.to_string()))
                .map(|c| c as i32).next();
            match k {
                Some(n) => calculate_priority(n), 
                None => 0,
            } 
        })
        .sum()
}

fn part2(input: &String) -> i32 {
    input.split("\n")
        .collect::<Vec<&str>>()
        .chunks(3)
        .map(|chunk| {
            if chunk.len() != 3 { 0 }
            else {
                let (f, s, t) = (chunk[0], chunk[1], chunk[2]);
                let k = f.chars()
                    .filter(|c| s.contains(&c.to_string()) && t.contains(&c.to_string()))
                    .map(|c| c as i32).next();
                match k {
                    Some(n) => calculate_priority(n), 
                    None => 0,
                }

            }})
        .sum()
}


