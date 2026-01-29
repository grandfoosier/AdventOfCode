pub fn run(input: &str) {
    println!("Running 2025 Day 03 solution");
    part_a(input);
    part_b(input);
}

fn part_a(input: &str) {
    let mut sum = 0;
    for line in input.lines() {
        let digits: Vec<u32> = line
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect();
        let (mut tv, mut ti) = (0, 0);
        for i in 0..digits.len()-1 {
            if digits[i] > tv {
                tv = digits[i];
                ti = i;
            }
        }
        let mut ov = 0;
        for i in ti+1..digits.len() {
            if digits[i] > ov {
                ov = digits[i];
            }
        }
        sum += 10*tv + ov;
    }
    println!("A) Total output joltage: {sum}");
}

fn part_b(input: &str) {
let mut sum = 0;
    for line in input.lines() {
        let digits: Vec<usize> = line
            .chars()
            .filter_map(|c| c.to_digit(10).map(|o| o as usize))
            .collect();
        let mut value = 0;
        let mut next_index = 0;
        for index in next_index+1..digits.len()-11 {
            if digits[index] > digits[next_index] {
                next_index = index;
            }
        }
        let mut last_index = next_index;
        value = value*10 + digits[next_index];
        for round in 1..12 {
            let mut next_index = last_index+1;
            for index in next_index+1..digits.len()-(11-round) {
                if digits[index] > digits[next_index] {
                    next_index = index;
                }
            }
            last_index = next_index;
            value = value*10 + digits[next_index];
        }
        println!("Value for line: {value}");
        sum += value;
    }
    println!("B) Total output joltage: {sum}");
}