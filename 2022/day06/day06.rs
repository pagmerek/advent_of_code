use itertools::Itertools;
use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

fn part1(input: &String) -> usize {
    for i in 3..input.len() {
        if input[(i - 3)..(i + 1)]
            .chars()
            .collect::<Vec<char>>()
            .iter()
            .unique()
            .count()
            == 4
        {
            return i + 1;
        }
    }
    return 0;
}

fn part2(input: &String) -> usize {
    for i in 13..input.len() {
        if input[(i - 13)..(i + 1)]
            .chars()
            .collect::<Vec<char>>()
            .iter()
            .unique()
            .count()
            == 14
        {
            return i + 1;
        }
    }
    return 0;
}
