pub fn run(input: &str) {
    println!("Running 2025 Day 02 solution");
    part_a(input);
    part_b(input);
}

fn adjust(start: &str, end: &str) -> (String, String) {
    let start_half = if start.len() % 2 == 1 {
        format!("1{}", "0".repeat(start.len()/2))
    } else {
        start[..start.len()/2].to_string()
    };
    let end_half = if end.len() % 2 == 1 {
        "9".repeat(end.len()/2)
    } else {
        end[..end.len()/2].to_string()
    };
    // println!("First halves padded to '{start_half}' and '{end_half}'");
    (start_half, end_half)
}

fn sum_invalid(start: &str, end: &str) -> usize {
    // println!("Checking range {start}-{end}");
    let (start_half, end_half) = adjust(start, end);
    let (mut start_half_num, mut end_half_num) = (start_half.parse::<usize>().unwrap(), end_half.parse::<usize>().unwrap());
    if start_half_num > end_half_num {
        // println!("No valid numbers in range.\n");
        return 0;
    }
    let (low_repeated, high_repeated) = (format!("{start_half}{start_half}"), format!("{end_half}{end_half}"));
    let (low_num, high_num) = (low_repeated.parse::<usize>().unwrap(), high_repeated.parse::<usize>().unwrap());
    // println!("Checking low and high bounds...");
    let (start_num, end_num) = (start.parse::<usize>().unwrap(), end.parse::<usize>().unwrap());
    if low_num < start_num {
        start_half_num += 1;
        // println!("  Excluding low {low_repeated}");
    }
    if high_num > end_num {
        end_half_num -= 1;
        // println!("  Excluding high {high_repeated}");
    }
    // println!("  Valid range: {start_half_num} to {end_half_num}");
    if start_half_num > end_half_num {
        // println!("  No valid numbers in range.\n");
        return 0;
    }
    let mut sum = 0;
    for num in start_half_num..=end_half_num { sum += format!("{num}{num}").parse::<usize>().unwrap(); }
    // println!("Sum of invalid ids: {sum}\n");
    return sum;
}

fn part_a(input: &str) {
    let mut sum = 0;
    for range in input.to_string().split(',') {
        let (start, end) = range.split_at(range.find('-').unwrap());
        sum += sum_invalid(start, end[1..].trim());
    }
    println!("A) Sum of invalid ids: {sum}");
}

fn repeats(start: &str, end: &str, factor: usize) -> Vec<usize> {
    if start.len() < end.len() {
        let adj_start = format!("{}", 10_usize.pow(start.len() as u32));
        let adj_end = format!("{}", 10_usize.pow(start.len() as u32) - 1);
        let mut ids = repeats(start, &adj_end, factor);
        ids.extend(repeats(&adj_start, end, factor));
        return ids;
    }
    if factor >= end.len() { return Vec::new(); }
    // println!("  Adjusted range for repeat size {factor}: {start}-{end}");
    let mut ids: Vec<usize> = Vec::new();
    let (start_num, end_num) = (start.parse::<usize>().unwrap(), end.parse::<usize>().unwrap());
    if start_num > end_num { return ids; }
    for bit in start[..factor].parse::<usize>().unwrap()..=end[..factor].parse::<usize>().unwrap() {
        let rep_str = format!("{:0factor$}", bit).repeat(start.len() / factor);
        let rep_num = rep_str.parse::<usize>().unwrap();
        if rep_num < start_num || rep_num > end_num { continue; }
        ids.push(rep_num);
    }
    ids
}

fn sum_invalid_b(start: &str, end: &str) -> usize {
    // println!("Checking range {start}-{end}");
    let (len_l, len_h) = (start.len(), end.len());
    let (mut sum, mut ids) = (0, Vec::new());
    for i in 1..=5 {
        if i >= len_h { break; }
        if len_l % i != 0 && len_h % i != 0 { continue; }
        let (mut adj_start, mut adj_end) = (start.to_string(), end.to_string());
        if len_l % i != 0 {
            adj_start = format!("{}", 10_usize.pow(len_l as u32));
        }
        if len_h % i != 0 {
            adj_end = format!("{}", 10_usize.pow(len_l as u32) - 1);
        }
        // println!("  Checking repeat of first {i} digits...");
        let mut ids_i = repeats(&adj_start, &adj_end, i);
        ids.append(&mut ids_i);
    }
    ids.sort();
    ids.dedup();
    // println!("{ids:?}");
    for id in ids {
        // println!("    Found valid id: {id}");
        sum += id;
    }
    return sum;
}

fn part_b(input: &str) {
    let mut sum = 0;
    for range in input.to_string().split(',') {
        let (start, end) = range.split_at(range.find('-').unwrap());
        sum += sum_invalid_b(start, end[1..].trim());
    }
    println!("B) Sum of invalid ids: {sum}");
}