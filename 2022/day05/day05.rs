use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

fn parse_stacks(structure: Vec<&str>) -> Vec<String> {
    let mut bins: Vec<String> = Vec::new();
    for x in (1..structure.last().unwrap().len()).step_by(4) {
        bins.push(
            structure
                .iter()
                .fold(String::new(), |mut acc: String, a| {
                    let c = a.as_bytes()[x] as char;
                    if c.is_alphabetic() {
                        acc.push(c);
                    }
                    acc
                })
                .chars()
                .rev()
                .collect::<String>(),
        );
    }
    return bins;
}

fn part1(input: &String) -> String {
    let mut i = input.split("\n\n");
    let (structure, commands) = (
        i.next().unwrap().split('\n').collect::<Vec<&str>>(),
        i.next().unwrap().split('\n'),
    );
    let mut bins = parse_stacks(structure);
    for l in commands {
        let cs = l.split(" ").collect::<Vec<&str>>();
        if cs.len() > 3 {
            let (amount, from, to): (i32, usize, usize) = (
                cs[1].parse().unwrap(),
                cs[3].parse().unwrap(),
                cs[5].parse().unwrap(),
            );
            for _ in 0..amount {
                match (*bins)[from - 1].pop() {
                    Some(x) => (*bins)[to - 1].push(x),
                    None => (),
                }
            }
        }
    } 
    bins.iter().map(|l| l.clone().pop().unwrap()).collect()
}

fn part2(input: &String) -> String {
    let mut i = input.split("\n\n");
    let (structure, commands) = (
        i.next().unwrap().split('\n').collect::<Vec<&str>>(),
        i.next().unwrap().split('\n'),
    );
    let mut bins = parse_stacks(structure);
    for l in commands {
        let cs = l.split(" ").collect::<Vec<&str>>();
        if cs.len() > 3 {
            let (amount, from, to): (i32, usize, usize) = (
                cs[1].parse().unwrap(),
                cs[3].parse().unwrap(),
                cs[5].parse().unwrap(),
            );
            let mut pack = String::new();
            for _ in 0..amount {
                match (*bins)[from - 1].pop() {
                    Some(x) => pack.insert(0, x),
                    None => (),
                }
            }
            (*bins)[to-1].push_str(&pack);
        }
    }
    bins.iter().map(|l| l.clone().pop().unwrap()).collect()
}
