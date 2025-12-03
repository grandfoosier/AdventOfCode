pub fn run(input: &str) {
    println!("Running 2025 Day 01 solution");
    part_a(input);
    part_b(input);
}

fn turn_right(current: i16, turn: i16) -> (i16, u16) {
    let n = current + turn;
    (n % 100, n as u16 / 100)
}

fn turn_left(current: i16, turn: i16) -> (i16, u16) {
    let (d, z) = turn_right((100 - current) % 100, turn);
    ((100 - d) % 100, z)
}

fn part_a(input: &str) {
    let (mut dial, mut zeroes) = (50, 0);
    for cmd in input.lines() {
        let (turn_dir, turn_amt) = cmd.split_at(1);
        let turn_amt: i16 = match turn_amt.parse() {
            Ok(n) => n,
            Err(_) => {
                eprintln!("Invalid turn amount in command '{cmd}'");
                continue;
            }
        };
        dial = match turn_dir {
            "R" => turn_right(dial, turn_amt).0,
            "L" => turn_left(dial, turn_amt).0,
            _ => {
                eprintln!("Invalid turn direction in command '{}'", cmd);
                continue;
            }
        };
        if dial == 0 { zeroes += 1; }
    }
    println!("A) Number of times dial hit zero: {zeroes}");
}

fn part_b(input: &str) {
    let (mut dial, mut zeroes) = (50, 0);
    for cmd in input.lines() {
        let (turn_dir, turn_amt) = cmd.split_at(1);
        let turn_amt: i16 = match turn_amt.parse() {
            Ok(n) => n,
            Err(_) => {
                eprintln!("Invalid turn amount in command '{cmd}'");
                continue;
            }
        };
        let (new, zs) = match turn_dir {
            "R" => turn_right(dial, turn_amt),
            "L" => turn_left(dial, turn_amt),
            _ => {
                eprintln!("Invalid turn direction in command '{}'", cmd);
                continue;
            }
        };
        dial = new;
        zeroes += zs;
    }
    println!("B) Number of times dial hit zero: {zeroes}");
}